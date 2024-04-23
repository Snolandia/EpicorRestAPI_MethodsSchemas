import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ECCUDMapSvc
# Description: Service for performing maintenance on ECC UD field mappings
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ECCUDMaps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECCUDMaps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECCUDMaps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCUDMapTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMaps",headers=creds) as resp:
           return await resp.json()

async def post_ECCUDMaps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECCUDMaps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECCUDMapTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECCUDMapTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMaps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECCUDMaps_Company_MapID_MessageType_SchemaName_TableName(Company, MapID, MessageType, SchemaName, TableName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECCUDMap item
   Description: Calls GetByID to retrieve the ECCUDMap item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCUDMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCUDMapTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMaps(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECCUDMaps_Company_MapID_MessageType_SchemaName_TableName(Company, MapID, MessageType, SchemaName, TableName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECCUDMap for the service
   Description: Calls UpdateExt to update ECCUDMap. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECCUDMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECCUDMapTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMaps(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECCUDMaps_Company_MapID_MessageType_SchemaName_TableName(Company, MapID, MessageType, SchemaName, TableName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECCUDMap item
   Description: Call UpdateExt to delete ECCUDMap item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECCUDMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMaps(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECCUDMaps_Company_MapID_MessageType_SchemaName_TableName_ECCUDMapColumns(Company, MapID, MessageType, SchemaName, TableName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECCUDMapColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECCUDMapColumns1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCUDMapColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMaps(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + ")/ECCUDMapColumns",headers=creds) as resp:
           return await resp.json()

async def get_ECCUDMaps_Company_MapID_MessageType_SchemaName_TableName_ECCUDMapColumns_Company_MapID_MessageType_SchemaName_TableName_ColumnName(Company, MapID, MessageType, SchemaName, TableName, ColumnName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECCUDMapColumn item
   Description: Calls GetByID to retrieve the ECCUDMapColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCUDMapColumn1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCUDMapColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMaps(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + ")/ECCUDMapColumns(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECCUDMapColumns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECCUDMapColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECCUDMapColumns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCUDMapColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMapColumns",headers=creds) as resp:
           return await resp.json()

async def post_ECCUDMapColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECCUDMapColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECCUDMapColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECCUDMapColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMapColumns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECCUDMapColumns_Company_MapID_MessageType_SchemaName_TableName_ColumnName(Company, MapID, MessageType, SchemaName, TableName, ColumnName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECCUDMapColumn item
   Description: Calls GetByID to retrieve the ECCUDMapColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECCUDMapColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECCUDMapColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMapColumns(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECCUDMapColumns_Company_MapID_MessageType_SchemaName_TableName_ColumnName(Company, MapID, MessageType, SchemaName, TableName, ColumnName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECCUDMapColumn for the service
   Description: Calls UpdateExt to update ECCUDMapColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECCUDMapColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECCUDMapColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMapColumns(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + "," + ColumnName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECCUDMapColumns_Company_MapID_MessageType_SchemaName_TableName_ColumnName(Company, MapID, MessageType, SchemaName, TableName, ColumnName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECCUDMapColumn item
   Description: Call UpdateExt to delete ECCUDMapColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECCUDMapColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapID: Desc: MapID   Required: True   Allow empty value : True
      :param MessageType: Desc: MessageType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/ECCUDMapColumns(" + Company + "," + MapID + "," + MessageType + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECCUDMapTableListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseECCUDMapTable, whereClauseECCUDMapColumn, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseECCUDMapTable=" + whereClauseECCUDMapTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECCUDMapColumn=" + whereClauseECCUDMapColumn
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(mapID, messageType, schemaName, tableName, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "mapID=" + mapID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "messageType=" + messageType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "schemaName=" + schemaName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tableName=" + tableName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetFullKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFullKeys
   Description: Returns the full key out
   OperationID: GetFullKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFullKey(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFullKey
   Description: Returns the full key
   OperationID: GetFullKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUDMapTableForEntry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUDMapTableForEntry
   Description: Returns tableset for entry form.  This is different than the standard GetByID in that it
will return an addition ColumnInfo list which is avail UD fields that will be combined with
the existing ECCUDMapColumns
   OperationID: GetUDMapTableForEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUDMapTableForEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUDMapTableForEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECCUDMapTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECCUDMapTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECCUDMapTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECCUDMapTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECCUDMapTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECCUDMapColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECCUDMapColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECCUDMapColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECCUDMapColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECCUDMapColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ECCUDMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCUDMapColumnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECCUDMapColumnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCUDMapTableListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECCUDMapTableListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECCUDMapTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECCUDMapTableRow] = obj["value"]
      pass

class Erp_Tablesets_ECCUDMapColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MapID:str = obj["MapID"]
      """  Unique Map ID for message UD field mapping.  """  
      self.MessageType:str = obj["MessageType"]
      """  Specific message used for communicating with web.  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Column Name  """  
      self.ColumnLabel:str = obj["ColumnLabel"]
      """  Column Label  """  
      self.Enabled:bool = obj["Enabled"]
      """  Field is enabled and ready for sending and receiving.  """  
      self.Custom:bool = obj["Custom"]
      """  The field is custom and not a regular UD field.  This field must use a BPM  """  
      self.Attribute:bool = obj["Attribute"]
      """  This field will be included in the Attribute segment  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UseBPM:bool = obj["UseBPM"]
      self.TempExtColumn:bool = obj["TempExtColumn"]
      """  Temporary Extended Column for rows retreived from ICE columns  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECCUDMapTableListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MapID:str = obj["MapID"]
      """  Unique Map ID for message UD field mapping.  """  
      self.MessageType:str = obj["MessageType"]
      """  Specific message used for communicating with web.  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.Enabled:bool = obj["Enabled"]
      """  Message map is enabled and ready for sending and receiving UD field mapping  """  
      self.UseBPM:bool = obj["UseBPM"]
      """  Will use a BPM for all UD mapping instead of what is setup in field mapping.  """  
      self.HasAttribute:bool = obj["HasAttribute"]
      """  This message mapping has attribute segment and the field mapping Attribute is enabled.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECCUDMapTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MapID:str = obj["MapID"]
      """  Unique Map ID for message UD field mapping.  """  
      self.MessageType:str = obj["MessageType"]
      """  Specific message used for communicating with web.  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.Enabled:bool = obj["Enabled"]
      """  Message map is enabled and ready for sending and receiving UD field mapping  """  
      self.UseBPM:bool = obj["UseBPM"]
      """  Will use a BPM for all UD mapping instead of what is setup in field mapping.  """  
      self.HasAttribute:bool = obj["HasAttribute"]
      """  This message mapping has attribute segment and the field mapping Attribute is enabled.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  System Flag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
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
class DeleteByID_input:
   """ Required : 
   mapID
   messageType
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.mapID:str = obj["mapID"]
      self.messageType:str = obj["messageType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ECCUDMapColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MapID:str = obj["MapID"]
      """  Unique Map ID for message UD field mapping.  """  
      self.MessageType:str = obj["MessageType"]
      """  Specific message used for communicating with web.  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Column Name  """  
      self.ColumnLabel:str = obj["ColumnLabel"]
      """  Column Label  """  
      self.Enabled:bool = obj["Enabled"]
      """  Field is enabled and ready for sending and receiving.  """  
      self.Custom:bool = obj["Custom"]
      """  The field is custom and not a regular UD field.  This field must use a BPM  """  
      self.Attribute:bool = obj["Attribute"]
      """  This field will be included in the Attribute segment  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UseBPM:bool = obj["UseBPM"]
      self.TempExtColumn:bool = obj["TempExtColumn"]
      """  Temporary Extended Column for rows retreived from ICE columns  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECCUDMapTableListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MapID:str = obj["MapID"]
      """  Unique Map ID for message UD field mapping.  """  
      self.MessageType:str = obj["MessageType"]
      """  Specific message used for communicating with web.  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.Enabled:bool = obj["Enabled"]
      """  Message map is enabled and ready for sending and receiving UD field mapping  """  
      self.UseBPM:bool = obj["UseBPM"]
      """  Will use a BPM for all UD mapping instead of what is setup in field mapping.  """  
      self.HasAttribute:bool = obj["HasAttribute"]
      """  This message mapping has attribute segment and the field mapping Attribute is enabled.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECCUDMapTableListTableset:
   def __init__(self, obj):
      self.ECCUDMapTableList:list[Erp_Tablesets_ECCUDMapTableListRow] = obj["ECCUDMapTableList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ECCUDMapTableRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.MapID:str = obj["MapID"]
      """  Unique Map ID for message UD field mapping.  """  
      self.MessageType:str = obj["MessageType"]
      """  Specific message used for communicating with web.  """  
      self.SchemaName:str = obj["SchemaName"]
      """  Schema Name  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.Enabled:bool = obj["Enabled"]
      """  Message map is enabled and ready for sending and receiving UD field mapping  """  
      self.UseBPM:bool = obj["UseBPM"]
      """  Will use a BPM for all UD mapping instead of what is setup in field mapping.  """  
      self.HasAttribute:bool = obj["HasAttribute"]
      """  This message mapping has attribute segment and the field mapping Attribute is enabled.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  System Flag  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECCUDMappingTableset:
   def __init__(self, obj):
      self.ECCUDMapTable:list[Erp_Tablesets_ECCUDMapTableRow] = obj["ECCUDMapTable"]
      self.ECCUDMapColumn:list[Erp_Tablesets_ECCUDMapColumnRow] = obj["ECCUDMapColumn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtECCUDMappingTableset:
   def __init__(self, obj):
      self.ECCUDMapTable:list[Erp_Tablesets_ECCUDMapTableRow] = obj["ECCUDMapTable"]
      self.ECCUDMapColumn:list[Erp_Tablesets_ECCUDMapColumnRow] = obj["ECCUDMapColumn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   mapID
   messageType
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.mapID:str = obj["mapID"]
      self.messageType:str = obj["messageType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECCUDMappingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECCUDMappingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECCUDMappingTableset] = obj["returnObj"]
      pass

class GetFullKey_input:
   """ Required : 
   mapID
   """  
   def __init__(self, obj):
      self.mapID:str = obj["mapID"]
      pass

class GetFullKey_output:
   def __init__(self, obj):
      self.returnObj:object
      pass

class GetFullKeys_input:
   """ Required : 
   mapID
   """  
   def __init__(self, obj):
      self.mapID:str = obj["mapID"]
      pass

class GetFullKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.returnedMapId:str = obj["parameters"]
      self.messageType:str = obj["parameters"]
      self.schemaName:str = obj["parameters"]
      self.tableName:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_ECCUDMapTableListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewECCUDMapColumn_input:
   """ Required : 
   ds
   mapID
   messageType
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECCUDMappingTableset] = obj["ds"]
      self.mapID:str = obj["mapID"]
      self.messageType:str = obj["messageType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class GetNewECCUDMapColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECCUDMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECCUDMapTable_input:
   """ Required : 
   ds
   mapID
   messageType
   schemaName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECCUDMappingTableset] = obj["ds"]
      self.mapID:str = obj["mapID"]
      self.messageType:str = obj["messageType"]
      self.schemaName:str = obj["schemaName"]
      pass

class GetNewECCUDMapTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECCUDMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseECCUDMapTable
   whereClauseECCUDMapColumn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseECCUDMapTable:str = obj["whereClauseECCUDMapTable"]
      self.whereClauseECCUDMapColumn:str = obj["whereClauseECCUDMapColumn"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECCUDMappingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetUDMapTableForEntry_input:
   """ Required : 
   mapID
   """  
   def __init__(self, obj):
      self.mapID:str = obj["mapID"]
      pass

class GetUDMapTableForEntry_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ECCUDMappingTableset] = obj["returnObj"]
      pass

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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtECCUDMappingTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtECCUDMappingTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ECCUDMappingTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ECCUDMappingTableset] = obj["ds"]
      pass

      """  output parameters  """  

