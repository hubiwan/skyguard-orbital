from sgp4.api import Satrec, jday
import requests
import datetime
import math

DEMO_TLES = [
    "ISS (ZARYA)", "1 25544U 98067A   23165.53406645  .00014736  00000+0  26651-3 0  9996", "2 25544  51.6416 336.7865 0005470 102.3925 348.7402 15.50060936401083",
    "TIANGONG", "1 48274U 21035A   23165.66060598  .00025732  00000+0  16886-3 0  9992", "2 48274  41.4727 340.5273 0006764 266.3887 184.2882 15.60337223117462",
    "HUBBLE (HST)", "1 20580U 90037B   23165.23652853  .00001854  00000+0  67078-4 0  9997", "2 20580  28.4695 277.6320 0003050 248.8354 186.2084 15.08868615654320",
    "NOAA 19 (WEATHER)", "1 33591U 09005A   23165.50495944  .00000103  00000+0  97486-4 0  9994", "2 33591  99.1384 148.8687 0014167 197.8085 162.2612 14.12464195741632",
    "STARLINK-1007", "1 44713U 19074A   23165.33020613  .00003264  00000+0  23385-3 0  9998", "2 44713  53.0536 179.9190 0001643  96.5332 263.5855 15.06394354190828",
    "ENVISAT (DEBRIS)", "1 27386U 02009A   23165.12345678  .00000200  00000+0  12345-3 0  9991", "2 27386  98.0000 100.0000 0001000 100.0000 100.0000 14.00000000000000",
    "GPS IIR-M7", "1 32711U 08012A   23165.00000000  .00000050  00000+0  00000+0 0  9991", "2 32711  55.0000  60.0000 0100000 120.0000 200.0000  2.00500000000000",
    "GALILEO 22", "1 43055U 17079A   23165.00000000  .00000000  00000+0  00000+0 0  9998", "2 43055  56.0000 120.0000 0005000 180.0000 100.0000  1.70000000000000",
    "METOP-C", "1 43689U 18087A   23165.51862140  .00000155  00000+0  10309-3 0  9995", "2 43689  98.6976 137.9620 0001091  79.2890 280.8520 14.21503362239460",
    "SENTINEL-6", "1 46984U 20086A   23165.00000000  .00001000  00000+0  10000-4 0  9990", "2 46984  66.0000 300.0000 0001000  90.0000 270.0000 13.00000000000000",
    "IRIDIUM 167", "1 43933U 19002K   23165.00000000  .00001000  00000+0  10000-3 0  9999", "2 43933  86.0000 150.0000 0001000 100.0000 100.0000 14.00000000000000",
    "COSMOS 2251 (DEBRIS)", "1 33762U 93036BJM 23164.92817399  .00078129  00000+0  22199-2 0  9993", "2 33762  74.0345 233.1932 0038827 232.0970 127.4262 14.71866444641364",
    "FENGYUN 1C (DEBRIS)", "1 29701U 99025BPM 23165.00000000  .00010000  00000+0  10000-3 0  9999", "2 29701  99.0000 120.0000 0100000 100.0000 100.0000 14.00000000000000",
    "TERRA", "1 25994U 99068A   23165.00000000  .00000100  00000+0  10000-4 0  9999", "2 25994  98.0000 180.0000 0001000 100.0000 100.0000 14.00000000000000",
    "AQUA", "1 27424U 02022A   23165.00000000  .00000100  00000+0  10000-4 0  9999", "2 27424  98.0000 190.0000 0001000 100.0000 100.0000 14.00000000000000",
    "LANDSAT 8", "1 39084U 13008A   23165.00000000  .00000100  00000+0  10000-4 0  9999", "2 39084  98.0000 200.0000 0001000 100.0000 100.0000 14.00000000000000",
    "SUOMI NPP", "1 37849U 11061A   23165.00000000  .00000100  00000+0  10000-4 0  9999", "2 37849  98.0000 210.0000 0001000 100.0000 100.0000 14.00000000000000",
    "CALIPSO", "1 29108U 06016A   23165.00000000  .00000100  00000+0  10000-4 0  9999", "2 29108  98.0000 220.0000 0001000 100.0000 100.0000 14.00000000000000",
    "CLOUDSAT", "1 29107U 06016B   23165.00000000  .00000100  00000+0  10000-4 0  9999", "2 29107  98.0000 230.0000 0001000 100.0000 100.0000 14.00000000000000",
    "O3B FM20", "1 44388U 19020D   23165.00000000  .00000100  00000+0  10000-4 0  9999", "2 44388   0.0000 240.0000 0001000 100.0000 100.0000  5.00000000000000"
]

