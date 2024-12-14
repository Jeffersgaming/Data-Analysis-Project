# Modules for the program 
import matplotlib.pyplot as plt 
import mysql.connector 
import statistics 
import PySimpleGUI as sg 
 
# Database connection 
connector = mysql.connector.connect(host="localhost", user="root", passwd="root", database="practical") 
cursor = connector.cursor() 
 
# Main Program Menu 
while True: 
    layout = [ 
        [sg.Button("Create Pie Chart")], 
        [sg.Button("Display Bar Graph")], 
        [sg.Button("Display Line Graph")], 
        [sg.Button("Get Statistics")], 
        [sg.Button("Record Sales")], 
        [sg.Button("Create Scatter Point Graph")], 
        [sg.Button("Forecast or Calculate your Sales")], 
        [sg.Button("Exit")], 
    ] 
    window = sg.Window("Data Analysis GUI", layout, size=(400, 300)) 
    event, values = window.read() 
 
# To create pie chart  
    if event == "Create Pie Chart": 
        layout1 = [ 
            [sg.Text("Enter what do you want to analyze: "), sg.InputText(key="Title")], 
            [sg.Text("Enter labels separated by commas: "), sg.InputText(key="Labels")], 
            [sg.Text("Enter sizes separated by commas: "), sg.InputText(key="Sizes")], 
            [sg.Button("Generate Pie Chart"), sg.Button("Back")] 
        ] 
        window = sg.Window("Create Pie Chart", layout1) 
        while True: 
            event, values = window.read() 
            if event == sg.WINDOW_CLOSED or event == "Back": 
                break 
            if event == "Generate Pie Chart": 
                Title = values["Title"] 
                labels = values["Labels"].split(",") 
                sizes = list(map(int, values["Sizes"].split(","))) 
 
                plt.pie(sizes, labels=labels, autopct='%1.1f%%') 
                plt.title(f"Data Analysis of {Title} through Pie Chart") 
                plt.show() 
 
                insert_query = "INSERT INTO chart_info (chart_type, title, labels, sizes) VALUES (%s, %s, %s, %s)" 
                values = ("pie_chart", Title, ','.join(labels), ','.join(map(str, sizes))) 
                cursor.execute(insert_query, values)
                connector.commit() 
                print("Chart information saved!") 
        window.close() 
 
# To display bar graph 
    elif event == "Display Bar Graph": 
        layout1 = [ 
            [sg.Text("Enter what do you want to analyze: "), sg.InputText(key="Title")], 
            [sg.Text("Enter labels separated by commas: "), sg.InputText(key="Labels")], 
            [sg.Text("Enter sizes separated by commas: "), sg.InputText(key="Sizes")], 
            [sg.Button("Generate Bar Graph"), sg.Button("Back")] 
        ] 
        window = sg.Window("Create Bar Graph", layout1) 
 
        while True: 
            event, values = window.read() 
 
            if event == sg.WINDOW_CLOSED or event == "Back": 
                break 
 
            if event == "Generate Bar Graph": 
                Title = values["Title"] 
                labels = values["Labels"].split(",") 
                sizes = list(map(int, values["Sizes"].split(","))) 
 
                plt.bar(labels, sizes) 
                plt.xlabel("Labels") 
                plt.ylabel("Sizes") 
                plt.title(f"Data Analysis through Graph of {Title}") 
                plt.show() 
 
                insert_query = "INSERT INTO chart_info (chart_type, title, labels, sizes) VALUES (%s, %s, %s, %s)" 
                values = ("bar_graph", Title, ','.join(labels), ','.join(map(str, sizes))) 
                cursor.execute(insert_query, values) 
                connector.commit() 
                print("Chart information saved!") 
        window.close() 
 
