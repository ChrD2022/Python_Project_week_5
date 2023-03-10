DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(255),
    manufacturer_location VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    buy_cost INT,
    sell_cost INT,
    manufacturer_id INT NOT NULL REFERENCES manufacturers(id)
);