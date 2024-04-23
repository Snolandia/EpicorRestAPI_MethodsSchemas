import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.IntegrationFieldMapSvc
# Description: Integration Field Map.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_IntegrationFieldMaps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IntegrationFieldMaps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IntegrationFieldMaps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IntegrationFieldMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/IntegrationFieldMaps",headers=creds) as resp:
           return await resp.json()

async def post_IntegrationFieldMaps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IntegrationFieldMaps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IntegrationFieldMapRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IntegrationFieldMapRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/IntegrationFieldMaps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IntegrationFieldMaps_Company_IntegrationType_IntegrationID_SystemCode_DataTableID_FieldName(Company, IntegrationType, IntegrationID, SystemCode, DataTableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IntegrationFieldMap item
   Description: Calls GetByID to retrieve the IntegrationFieldMap item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IntegrationFieldMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param IntegrationType: Desc: IntegrationType   Required: True   Allow empty value : True
      :param IntegrationID: Desc: IntegrationID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IntegrationFieldMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/IntegrationFieldMaps(" + Company + "," + IntegrationType + "," + IntegrationID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IntegrationFieldMaps_Company_IntegrationType_IntegrationID_SystemCode_DataTableID_FieldName(Company, IntegrationType, IntegrationID, SystemCode, DataTableID, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IntegrationFieldMap for the service
   Description: Calls UpdateExt to update IntegrationFieldMap. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IntegrationFieldMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param IntegrationType: Desc: IntegrationType   Required: True   Allow empty value : True
      :param IntegrationID: Desc: IntegrationID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IntegrationFieldMapRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/IntegrationFieldMaps(" + Company + "," + IntegrationType + "," + IntegrationID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IntegrationFieldMaps_Company_IntegrationType_IntegrationID_SystemCode_DataTableID_FieldName(Company, IntegrationType, IntegrationID, SystemCode, DataTableID, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IntegrationFieldMap item
   Description: Call UpdateExt to delete IntegrationFieldMap item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IntegrationFieldMap
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param IntegrationType: Desc: IntegrationType   Required: True   Allow empty value : True
      :param IntegrationID: Desc: IntegrationID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/IntegrationFieldMaps(" + Company + "," + IntegrationType + "," + IntegrationID + "," + SystemCode + "," + DataTableID + "," + FieldName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IntegrationFieldMapListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseIntegrationFieldMap, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseIntegrationFieldMap=" + whereClauseIntegrationFieldMap
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(integrationType, integrationID, systemCode, dataTableID, fieldName, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "integrationType=" + integrationType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "integrationID=" + integrationID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "systemCode=" + systemCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "dataTableID=" + dataTableID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fieldName=" + fieldName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListIntegrationMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListIntegrationMap
   Description: Get a list of Integrations for the specified Integration Type.
   OperationID: GetListIntegrationMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListIntegrationMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListIntegrationMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIntegrationMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIntegrationMap
   Description: Get an Integration and related tables for the specified Integration Type and ID.
   OperationID: GetIntegrationMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIntegrationMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIntegrationMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByTable
   Description: Get the Integration Field Map for a specified Integration Type, ID, and Table.
This method will also include tables mapped to related UD tables.
   OperationID: GetByTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListField
   Description: Get a list of unused fields for the specified Integration and Table.
   OperationID: GetListField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnSelectedFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnSelectedFields
   Description: Validate and populate Integration Field map rows.
   OperationID: OnSelectedFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnSelectedFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnSelectedFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIntegrationFieldMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIntegrationFieldMap
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIntegrationFieldMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIntegrationFieldMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIntegrationFieldMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IntegrationFieldMapSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IntegrationFieldMapListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IntegrationFieldMapListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IntegrationFieldMapRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IntegrationFieldMapRow] = obj["value"]
      pass

class Ice_Tablesets_IntegrationFieldMapListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.IntegrationType:str = obj["IntegrationType"]
      """  IntegrationType  """  
      self.IntegrationID:str = obj["IntegrationID"]
      """  IntegrationID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IntegrationFieldMapRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.IntegrationType:str = obj["IntegrationType"]
      """  IntegrationType  """  
      self.IntegrationID:str = obj["IntegrationID"]
      """  IntegrationID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.Boolean01:bool = obj["Boolean01"]
      """  Boolean01  """  
      self.Boolean02:bool = obj["Boolean02"]
      """  Boolean02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisableBoolean01:bool = obj["DisableBoolean01"]
      self.DisableBoolean02:bool = obj["DisableBoolean02"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   integrationType
   integrationID
   systemCode
   dataTableID
   fieldName
   """  
   def __init__(self, obj):
      self.integrationType:str = obj["integrationType"]
      self.integrationID:str = obj["integrationID"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      self.fieldName:str = obj["fieldName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   integrationType
   integrationID
   systemCode
   dataTableID
   fieldName
   """  
   def __init__(self, obj):
      self.integrationType:str = obj["integrationType"]
      self.integrationID:str = obj["integrationID"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["returnObj"]
      pass

class GetByTable_input:
   """ Required : 
   integrationType
   integrationID
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.integrationType:str = obj["integrationType"]
      """  Integration Type, i.e. DF for Data Fabric.  """  
      self.integrationID:str = obj["integrationID"]
      """  Integration ID.  """  
      self.systemCode:str = obj["systemCode"]
      """  System Code.  """  
      self.dataTableID:str = obj["dataTableID"]
      """  Data Table ID.  """  
      pass

class GetByTable_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["returnObj"]
      pass

class GetIntegrationMap_input:
   """ Required : 
   integrationType
   integrationID
   """  
   def __init__(self, obj):
      self.integrationType:str = obj["integrationType"]
      """  Integration Type, i.e. DF for Data Fabric.  """  
      self.integrationID:str = obj["integrationID"]
      """  Integration ID.  """  
      pass

class GetIntegrationMap_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IntegrationMapTableset] = obj["returnObj"]
      pass

class GetListField_input:
   """ Required : 
   integrationType
   integrationID
   systemCode
   dataTableID
   startsWith
   """  
   def __init__(self, obj):
      self.integrationType:str = obj["integrationType"]
      """  Integration Type, i.e. DF for Data Fabric.  """  
      self.integrationID:str = obj["integrationID"]
      """  Integration ID.  """  
      self.systemCode:str = obj["systemCode"]
      """  System Code.  """  
      self.dataTableID:str = obj["dataTableID"]
      """  Data Table ID.  """  
      self.startsWith:str = obj["startsWith"]
      """  Field name starts with.  """  
      pass

class GetListField_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IntegrationFieldTableset] = obj["returnObj"]
      pass

class GetListIntegrationMap_input:
   """ Required : 
   integrationType
   startsWith
   """  
   def __init__(self, obj):
      self.integrationType:str = obj["integrationType"]
      """  Integration Type, i.e. DF for Data Fabric.  """  
      self.startsWith:str = obj["startsWith"]
      """  Starts with.  """  
      pass

class GetListIntegrationMap_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IntegrationMapListTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_IntegrationFieldMapListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewIntegrationFieldMap_input:
   """ Required : 
   ds
   integrationType
   integrationID
   systemCode
   dataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["ds"]
      self.integrationType:str = obj["integrationType"]
      self.integrationID:str = obj["integrationID"]
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      pass

class GetNewIntegrationFieldMap_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseIntegrationFieldMap
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIntegrationFieldMap:str = obj["whereClauseIntegrationFieldMap"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["returnObj"]
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

class Ice_Tablesets_IntegrationFieldMapListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.IntegrationType:str = obj["IntegrationType"]
      """  IntegrationType  """  
      self.IntegrationID:str = obj["IntegrationID"]
      """  IntegrationID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IntegrationFieldMapListTableset:
   def __init__(self, obj):
      self.IntegrationFieldMapList:list[Ice_Tablesets_IntegrationFieldMapListRow] = obj["IntegrationFieldMapList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IntegrationFieldMapRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.IntegrationType:str = obj["IntegrationType"]
      """  IntegrationType  """  
      self.IntegrationID:str = obj["IntegrationID"]
      """  IntegrationID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTableID  """  
      self.FieldName:str = obj["FieldName"]
      """  FieldName  """  
      self.Boolean01:bool = obj["Boolean01"]
      """  Boolean01  """  
      self.Boolean02:bool = obj["Boolean02"]
      """  Boolean02  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisableBoolean01:bool = obj["DisableBoolean01"]
      self.DisableBoolean02:bool = obj["DisableBoolean02"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IntegrationFieldMapTableset:
   def __init__(self, obj):
      self.IntegrationFieldMap:list[Ice_Tablesets_IntegrationFieldMapRow] = obj["IntegrationFieldMap"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IntegrationFieldRow:
   def __init__(self, obj):
      self.FieldName:str = obj["FieldName"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.DataType:str = obj["DataType"]
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IntegrationFieldTableset:
   def __init__(self, obj):
      self.IntegrationField:list[Ice_Tablesets_IntegrationFieldRow] = obj["IntegrationField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IntegrationMapListTableset:
   def __init__(self, obj):
      self.IntegrationMap:list[Ice_Tablesets_IntegrationMapRow] = obj["IntegrationMap"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IntegrationMapRow:
   def __init__(self, obj):
      self.IntegrationID:str = obj["IntegrationID"]
      self.Name:str = obj["Name"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IntegrationMapTableRow:
   def __init__(self, obj):
      self.IntegrationID:str = obj["IntegrationID"]
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IntegrationMapTableset:
   def __init__(self, obj):
      self.IntegrationMap:list[Ice_Tablesets_IntegrationMapRow] = obj["IntegrationMap"]
      self.IntegrationMapTable:list[Ice_Tablesets_IntegrationMapTableRow] = obj["IntegrationMapTable"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtIntegrationFieldMapTableset:
   def __init__(self, obj):
      self.IntegrationFieldMap:list[Ice_Tablesets_IntegrationFieldMapRow] = obj["IntegrationFieldMap"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class OnSelectedFields_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["ds"]
      pass

class OnSelectedFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtIntegrationFieldMapTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtIntegrationFieldMapTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_IntegrationFieldMapTableset] = obj["ds"]
      pass

      """  output parameters  """  