# To display line graph 
    elif event == "Display Line Graph": 
        import PySimpleGUI as sg 
        import matplotlib.pyplot as plt 
 
        def create_line_graph_layout(): 
            return [ 
                [sg.Text("Enter what do you want to analyze: "), sg.InputText(key="Title")], 
                [sg.Text("How many data points do you want to enter: "), sg.InputText(key="NumPoints")], 
                [sg.Button("Generate Line Graph"), sg.Button("Back")] 
            ] 
        while True: 
            layout3 = [ 
                [sg.Button("Generate Line Graph"),
                 sg.Button("Back")] 
            ] 
            window = sg.Window("Line Graph", layout3, size=(400, 300)) 
            event, values = window.read() 
            if event == sg.WINDOW_CLOSED or event == "Back": 
                break 
 
            if event == "Generate Line Graph": 
                line_layout = create_line_graph_layout() 
                line_window = sg.Window("Generate Line Graph", line_layout) 
 
                while True: 
                    event, line_values = line_window.read() 
 
                    if event == sg.WINDOW_CLOSED or event == "Back": 
                        break 
 
                    if event == "Generate Line Graph": 
                        title = line_values["Title"] 
 
                        try: 
                            num_points = int(line_values["NumPoints"]) 
                        except ValueError: 
                            sg.popup_error("Invalid input. Please enter an integer.") 
                            continue 
 
                        x = [] 
                        y = [] 
                        for i in range(num_points): 
                            month = sg.popup_get_text("Enter month (In integer form)") 
                            while True: 
                                try: 
                                    sales = int(sg.popup_get_text("Enter sales (below 1000)")) 
                                    break 
                                except ValueError: 
                                    sg.popup_error("Invalid input. Please enter an integer.") 
                            x.append(month) 
                            y.append(sales) 
 
                        plt.plot(x, y) 
                        plt.xlabel("X-axis") 
                        plt.ylabel("Y-axis") 
                        plt.title(title) 
                        plt.show() 
                line_window.close() 
 
        window.close() 
 
# To enter data and get statistics 
    elif event == "Get Statistics": 
        layout3 = [ 
            [sg.Text("How many numbers do you want to enter? "), sg.InputText(key="Count")], 
            [sg.Button("Enter"), sg.Button("Back")]
             ] 
        window = sg.Window("Get Statistics", layout3) 
 
        while True: 
            event, values = window.read() 
 
            if event == sg.WINDOW_CLOSED or event == "Back": 
                break 
 
            if event == "Enter": 
                try: 
                    n = int(values["Count"]) 
                    my_list = [] 
                    for i in range(n): 
                        data = int(sg.popup_get_text(f"Enter a number ({i + 1}): ")) 
                        my_list.append(data) 
 
                    sg.popup_ok(f"Your list: {my_list}") 
 
                    mean = statistics.mean(my_list) 
                    median = statistics.median(my_list) 
                    mode = statistics.mode(my_list) 
                    stdev = statistics.stdev(my_list) 
                    variance = statistics.variance(my_list) 
 
                    sg.popup_ok( f"Mean: {mean}\nMedian: {median}\nMode: {mode}\nStandard Deviation: {stdev}\nVariance: {variance}") 
 
                    minimum = min(my_list) 
                    maximum = max(my_list) 
                    sg.popup_ok(f"Minimum: {minimum}\nMaximum: {maximum}") 
 
                except ValueError: 
                    sg.popup_error("Invalid input. Please enter an integer.") 
 
        window.close() 
 
