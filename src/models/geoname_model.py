from sqlalchemy_serializer import SerializerMixin
from collections import OrderedDict

from .. import db

# Tables
# The main `geoname` table from [geonames.org](https://download.geonames.org/export/dump/) has the following fields :
"""
geonameid         : integer id of record in geonames database
name              : name of geographical point (utf8) varchar(200)
asciiname         : name of geographical point in plain ascii characters, varchar(200)
alternatenames    : alternatenames, comma separated varchar(5000)
latitude          : latitude in decimal degrees (wgs84)
longitude         : longitude in decimal degrees (wgs84)
feature class     : see http://www.geonames.org/export/codes.html, char(1)
feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
country code      : ISO-3166 2-letter country code, 2 characters
cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 60 characters
admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display
    names of this code; varchar(20)
admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
admin3 code       : code for third level administrative division, varchar(20)
admin4 code       : code for fourth level administrative division, varchar(20)
population        : bigint (8 byte int)
elevation         : in meters, integer
dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30''
(ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
timezone          : the timezone id (see file timeZone.txt) varchar(40)
modification date : date of last modification in yyyy-MM-dd format
"""


class Geoname(db.Model, SerializerMixin):
    __tablename__ = "geoname"

    serialize_only = ('id', 'name', 'country', 'admin1', 'latitude', 'longitude', 'population', 'tz')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ascii_name = db.Column(db.String(255))
    alt_name = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    feat_class = db.Column(db.String(10))
    feat_code = db.Column(db.String(10))
    country = db.Column(db.String(2))
    cc2 = db.Column(db.String(2))
    admin1 = db.Column(db.String(20))
    admin2 = db.Column(db.String(20))
    admin3 = db.Column(db.String(20))
    admin4 = db.Column(db.String(20))
    population = db.Column(db.Integer)
    elevation = db.Column(db.Integer)
    dem = db.Column(db.Integer)
    tz = db.Column(db.String(50))
    modified_at = db.Column(db.DateTime)

    def to_dict(self):
        return OrderedDict((key, getattr(self, key)) for key in self.serialize_only)

    def __repr__(self):
        return f"<City {self.name}>"
