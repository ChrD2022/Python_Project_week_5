dropdb junk_emporium

createdb junk_emporium

psql -d junk_emporium -f db/junk_emporium.sql

python3 console.py