# To make a record of sales  
    elif event == "Record Sales": 
        import mysql.connector 
        import PySimpleGUI as sg 
 
        connector = mysql.connector.connect(host="localhost", user="root", passwd="root", 
database="practical") 
        cursor = connector.cursor() 
 
        while True: 
            print("\nA: To create a record:") 
            print("B: To display the record:") 
            print("C: To search a product in the record:") 
            print("D: To add a product in the record:") 
            print("E: To delete a product from the record:") 
            print("F: To update a product in the record:") 
            print("Press any other key to exit the record:") 
 
            h = input('Enter your CHOICE:') 
 
            if h in ["A", "a"]: 
                while True: 
                    product_name = input("\nEnter the product name: ") 
                    quantity = int(input("Enter the quantity sold: ")) 
                    price = float(input("Enter the price per unit: ")) 
                    sale_date = input("Enter the sale date (YYYY-MM-DD): ") 
                    insert_query = "INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (%s, %s, %s, %s)" 
                    values = (product_name, quantity, price, sale_date) 
                    cursor.execute(insert_query, values) 
                    connector.commit() 
                    print("Record Created!") 
 
                    another_sale = input("Do you want to record another sale? Y/N: ").lower() 
                    if another_sale == 'y': 
                        continue 
                    else: 
                        break 
 
            elif h in ["B", "b"]: 
                def display_sales_records(): 
                    select_query = "SELECT * FROM sales" 
                    cursor.execute(select_query) 
                    records = cursor.fetchall() 
                    if not records: 
                        print("No sales records found.") 
                    else: 
                        print("Sales Records:") 
                        for record in records: 
                            print(f"ID: {record[0]}") 
                            print(f"Product Name: {record[1]}") 
                            print(f"Quantity: {record[2]}") 
                            print(f"Price: {record[3]}") 
                            print(f"Sale Date: {record[4]}") 
                            print("------------") 
 
 
                display_sales_records() 
 
            elif h in ["C", "c"]: 
                def search_sales_by_product_name(product_name): 
                    search_query = "SELECT * FROM sales WHERE product_name = %s" 
                    cursor.execute(search_query, (product_name,)) 
                    records = cursor.fetchall() 
                    if not records: 
                        print(f"No sales records found for product: {product_name}") 
                    else: 
                        print(f"Sales Records for product: {product_name}")
                        for record in records: 
                            print(f"ID: {record[0]}") 
                            print(f"Quantity: {record[1]}") 
                            print(f"Price: {record[2]}") 
                            print(f"Sale Date: {record[3]}") 
                            print("------------") 
 
 
                search_product_name = input("\nEnter the product name to search: ") 
                search_sales_by_product_name(search_product_name) 
 
            elif h in ["D", "d"]: 
                def add_sales_record(product_name, quantity, price, sale_date): 
                    insert_query = "INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (%s, %s, %s, %s)" 
                    values = (product_name, quantity, price, sale_date) 
                    cursor.execute(insert_query, values) 
                    connector.commit() 
                    print("New sales record added successfully.") 
 
 
                product_name = input("\nEnter the product name: ") 
                quantity = int(input("Enter the quantity sold: ")) 
                price = float(input("Enter the price per unit: ")) 
                sale_date = input("Enter the sale date (YYYY-MM-DD): ") 
                add_sales_record(product_name, quantity, price, sale_date) 
 
            elif h in ["E", "e"]: 
                def delete_sales_record(record_id): 
                    delete_query = "DELETE FROM sales WHERE id = %s" 
                    cursor.execute(delete_query, (record_id,)) 
                    connector.commit() 
                    print(f"Sales record with ID {record_id} has been deleted successfully.") 
 
 
                record_id = int(input("\nEnter the ID of the sales record to delete: ")) 
                delete_sales_record(record_id) 
 
            elif h in ["F", "f"]: 
                def update_sales_record(record_id, new_product_name, new_quantity, new_price, 
new_sale_date): 
                    update_query = "UPDATE sales SET product_name = %s, quantity = %s, price = %s, sale_date = %s WHERE id = %s" 
                    values = (new_product_name, new_quantity, new_price, new_sale_date, record_id) 
                    cursor.execute(update_query, values) 
                    connector.commit() 
                    print(f"Sales record with ID {record_id} has been updated successfully.") 
 
 
                record_id = int(input("Enter the ID of the sales record to update: ")) 
                new_product_name = input("Enter the new product name: ") 
                new_quantity = int(input("Enter the new quantity sold: ")) 
                new_price = float(input("Enter the new price per unit: "))
                new_sale_date = input("Enter the new sale date (YYYY-MM-DD): ") 
                update_sales_record(record_id, new_product_name, new_quantity, new_price, new_sale_date) 
 
            else: 
                exit() 
