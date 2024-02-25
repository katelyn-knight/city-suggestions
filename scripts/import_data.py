import sys
sys.path.append('..')

from src import db
from src import app
from src.models.geoname_model import Geoname
import csv
from datetime import datetime

app.app_context().push()


def import_data_from_tsv(filename):
    csv.field_size_limit(sys.maxsize)

    with open(filename, 'r', encoding='utf-8') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        for row in reader:
            if not row['modified_at']:
                break
            # Convert modified_at to a datetime object
            modified_at_str = row['modified_at']
            if modified_at_str:
                modified_at = datetime.strptime(modified_at_str, "%Y-%m-%d")
            else:
                modified_at = None  # Or any default value you choose

            geoname = Geoname(
                name=row['name'],
                ascii_name=row['ascii'],
                alt_name=row['alt_name'],
                latitude=float(row['lat']),
                longitude=float(row['long']),
                feat_class=row['feat_class'],
                feat_code=row['feat_code'],
                country=row['country'],
                cc2=row['cc2'],
                admin1=row['admin1'],
                admin2=row['admin2'],
                admin3=row['admin3'],
                admin4=row['admin4'],
                population=int(row['population']) if row['population'] else None,
                elevation=int(row['elevation']) if row['elevation'] else None,
                dem=int(row['dem']) if row['dem'] else None,
                tz=row['tz'],
                modified_at=modified_at
            )
            db.session.add(geoname)
        db.session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 import_data.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    import_data_from_tsv(filename)