LOCATIONS = {
    "POLAND (Warsaw)": {"lat": 52.2297, "lng": 21.0122},
    "USA (Washington DC)": {"lat": 38.9072, "lng": -77.0369},
    "CHINA (Beijing)": {"lat": 39.9042, "lng": 116.4074},
    "UK (London)": {"lat": 51.5074, "lng": -0.1278},
    "JAPAN (Tokyo)": {"lat": 35.6762, "lng": 139.6503},
    "RUSSIA (Moscow)": {"lat": 55.7558, "lng": 37.6173}
}

class SatelliteTracker:
    def __init__(self):
        self.tles = DEMO_TLES

    def get_current_positions(self):
        satellites = []
        i = 0
        while i < len(self.tles) - 2:
            name = self.tles[i].strip()
            line1 = self.tles[i+1]
            line2 = self.tles[i+2]
            i += 3
            try:
                sat_obj = Satrec.twoline2rv(line1, line2)
                now = datetime.datetime.utcnow()
                jd, fr = jday(now.year, now.month, now.day, now.hour, now.minute, now.second)
                e, r, v = sat_obj.sgp4(jd, fr)
                if e == 0:
                    x, y, z = r[0], r[1], r[2]
                    vx, vy, vz = v[0], v[1], v[2]
                    r_km = math.sqrt(x*x + y*y + z*z)
                    lat = math.degrees(math.asin(z/r_km))
                    lng = math.degrees(math.atan2(y, x)) - ((now.hour*60 + now.minute) * 0.25)
                    lng = (lng + 180) % 360 - 180
                    speed_kms = math.sqrt(vx*vx + vy*vy + vz*vz)
                    speed_kmh = speed_kms * 3600
                    satellites.append({
                        'name': name,
                        'lat': lat,
                        'lng': lng,
                        'alt': (r_km - 6371) / 6371 * 0.5,
                        'real_alt': round(r_km - 6371, 1),
                        'speed': round(speed_kmh, 0)
                    })
            except:
                continue
        return satellites

    def get_trajectory(self, sat_name):
        path = []
        line1, line2 = None, None
        i = 0
        while i < len(self.tles) - 2:
            if self.tles[i].strip() == sat_name:
                line1, line2 = self.tles[i+1], self.tles[i+2]
                break
            i += 3
        if not line1:
            return []
        sat_obj = Satrec.twoline2rv(line1, line2)
        start_time = datetime.datetime.utcnow()
        for minutes in range(0, 95, 2):
            future_time = start_time + datetime.timedelta(minutes=minutes)
            jd, fr = jday(future_time.year, future_time.month, future_time.day, future_time.hour, future_time.minute, future_time.second)
            e, r, v = sat_obj.sgp4(jd, fr)
            if e == 0:
                x, y, z = r[0], r[1], r[2]
                r_km = math.sqrt(x*x + y*y + z*z)
                lat = math.degrees(math.asin(z/r_km))
                lng = math.degrees(math.atan2(y, x)) - ((future_time.hour*60 + future_time.minute + minutes) * 0.25)
                lng = (lng + 180) % 360 - 180
                path.append([lat, lng, (r_km - 6371) / 6371 * 0.5])
        return [path]

    def predict_passes(self, country_name):
        target = LOCATIONS.get(country_name)
        if not target:
            return []
        predictions = []
        i = 0
        while i < len(self.tles) - 2:
            name = self.tles[i].strip()
            line1 = self.tles[i+1]
            line2 = self.tles[i+2]
            i += 3
            sat_obj = Satrec.twoline2rv(line1, line2)
            found_pass = False
            for minutes in range(0, 720, 15):
                future_utc = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes)
                jd, fr = jday(future_utc.year, future_utc.month, future_utc.day, future_utc.hour, future_utc.minute, future_utc.second)
                e, r, v = sat_obj.sgp4(jd, fr)
                if e == 0:
                    x, y, z = r[0], r[1], r[2]
                    r_km = math.sqrt(x*x + y*y + z*z)
                    sat_lat = math.degrees(math.asin(z/r_km))
                    sat_lng = math.degrees(math.atan2(y, x)) - ((future_utc.hour*60 + future_utc.minute) * 0.25)
                    sat_lng = (sat_lng + 180) % 360 - 180
                    dist = math.sqrt((sat_lat - target['lat'])**2 + (sat_lng - target['lng'])**2)
                    if dist < 20:
                        future_pl = future_utc + datetime.timedelta(hours=1)
                        time_str = future_pl.strftime("%H:%M PL")
                        if minutes == 0:
                            time_str = "NOW"
                        predictions.append({
                            'name': name,
                            'time': time_str,
                            'minutes_away': minutes
                        })
                        found_pass = True
                        break
            if not found_pass:
                predictions.append({
                    'name': name,
                    'time': "NO PASS < 12h",
                    'minutes_away': 9999
                })
        predictions.sort(key=lambda x: x['minutes_away'])
        return predictions
