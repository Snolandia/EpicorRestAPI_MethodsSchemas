import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConfiguratorAssembliesSvc
# Description: Configurator Assemblies
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorAssemblies(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConfiguratorAssemblies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfiguratorAssemblies
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcAssemblyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/ConfiguratorAssemblies",headers=creds) as resp:
           return await resp.json()

async def post_ConfiguratorAssemblies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfiguratorAssemblies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcAssemblyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcAssemblyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/ConfiguratorAssemblies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorAssemblies_Company_ConfigID_AssemblyName(Company, ConfigID, AssemblyName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConfiguratorAssembly item
   Description: Calls GetByID to retrieve the ConfiguratorAssembly item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfiguratorAssembly
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcAssemblyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/ConfiguratorAssemblies(" + Company + "," + ConfigID + "," + AssemblyName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConfiguratorAssemblies_Company_ConfigID_AssemblyName(Company, ConfigID, AssemblyName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConfiguratorAssembly for the service
   Description: Calls UpdateExt to update ConfiguratorAssembly. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfiguratorAssembly
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcAssemblyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/ConfiguratorAssemblies(" + Company + "," + ConfigID + "," + AssemblyName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConfiguratorAssemblies_Company_ConfigID_AssemblyName(Company, ConfigID, AssemblyName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConfiguratorAssembly item
   Description: Call UpdateExt to delete ConfiguratorAssembly item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfiguratorAssembly
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/ConfiguratorAssemblies(" + Company + "," + ConfigID + "," + AssemblyName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorAssemblies_Company_ConfigID_AssemblyName_PcAssemblyUsings(Company, ConfigID, AssemblyName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcAssemblyUsings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcAssemblyUsings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcAssemblyUsingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/ConfiguratorAssemblies(" + Company + "," + ConfigID + "," + AssemblyName + ")/PcAssemblyUsings",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorAssemblies_Company_ConfigID_AssemblyName_PcAssemblyUsings_Company_ConfigID_AssemblyName_UsingSeq(Company, ConfigID, AssemblyName, UsingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcAssemblyUsing item
   Description: Calls GetByID to retrieve the PcAssemblyUsing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcAssemblyUsing1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param UsingSeq: Desc: UsingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcAssemblyUsingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/ConfiguratorAssemblies(" + Company + "," + ConfigID + "," + AssemblyName + ")/PcAssemblyUsings(" + Company + "," + ConfigID + "," + AssemblyName + "," + UsingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcAssemblyUsings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcAssemblyUsings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcAssemblyUsings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcAssemblyUsingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/PcAssemblyUsings",headers=creds) as resp:
           return await resp.json()

async def post_PcAssemblyUsings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcAssemblyUsings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcAssemblyUsingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcAssemblyUsingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/PcAssemblyUsings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcAssemblyUsings_Company_ConfigID_AssemblyName_UsingSeq(Company, ConfigID, AssemblyName, UsingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcAssemblyUsing item
   Description: Calls GetByID to retrieve the PcAssemblyUsing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcAssemblyUsing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param UsingSeq: Desc: UsingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcAssemblyUsingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/PcAssemblyUsings(" + Company + "," + ConfigID + "," + AssemblyName + "," + UsingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcAssemblyUsings_Company_ConfigID_AssemblyName_UsingSeq(Company, ConfigID, AssemblyName, UsingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcAssemblyUsing for the service
   Description: Calls UpdateExt to update PcAssemblyUsing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcAssemblyUsing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param UsingSeq: Desc: UsingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcAssemblyUsingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/PcAssemblyUsings(" + Company + "," + ConfigID + "," + AssemblyName + "," + UsingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcAssemblyUsings_Company_ConfigID_AssemblyName_UsingSeq(Company, ConfigID, AssemblyName, UsingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcAssemblyUsing item
   Description: Call UpdateExt to delete PcAssemblyUsing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcAssemblyUsing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param AssemblyName: Desc: AssemblyName   Required: True   Allow empty value : True
      :param UsingSeq: Desc: UsingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/PcAssemblyUsings(" + Company + "," + ConfigID + "," + AssemblyName + "," + UsingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcAssemblyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcAssembly, whereClausePcAssemblyUsing, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcAssembly=" + whereClausePcAssembly
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcAssemblyUsing=" + whereClausePcAssemblyUsing
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(configID, assemblyName, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "configID=" + configID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "assemblyName=" + assemblyName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckForDuplicateAssemblies(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDuplicateAssemblies
   Description: Called to determine if the assembly name has already been added to this configuration
   OperationID: CheckForDuplicateAssemblies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDuplicateAssemblies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDuplicateAssemblies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckValidConfigID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckValidConfigID
   Description: Called to validate the user entered configuration
   OperationID: CheckValidConfigID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckValidConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForDuplicateUsingClauses(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDuplicateUsingClauses
   Description: Called to determine if the using clause already exists
   OperationID: CheckForDuplicateUsingClauses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDuplicateUsingClauses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDuplicateUsingClauses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUsingClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUsingClause
   Description: Verify the user entered Using Clause is valid for the given assembly.
   OperationID: ValidateUsingClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUsingClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUsingClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsAliasUnique(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsAliasUnique
   Description: Verify the user entered alias has not already been used for this configuration and assembly
   OperationID: IsAliasUnique
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsAliasUnique_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAliasUnique_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAndCheckForDuplicateAssemblies(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAndCheckForDuplicateAssemblies
   Description: Verify the user entered assembly is valid and also if it is not duplicated.
   OperationID: ValidateAndCheckForDuplicateAssemblies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAndCheckForDuplicateAssemblies_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAndCheckForDuplicateAssemblies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAssembly
   Description: Verify the user entered assembly is valid
   OperationID: ValidateAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAssemblyList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAssemblyList
   Description: Retrieve the list of assemblies that can be referenced
   OperationID: GetAssemblyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAssemblyList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAssemblyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAFSForSearch(epicorHeaders = None):
   """  
   Summary: Invoke method GetAFSForSearch
   Description: returns the valid directories to search in a deliminted string
   OperationID: GetAFSForSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAFSForSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AddMultipleReferences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddMultipleReferences
   Description: This method creates multiple references when the user did a search/selecct.
   OperationID: AddMultipleReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddMultipleReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMultipleReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshUsingClauses(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshUsingClauses
   Description: This method deletes all existing PcAssemblyUsing rows for a configurator and rebuilds them.
   OperationID: RefreshUsingClauses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshUsingClauses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshUsingClauses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcAssembly
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcAssemblyUsing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcAssemblyUsing
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcAssemblyUsing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcAssemblyUsing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcAssemblyUsing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorAssembliesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcAssemblyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcAssemblyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcAssemblyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcAssemblyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcAssemblyUsingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcAssemblyUsingRow] = obj["value"]
      pass

class Erp_Tablesets_PcAssemblyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAssemblyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.Path:str = obj["Path"]
      """  Path  """  
      self.IncludeIn:int = obj["IncludeIn"]
      """  IncludeIn  """  
      self.ExternalAssembly:bool = obj["ExternalAssembly"]
      """  ExternalAssembly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CreateUsingClauses:bool = obj["CreateUsingClauses"]
      """  Used to determine if the using clauses are to be automatically created when a a new assembly is specified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PcStatusApproved:bool = obj["PcStatusApproved"]
      self.PcStatusDescription:str = obj["PcStatusDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAssemblyUsingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.UsingSeq:int = obj["UsingSeq"]
      """  UsingSeq  """  
      self.UsingClause:str = obj["UsingClause"]
      """  UsingClause  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddMultipleReferences_input:
   """ Required : 
   configID
   ipCreateUsingClauses
   ds
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID the references are tied to  """  
      self.ipCreateUsingClauses:bool = obj["ipCreateUsingClauses"]
      """  if true, the using clauses will be created  """  
      self.ds:list[Erp_Tablesets_PcAssemblySelectionTableset] = obj["ds"]
      pass

class AddMultipleReferences_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcAssemblySelectionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckForDuplicateAssemblies_input:
   """ Required : 
   configID
   ipAssemblyName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration the assembly is being made available  """  
      self.ipAssemblyName:str = obj["ipAssemblyName"]
      """  The assembly name include the .dll  """  
      pass

class CheckForDuplicateAssemblies_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipAssemblyName:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckForDuplicateUsingClauses_input:
   """ Required : 
   configID
   assemblyName
   ipUsingClause
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.assemblyName:str = obj["assemblyName"]
      """  Assembly name including .dll  """  
      self.ipUsingClause:str = obj["ipUsingClause"]
      """  the using statement to validate  """  
      pass

class CheckForDuplicateUsingClauses_output:
   def __init__(self, obj):
      pass

class CheckValidConfigID_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  configuration ID to validate  """  
      pass

class CheckValidConfigID_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   configID
   assemblyName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.assemblyName:str = obj["assemblyName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ConfiguratorAssembliesTableset:
   def __init__(self, obj):
      self.PcAssembly:list[Erp_Tablesets_PcAssemblyRow] = obj["PcAssembly"]
      self.PcAssemblyUsing:list[Erp_Tablesets_PcAssemblyUsingRow] = obj["PcAssemblyUsing"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCAssemblySelectionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssemblyLocation:str = obj["AssemblyLocation"]
      self.Assembly:str = obj["Assembly"]
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAssemblyDirsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AvailDirectories:str = obj["AvailDirectories"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAssemblyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAssemblyListTableset:
   def __init__(self, obj):
      self.PcAssemblyList:list[Erp_Tablesets_PcAssemblyListRow] = obj["PcAssemblyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcAssemblyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.Path:str = obj["Path"]
      """  Path  """  
      self.IncludeIn:int = obj["IncludeIn"]
      """  IncludeIn  """  
      self.ExternalAssembly:bool = obj["ExternalAssembly"]
      """  ExternalAssembly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CreateUsingClauses:bool = obj["CreateUsingClauses"]
      """  Used to determine if the using clauses are to be automatically created when a a new assembly is specified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PcStatusApproved:bool = obj["PcStatusApproved"]
      self.PcStatusDescription:str = obj["PcStatusDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAssemblySelectionTableset:
   def __init__(self, obj):
      self.PcAssemblyDirs:list[Erp_Tablesets_PcAssemblyDirsRow] = obj["PcAssemblyDirs"]
      self.PCAssemblySelection:list[Erp_Tablesets_PCAssemblySelectionRow] = obj["PCAssemblySelection"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcAssemblyUsingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.AssemblyName:str = obj["AssemblyName"]
      """  AssemblyName  """  
      self.UsingSeq:int = obj["UsingSeq"]
      """  UsingSeq  """  
      self.UsingClause:str = obj["UsingClause"]
      """  UsingClause  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtConfiguratorAssembliesTableset:
   def __init__(self, obj):
      self.PcAssembly:list[Erp_Tablesets_PcAssemblyRow] = obj["PcAssembly"]
      self.PcAssemblyUsing:list[Erp_Tablesets_PcAssemblyUsingRow] = obj["PcAssemblyUsing"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAFSForSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcAssemblySelectionTableset] = obj["returnObj"]
      pass

class GetAssemblyList_input:
   """ Required : 
   assemblyDirectory
   assemblyFilter
   configID
   """  
   def __init__(self, obj):
      self.assemblyDirectory:str = obj["assemblyDirectory"]
      """  Directory to search, must be part of the AssemblyFileSystem found in the web.config  """  
      self.assemblyFilter:str = obj["assemblyFilter"]
      """  filter to apply - optional  """  
      self.configID:str = obj["configID"]
      """  Configuration ID that is currently being processed.  Used to exclude already assigned assemblies.  """  
      pass

class GetAssemblyList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcAssemblySelectionTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   configID
   assemblyName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.assemblyName:str = obj["assemblyName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcAssemblyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPcAssemblyUsing_input:
   """ Required : 
   ds
   configID
   assemblyName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.assemblyName:str = obj["assemblyName"]
      pass

class GetNewPcAssemblyUsing_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcAssembly_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePcAssembly
   whereClausePcAssemblyUsing
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcAssembly:str = obj["whereClausePcAssembly"]
      self.whereClausePcAssemblyUsing:str = obj["whereClausePcAssemblyUsing"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class IsAliasUnique_input:
   """ Required : 
   configID
   assemblyName
   ipAlias
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.assemblyName:str = obj["assemblyName"]
      """  Assembly Name  """  
      self.ipAlias:str = obj["ipAlias"]
      """  user entered alias  """  
      pass

class IsAliasUnique_output:
   def __init__(self, obj):
      pass

class RefreshUsingClauses_input:
   """ Required : 
   configID
   ds
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      pass

class RefreshUsingClauses_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorAssembliesTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorAssembliesTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorAssembliesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAndCheckForDuplicateAssemblies_input:
   """ Required : 
   configID
   assemblyName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.assemblyName:str = obj["assemblyName"]
      """  Assembly Name to check  """  
      pass

class ValidateAndCheckForDuplicateAssemblies_output:
   def __init__(self, obj):
      pass

class ValidateAssembly_input:
   """ Required : 
   assemblyName
   """  
   def __init__(self, obj):
      self.assemblyName:str = obj["assemblyName"]
      """  Assembly Name to check  """  
      pass

class ValidateAssembly_output:
   def __init__(self, obj):
      pass

class ValidateUsingClause_input:
   """ Required : 
   configID
   assemblyName
   ipUsingClause
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  ConfigurationID  """  
      self.assemblyName:str = obj["assemblyName"]
      """  Assembly Name  """  
      self.ipUsingClause:str = obj["ipUsingClause"]
      """  Using Clause to validate  """  
      pass

class ValidateUsingClause_output:
   def __init__(self, obj):
      pass

