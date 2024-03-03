using System;
using System.Data.SqlClient;

class Program
{
    static void Main()
    {
        // Connection string
        string connectionString = "Data Source=LAPTOP-IQ4KLOUE; Integrated Security=True;Initial Catalog=LAPTOPIQ4KLOUE";

        try
        {
            // Create a SqlConnection object
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                // Open the connection
                connection.Open();

                // Create a SqlCommand object for the stored procedure
                using (SqlCommand command = new SqlCommand("YourStoredProcedureName", connection)) // Replace "YourStoredProcedureName" with the actual name of your stored procedure
                {
                    // Set the command type to stored procedure
                    command.CommandType = System.Data.CommandType.StoredProcedure;

                    // Execute the command and get a SqlDataReader
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        // Check if there are rows returned
                        if (reader.HasRows)
                        {
                            // Iterate through the rows
                            while (reader.Read())
                            {
                                // Retrieve values from the columns
                                int ID = reader.GetInt32(0);
                                string CATEGORY = reader.GetString(1);
                                decimal EXPENSEAMOUNT = reader.GetDecimal(2);

                                // Print or process the retrieved data as needed
                                Console.WriteLine($"File ID: {ID}, Category Name: {CATEGORY}, Expense Amount: {EXPENSEAMOUNT}");
                            }
                        }
                        else
                        {
                            Console.WriteLine("No rows found.");
                        }
                    } // Close the SqlDataReader
                } // Close the SqlCommand
            } // Close the SqlConnection
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }
}