# To create a scatter point graph 
    elif event == "Create Scatter Point Graph": 
        import PySimpleGUI as sg 
        import matplotlib.pyplot as plt 
 
        def create_scatter_point_layout(): 
            return [ 
                [sg.Text("Enter the number of data points: "), sg.InputText(key="NumPoints")], 
                [sg.Button("Generate Scatter Point Graph"), sg.Button("Back")] 
            ] 
 
        while True: 
            layout6 = [ 
                [sg.Button("Generate Scatter Point Graph"), 
                 sg.Button("Back")] 
            ] 
 
            window = sg.Window("Scatter Point Graph", layout6) 
            event, values = window.read() 
 
            if event == sg.WINDOW_CLOSED or event == "Back": 
                break 
 
            if event == "Generate Scatter Point Graph": 
                scatter_layout = create_scatter_point_layout() 
                scatter_window = sg.Window("Generate Scatter Point Graph", scatter_layout) 
 
                while True: 
                    event, scatter_values = scatter_window.read() 
 
                    if event == sg.WINDOW_CLOSED or event == "Back": 
                        break 
 
                    if event == "Generate Scatter Point Graph": 
                        try: 
                            num_points = int(scatter_values["NumPoints"]) 
                        except ValueError: 
                            sg.popup_error("Invalid input. Please enter an integer.") 
                            continue 
 
                        x_values = [] 
                        y_values = [] 
                        for i in range(num_points): 
                            x = float(sg.popup_get_text(f"Enter x value for data point {i + 1}: ")) 
                            y = float(sg.popup_get_text(f"Enter y value for data point {i + 1}: ")) 
                            x_values.append(x) 
                            y_values.append(y)
                            plt.figure(figsize=(8, 6)) 
                        plt.scatter(x_values, y_values) 
                        plt.title('Scatter Plot') 
                        plt.xlabel('X values') 
                        plt.ylabel('Y values') 
                        plt.grid(True) 
                        plt.show() 
                scatter_window.close() 
        window.close() 
 
# To forecast or calculate the sales 
    elif event == "Forecast or Calculate your Sales": 
        import pandas as pd 
        import PySimpleGUI as sg 
 
        def calculate_sales_forecast(): 
            return [ 
                [sg.Text("How many products did you have at the starting point: "), 
                 sg.InputText(key="StartingProducts")], 
                [sg.Text("Enter approx how much increment in sales you are observing: "), 
                 sg.InputText(key="Increment")], 
                [sg.Button("Calculate Sales Forecast"), sg.Button("Back")] 
            ] 
        while True: 
            layout7 = [ 
                [sg.Button("Calculate Sales Forecast"), 
                 sg.Button("Back")] 
            ] 
            window = sg.Window("Sales Forecast and Calculation", layout7) 
            event, values = window.read() 
            if event == sg.WINDOW_CLOSED or event == "Back": 
                break 
 
            if event == "Calculate Sales Forecast": 
                forecast_layout = calculate_sales_forecast() 
                forecast_window = sg.Window("Calculate Sales Forecast", forecast_layout) 
                while True: 
                    event, forecast_values = forecast_window.read() 
                    if event == sg.WINDOW_CLOSED or event == "Back": 
                        break 
 
                    if event == "Calculate Sales Forecast": 
                        try: 
                            starting_products = int(forecast_values["StartingProducts"]) 
                            increment = int(forecast_values["Increment"]) 
                        except ValueError: 
                            sg.popup_error("Invalid input. Please enter integer values.") 
                            continue 
 
                        sales_data = { 
                            'Date': pd.date_range(start='2024-01-01', periods=365),  # Dates 
                            'Sales': [starting_products + 2 * increment + 2 * (increment % 7) for increment in 
                                      range(365)]  # Sales values
                         } 
                        sales_df = pd.DataFrame(sales_data) 
 
                        start_date = pd.to_datetime(sg.popup_get_text("Enter start date (YYYY-MM-DD): ")) 
                        end_date = pd.to_datetime(sg.popup_get_text("Enter end date (YYYY-MM-DD): ")) 
 
                        period_sales = sales_df.loc[(sales_df['Date'] >= start_date) & (sales_df['Date'] <= end_date)] 
                        total_sales = period_sales['Sales'].sum() 
 
                        sg.popup( 
                            f"Total sales from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m%d')}: {total_sales}\n") 
                forecast_window.close() 
        window.close() 
    if event == sg.WINDOW_CLOSED or event == "Exit": 
        break 