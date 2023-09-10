import mysql.connector
import json
import openpyxl


def get_mysql_config():
    # Load MySQL configuration from config.json
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    return config


def create_connection():
    # Create a MySQL connection using the configuration from config.json
    config = get_mysql_config()
    connection = mysql.connector.connect(
        host=config["MYSQL_HOST"],
        user=config["MYSQL_USER"],
        password=config["MYSQL_PASSWORD"],
        database=config["MYSQL_DB"]
    )
    return connection


def close_connection(connection):
    # Close the MySQL connection
    connection.close()


def insert_customer_data(data):
    # Insert customer data into the customer_master table
    connection = create_connection()
    cursor = connection.cursor()

    # Define the SQL query to insert data into the table
    sql_query = """
        INSERT INTO customer_master (
            client_name, address, customer_type, purchase_contact, purchase_email, purchase_mobile,
            project_head, project_email, project_mobile, design_contact, design_email, design_mobile,
            quality_contact, quality_email, quality_mobile, account_contact, account_email, account_mobile,
            customer_rating, discount_details, overhead_details, priority_details,
            total_offer_sent, total_po_recovered, total_business
        )
        VALUES (%(client_name)s, %(address)s, %(customer_type)s, %(purchase_contact)s, %(purchase_email)s,
                %(purchase_mobile)s, %(project_head)s, %(project_email)s, %(project_mobile)s,
                %(design_contact)s, %(design_email)s, %(design_mobile)s, %(quality_contact)s,
                %(quality_email)s, %(quality_mobile)s, %(account_contact)s, %(account_email)s,
                %(account_mobile)s, 'A', %(discount_details)s, %(overhead_details)s,
                %(priority_details)s, %(total_offer_sent)s, %(total_po_recovered)s, %(total_business)s)
    """

    # Execute the query with data as a dictionary
    cursor.execute(sql_query, data)

    # Commit the changes and close the connection
    connection.commit()
    close_connection(connection)

    # Create a new Excel workbook
    workbook = openpyxl.Workbook()

    # Create a new worksheet
    worksheet = workbook.active

    # Add headers to the worksheet
    headers = [
        "Client Name",
        "Address",
        "Customer Type",
        "Purchase Contact",
        "Purchase Email",
        "Purchase Mobile",
        "Project Head",
        "Project Email",
        "Project Mobile",
        "Design Contact",
        "Design Email",
        "Design Mobile",
        "Quality Contact",
        "Quality Email",
        "Quality Mobile",
        "Account Contact",
        "Account Email",
        "Account Mobile",
        "Customer Rating",
        "Discount Details",
        "Overhead Details",
        "Priority Details",
        "Total Offer Sent",
        "Total PO Recovered",
        "Total Business"
    ]
    worksheet.append(headers)

    # Extract data from the 'data' dictionary and add it to the worksheet
    row = [
        data["client_name"],
        data["address"],
        data["customer_type"],
        data["purchase_contact"],
        data["purchase_email"],
        data["purchase_mobile"],
        data["project_head"],
        data["project_email"],
        data["project_mobile"],
        data["design_contact"],
        data["design_email"],
        data["design_mobile"],
        data["quality_contact"],
        data["quality_email"],
        data["quality_mobile"],
        data["account_contact"],
        data["account_email"],
        data["account_mobile"],
        'A',
        data["discount_details"],
        data["overhead_details"],
        data["priority_details"],
        data["total_offer_sent"],
        data["total_po_recovered"],
        data["total_business"]
    ]
    worksheet.append(row)

    # Save the workbook with a desired filename
    excel_filename = "/home/anand/PycharmProjects/Project/Records/client_data.xlsx"
    workbook.save(excel_filename)


def get_all_customers():
    # Retrieve all customer records from the customer_master table
    connection = create_connection()
    cursor = connection.cursor()

    # Define the SQL query to select all records from the table
    sql_query = "SELECT * FROM customer_master"

    cursor.execute(sql_query)
    result = cursor.fetchall()

    # Close the connection and return the result
    close_connection(connection)
    return result
