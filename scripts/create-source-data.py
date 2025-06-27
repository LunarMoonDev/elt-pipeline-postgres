import psycopg2
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

conn_params = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'database',
    'user': 'sample',
    'password': 'example'
}

def clean_database():
    """Clean the database by deleting tables"""

    with psycopg2.connect(**conn_params) as conn, conn.cursor() as cur:
        cur.execute(""" 
            SELECT table_schema, table_name 
            FROM information_schema.tables
            WHERE table_type = 'BASE TABLE'
                AND table_schema NOT IN ('pg_catalog', 'information_schema');
        """)
        tables = cur.fetchall()

        for schema, table in tables:
            truncate_sql = f'TRUNCATE TABLE "{schema}"."{table}" RESTART IDENTITY CASCADE;'
            cur.execute(truncate_sql)
        
        logging.info('Existing tables truncated and sequences reset.')
    

def load_sales_to_db():
    """Generate data for database with sales tables"""

    with psycopg2.connect(**conn_params) as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS public.sales_ph (
                sales_id INT NOT NULL,
                quantity_sold INT NOT NULL,
                unit_sell_price DECIMAL(10, 2) NOT NULL,
                unit_purchase_cost DECIMAL(10, 2) NOT NULL,
                sales_date DATE NOT NULL,
                updated_at TIMESTAMP NULL,
                PRIMARY KEY (sales_id)
            ); 
        """)

        sales_ph_data = [
            (1, 5, 1200.00, 950.00, '2024-07-15', '2024-08-01 10:00:00'),
            (2, 2, 999.99, 800.00, '2024-07-15', '2024-08-01 10:00:00'),
            (3, 1, 699.99, 500.00, '2024-07-16', '2024-08-01 10:00:00'),
            (4, 3, 499.99, 350.00, '2024-07-17', '2024-08-01 10:00:00'),
            (5, 4, 199.99, 150.00, '2024-07-18', '2024-08-01 10:00:00'),
            (6, 2, 49.99, 30.00, '2024-07-19', '2024-08-01 10:00:00'),
            (7, 6, 1200.00, 950.00, '2024-06-30', '2024-08-01 10:00:00'),
            (8, 1, 999.99, 800.00, '2024-07-01', '2024-08-01 10:00:00'),
            (9, 3, 699.99, 500.00, '2024-07-10', '2024-08-01 10:00:00'),
            (10, 2, 499.99, 350.00, '2024-06-25', '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO public.sales_ph (
                sales_id, quantity_sold, unit_sell_price, unit_purchase_cost, sales_date, updated_at
            ) VALUES (%s, %s, %s, %s, %s, %s);
            """, sales_ph_data)
        
        logging.info('sales_ph table created and populated.')

        cur.execute("""
            CREATE TABLE IF NOT EXISTS sales_uk (
                sales_id INT NOT NULL,
                quantity_sold INT NOT NULL,
                unit_sell_price DECIMAL(10, 2) NOT NULL,
                unit_purchase_cost DECIMAL(10, 2) NOT NULL,
                sales_date DATE NOT NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (sales_id) 
            );
        """)

        sales_uk_data = [
            (1, 5, 1200.00, 950.00, '2024-07-15', '2024-08-01 10:00:00'),
            (2, 2, 999.99, 800.00, '2024-07-15', '2024-08-01 10:00:00'),
            (3, 1, 699.99, 500.00, '2024-07-16', '2024-08-01 10:00:00'),
            (4, 3, 499.99, 350.00, '2024-07-17', '2024-08-01 10:00:00'),
            (5, 4, 199.99, 150.00, '2024-07-18', '2024-08-01 10:00:00'),
            (6, 2, 49.99, 30.00, '2024-07-19', '2024-08-01 10:00:00'),
            (7, 6, 1200.00, 950.00, '2024-06-30', '2024-08-01 10:00:00'),
            (8, 1, 999.99, 800.00, '2024-07-01', '2024-08-01 10:00:00'),
            (9, 3, 699.99, 500.00, '2024-07-10', '2024-08-01 10:00:00'),
            (10, 2, 499.99, 350.00, '2024-06-25', '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO public.sales_uk (
                sales_id, quantity_sold, unit_sell_price, unit_purchase_cost, sales_date, updated_at
            ) VALUES (%s, %s, %s, %s, %s, %s);
            """, sales_uk_data)
        
        logging.info('sales_uk table created and populated.')

def load_oms_to_db():
    """Generate data for database with oms tables"""
    
    with psycopg2.connect(**conn_params) as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Dates (
                Date DATE NOT NULL,
                Day VARCHAR(3) NULL,
                Month VARCHAR(10) NULL,
                Year VARCHAR(4) NULL,
                Quarter INT NULL,
                DayOfWeek VARCHAR(10) NULL,
                WeekOfYear INT NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (Date)
            );
        """)

        dates_data = [
            ('2024-01-01', 'Mon', 'January', '2024', 1, 'Monday', 1, '2024-08-01 10:00:00'),
            ('2024-01-02', 'Tue', 'January', '2024', 1, 'Tuesday', 1, '2024-08-01 10:00:00'),
            ('2024-01-03', 'Wed', 'January', '2024', 1, 'Wednesday', 1, '2024-08-01 10:00:00'),
            ('2024-01-04', 'Thu', 'January', '2024', 1, 'Thursday', 1, '2024-08-01 10:00:00'),
            ('2024-01-05', 'Fri', 'January', '2024', 1, 'Friday', 1, '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO Dates (Date, Day, Month, Year, Quarter, DayOfWeek, WeekOfYear, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, dates_data)
        
        logging.info('Dates table created and populated.')

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                CustomerID VARCHAR(10),
                FirstName VARCHAR(50),
                LastName VARCHAR(50),
                Email VARCHAR(100),
                Phone VARCHAR(100),
                Address VARCHAR(100),
                City VARCHAR(50),
                State VARCHAR(2),
                ZipCode VARCHAR(10),
                Updated_at TIMESTAMP
            );
        """)

        customers_data = [
            ('C001', 'John', 'Doe', 'john.doe@example.com', '555-0100', '123 Main St', 'Springfield', 'IL', '62701', '2024-08-01 10:00:00'),
            ('C002', 'Jane', 'Smith', 'jane.smith@example.com', '555-0101', '456 Oak St', 'Springfield', 'IL', '62702', '2024-08-01 10:00:00'),
            ('C003', 'Alice', 'Johnson', 'alice.johnson@example.com', '555-0102', '789 Pine St', 'Springfield', 'IL', '62703', '2024-08-01 10:00:00'),
            ('C004', 'Bob', 'Brown', 'bob.brown@example.com', '555-0103', '101 Maple St', 'Springfield', 'IL', '62704', '2024-08-01 10:00:00'),
            ('C005', 'Charlie', 'Davis', 'charlie.davis@example.com', '555-0104', '202 Birch St', 'Springfield', 'IL', '62705', '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO customers (CustomerID, FirstName, LastName, Email, Phone, Address, City, State, ZipCode, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, customers_data)

        logging.info('Customers table created and populated.')
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeID INT NOT NULL,
                FirstName VARCHAR(100) NULL,
                LastName VARCHAR(100) NULL,
                Email VARCHAR(200) NULL,
                JobTitle VARCHAR(100) NULL,
                HireDate DATE NULL,
                ManagerID INT NULL,
                Address VARCHAR(200) NULL,
                City VARCHAR(50) NULL,
                State VARCHAR(50) NULL,
                ZipCode VARCHAR(10) NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (EmployeeID)
            );
            """)

        employees_data = [
            (1, 'Tom', 'Hanks', 'tom.hanks@example.com', 'Manager', '2022-01-15', None, '101 Maple St', 'Springfield', 'IL', '62701', '2024-08-01 10:00:00'),
            (2, 'Emma', 'Watson', 'emma.watson@example.com', 'Sales Associate', '2023-02-20', 1, '202 Birch St', 'Springfield', 'IL', '62702', '2024-08-01 10:00:00'),
            (3, 'Mark', 'Smith', 'mark.smith@example.com', 'Developer', '2021-03-10', 1, '303 Cedar St', 'Springfield', 'IL', '62703', '2024-08-01 10:00:00'),
            (4, 'Lucy', 'Williams', 'lucy.williams@example.com', 'HR', '2020-04-25', 1, '404 Oak St', 'Springfield', 'IL', '62704', '2024-08-01 10:00:00'),
            (5, 'David', 'Jones', 'david.jones@example.com', 'Support', '2019-05-30', 2, '505 Pine St', 'Springfield', 'IL', '62705', '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, JobTitle, HireDate, ManagerID, Address, City, State, ZipCode, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, employees_data)
        
        logging.info('Employees table created and populated.')
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Stores (
                StoreID INT NOT NULL,
                StoreName VARCHAR(100) NULL,
                Address VARCHAR(200) NULL,
                City VARCHAR(50) NULL,
                State VARCHAR(50) NULL,
                ZipCode VARCHAR(10) NULL,
                Email VARCHAR(200) NULL,
                Phone VARCHAR(50) NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (StoreID)
            );
            """)

        stores_data = [
            (1000, 'Main Street Store', '111 Main St', 'Springfield', 'IL', '62701', 'mainstore@example.com', '555-0120', '2024-08-01 10:00:00'),
            (2, 'Downtown Store', '222 Elm St', 'Springfield', 'IL', '62702', 'downtownstore@example.com', '555-0121', '2024-08-01 10:00:00'),
            (3, 'Eastside Store', '333 Oak St', 'Springfield', 'IL', '62703', 'eastsidestore@example.com', '555-0122', '2024-08-01 10:00:00'),
            (4, 'Westside Store', '444 Birch St', 'Springfield', 'IL', '62704', 'westsidestore@example.com', '555-0123', '2024-08-01 10:00:00'),
            (5, 'Southside Store', '555 Cedar St', 'Springfield', 'IL', '62705', 'southsidestore@example.com', '555-0124', '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO Stores (StoreID, StoreName, Address, City, State, ZipCode, Email, Phone, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, stores_data)
        
        logging.info('Stores table created and populated.')
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Suppliers (
                SupplierID INT NOT NULL,
                SupplierName VARCHAR(100) NULL,
                ContactPerson VARCHAR(100) NULL,
                Email VARCHAR(200) NULL,
                Phone VARCHAR(50) NULL,
                Address VARCHAR(50) NULL,
                City VARCHAR(50) NULL,
                State VARCHAR(10) NULL,
                ZipCode VARCHAR(10) NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (SupplierID)
            );
            """)

        # Insert 10 records
        suppliers_data = [
            (1, 'ABC Supplies', 'Robert Brown', 'robert.brown@abc.com', '555-0130', '123 Supply St', 'Springfield', 'IL', '62701', '2024-08-01 10:00:00'),
            (2, 'XYZ Corp', 'Susan Green', 'susan.green@xyz.com', '555-0131', '456 Warehouse St', 'Springfield', 'IL', '62702', '2024-08-01 10:00:00'),
            (3, '123 Distributors', 'Nancy White', 'nancy.white@123.com', '555-0132', '789 Distribution St', 'Springfield', 'IL', '62703', '2024-08-01 10:00:00'),
            (4, 'Tech Supplies', 'James Black', 'james.black@tech.com', '555-0133', '101 Tech St', 'Springfield', 'IL', '62704', '2024-08-01 10:00:00'),
            (5, 'Home Supplies', 'Michael Blue', 'michael.blue@home.com', '555-0134', '202 Home St', 'Springfield', 'IL', '62705', '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO Suppliers (SupplierID, SupplierName, ContactPerson, Email, Phone, Address, City, State, ZipCode, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, suppliers_data)
        
        logging.info('Suppliers table created and populated.')
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                ProductID INT NOT NULL,
                Name VARCHAR(100) NULL,
                Category VARCHAR(100) NULL,
                RetailPrice DECIMAL(10,2) NULL,
                SupplierPrice DECIMAL(10,2) NULL,
                SupplierID INT NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (ProductID)
            );
            """)

        products_data = [
            (1, 'Laptop', 'Electronics', 999.99, 800.00, 1, '2024-08-01 10:00:00'),
            (2, 'Smartphone', 'Electronics', 699.99, 500.00, 2, '2024-08-01 10:00:00'),
            (3, 'Tablet', 'Electronics', 499.99, 350.00, 3, '2024-08-01 10:00:00'),
            (4, 'Monitor', 'Electronics', 199.99, 150.00, 4, '2024-08-01 10:00:00'),
            (5, 'Keyboard', 'Electronics', 49.99, 30.00, 5, '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO Products (ProductID, Name, Category, RetailPrice, SupplierPrice, SupplierID, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, products_data)
        
        logging.info('Products table created and populated.')
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS OrderItems (
                OrderItemID INT NOT NULL,
                OrderID INT NULL,
                ProductID INT NULL,
                Quantity INT NULL,
                UnitPrice DECIMAL(10,2) NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (OrderItemID)
            );
            """)

        orderitems_data = [
            (1, 1, 1, 1, 999.99, '2024-08-01 10:00:00'),
            (2, 2, 2, 1, 699.99, '2024-08-01 10:00:00'),
            (3, 3, 3, 2, 499.99, '2024-08-01 10:00:00'),
            (4, 4, 4, 1, 199.99, '2024-08-01 10:00:00'),
            (5, 5, 5, 3, 49.99, '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity, UnitPrice, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, orderitems_data)
        
        logging.info('OrderItems table created and populated.')
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                OrderID INT NOT NULL,
                OrderDate DATE NULL,
                CustomerID VARCHAR NULL,
                EmployeeID INT NULL,
                StoreID INT NULL,
                Status VARCHAR(10) NULL,
                Updated_at TIMESTAMP NULL,
                PRIMARY KEY (OrderID)
            );
            """)

        orders_data = [
            (1, '2024-07-15', 'C001', 1, 1000, '01', '2024-08-01 10:00:00'),
            (2, '2024-07-16', 'C002', 2, 2, '01', '2024-08-01 10:00:00'),
            (3, '2024-07-17', 'C003', 3, 3, '03', '2024-08-01 10:00:00'),
            (4, '2024-07-18', 'C004', 4, 4, '02', '2024-08-01 10:00:00'),
            (5, '2024-07-19', 'C005', 5, 5, '03', '2024-08-01 10:00:00')
        ]

        cur.executemany("""
            INSERT INTO Orders (OrderID, OrderDate, CustomerID, EmployeeID, StoreID, Status, Updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, orders_data)
        
        logging.info('Orders table created and populated.')

if __name__ == "__main__":
    clean_database()
    load_sales_to_db()
    load_oms_to_db()
    logging.info('Data loaded to SQLite database successfully.')