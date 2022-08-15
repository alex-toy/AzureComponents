# Azure Components

Azure Synapse Analytics is changing the way we work with data services in Azure. The ASA workspace combines the core technologies required for **data warehousing**, **Big Data Analytics** and **Data Science**.

In this project, we will use **Synapse Analytics** to solve the paradox of analytics with a unified analytical platform where **data analysts**, **data engineers** and **data scientists** can all perform essential tasks in the same workspace. 

We will use such tools as **Dedicated and Serverless SQL Pools**, integration with **Azure Data Lake**, performing **ETL** with **pipelines** and **data flows**, **Synapse notebooks** and finally the built-in Power BI integration capabilities.

Here are the steps to follow along :

## Creating resources

1. Create an **Azure Synapse Workspace**
<img src="/pictures/synapse-workspace.png" title="synapse workspace"  width="700">

2. Create an **Azure SQL database**
<img src="/pictures/sql.png" title="sql database"  width="700">

3. Create an **Azure Storage Account**
<img src="/pictures/storage-account.png" title="storage account"  width="700">

4. Create an **Azure PostgreSQL Database** (use Flexible Server, workload type development, add a firewall rule to allow access from any azure service)
<img src="/pictures/postgres.png" title="postgres"  width="700">

Then run **python DataToPostgres.py** in order to populate the PostgreSQL database. You will then be able to see the data later on, when we create a **Linked Service**.

5. Create a **Dedicated SQL pools**
<img src="/pictures/sql-pool.png" title="dedicated sql pool"  width="700">


## Ingesting data into Azure Synapse

1. Go to the **Linked Services** section
<img src="/pictures/linked-services.png" title="linked services"  width="700">

2. Create an **Azure Database for PostgreSQL** linked service. For **Encryption**, choose **Request SSL**.
<img src="/pictures/linked-service-postgres.png" title="linked services postgres"  width="300">

3. Create an **Azure Blob storage** linked service
<img src="/pictures/linked-service-blob.png" title="linked services blob storage"  width="300">

4. in order to create a **Linked Service** Go to the **Home/Ingest** section and select **Built-in copy task** and **Run once now**.
<img src="/pictures/home-ingest.png" title="ingest"  width="700">

5. Then select **Azure Database for PostgreSQL** as a source
<img src="/pictures/postgres-source.png" title="postgres source"  width="700">

6. Then add a destination link to **Azure Blob Storage** as a source
<img src="/pictures/link-destination.png" title="link destination"  width="700">

In the data section, you will find your newly created link :
<img src="/pictures/newly-created-link.png" title="newly created link"  width="700">

7. Create external table
<img src="/pictures/create-external-table.png" title="create external table"  width="300">

Then run the script to create a **staging table** :
<img src="/pictures/external-table-script.png" title="external table script"  width="700">

You can then go to your workspace and run a query on the newly created table :
<img src="/pictures/newly-created-table.png" title="external table script"  width="700">

