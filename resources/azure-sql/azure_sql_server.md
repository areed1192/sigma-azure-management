# Create a managed instance

Link: <https://docs.microsoft.com/en-us/azure/azure-sql/managed-instance/instance-create-quickstart>

To create a managed instance, follow these steps:

## Step 1: Sign in to the Azure portal

If you don't have an Azure subscription, create a free account.

1. Sign in to the Azure portal.
2. Select Azure SQL on the left menu of the Azure portal. If Azure SQL is not in the list, select All services, and then enter Azure SQL in the search box.
3. Select + Add to open the Select SQL deployment option page. You can view additional information about Azure SQL Managed Instance by selecting Show details on the SQL managed instances tile.
4. Select Create.

## Step 2: Basics tab

Fill out mandatory information required on the Basics tab. This is a minimum set of information required to
provision a managed instance.

Use the table below as a reference for information required at this tab.

| Setting                      | Suggested value                                              | Description                                                                                                              |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Subscription                 | Your subscription.                                           | A subscription that gives you permission to create new resources.                                                        |
| Resource group               | A new or existing resource group.                            | For valid resource group names, see Naming rules and restrictions.                                                       |
| Managed instance name        | Any valid name.                                              | For valid names, see Naming rules and restrictions.                                                                      |
| Region                       | The region in which you want to create the managed instance. | For information about regions, see Azure regions.                                                                        |
| Managed instance admin login | Any valid username.                                          | For valid names, see Naming rules and restrictions. Don't use "serveradmin" because that's a reserved server-level role. |
| Password                     | Any valid password.                                          | The password must be at least 16 characters long and meet the defined complexity requirements.                           |

Select Configure Managed Instance to size compute and storage resources and to review the pricing tiers. Use the sliders or text boxes to specify the amount of storage and the number of virtual cores. When you're finished, select Apply to save your selection.

## Step 3: Networking tab

Fill out optional information on the Networking tab. If you omit this information, the portal will apply default settings.

Use the table below as a reference for information required at this tab.

| Setting                                           | Suggested value                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Virtual network                                   | Select either Create new virtual network or a valid virtual network and subnet. | If a network or subnet is unavailable, it must be modified to satisfy the network requirements before you select it as a target for the new managed instance. For information about the requirements for configuring the network environment for SQL Managed Instance, see Configure a virtual network for SQL Managed Instance.                                                                                                                                                                                                                                                                                                                                    |
| Connection type                                   | Choose between a proxy and a redirect connection type.                          | For more information about connection types, see Azure SQL Managed Instance connection type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Public endpoint                                   | Select Enable.                                                                  | For a managed instance to be accessible through the public data endpoint, you need to enable this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Allow access from (if Public endpoint is enabled) | Select one of the options.                                                      | The portal experience enables configuring a security group with a public endpoint. Based on your scenario, select one of the following options: Azure services: We recommend this option when you're connecting from Power BI or another multitenant service. Internet: Use for test purposes when you want to quickly spin up a managed instance. We don't recommend it for production environments. No access: This option creates a Deny security rule. Modify this rule to make a managed instance accessible through a public endpoint.For more information on public endpoint security, see Using Azure SQL Managed Instance securely with a public endpoint. |

Based on your scenario, select one of the following options:

1. Azure services: We recommend this option when you're connecting from Power BI or another multitenant service.
2. Internet: Use for test purposes when you want to quickly spin up a managed instance. We don't recommend it for production environments.
3. No access: This option creates a Deny security rule. Modify this rule to make a managed instance accessible through a public endpoint.

For more information on public endpoint security, see Using Azure SQL Managed Instance securely with a public endpoint.
Select Review + create to review your choices before you create a managed instance. Or, configure more custom settings by selecting Next: Additional settings.

## Step 4: Additional settings

Fill out optional information on the Additional settings tab. If you omit this information, the portal will apply default settings.

Use the table below as a reference for information required at this tab.

| Setting                                                                   | Suggested value                                                                                                                                                                                            | Description                                                                                                                                              |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Collation                                                                 | Choose the collation that you want to use for your managed instance. If you migrate databases from SQL Server, check the source collation by using SELECT SERVERPROPERTY(N'Collation') and use that value. | For information about collations, see Set or change the server collation.                                                                                |
| Time zone                                                                 | Select the time zone that managed instance will observe.                                                                                                                                                   | For more information, see Time zones.                                                                                                                    |
| Use as failover secondary                                                 | Select Yes.                                                                                                                                                                                                | Enable this option to use the managed instance as a failover group secondary.                                                                            |
| Primary SQL Managed Instance (if Use as failover secondary is set to Yes) | Choose an existing primary managed instance that will be joined in the same DNS zone with the managed instance you're creating.                                                                            | This step will enable post-creation configuration of the failover group. For more information, see Tutorial: Add a managed instance to a failover group. |

## Step 4: Review + create

Select Review + create tab to review your choices before you create a managed instance.
