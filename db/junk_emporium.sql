DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    product_description TEXT,
    stock_level INT,
    buy_cost INT,
    sell_cost INT,
    manufacturer_id INT NOT NULL REFERENCES manufacturers(id)
);