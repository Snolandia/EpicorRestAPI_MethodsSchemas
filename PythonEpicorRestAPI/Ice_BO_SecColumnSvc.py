import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SecColumnSvc
# Description: Column security
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SecColumns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SecColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SecColumns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SecColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/SecColumns",headers=creds) as resp:
           return await resp.json()

async def post_SecColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SecColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SecColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SecColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/SecColumns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SecColumns_Company_DatasourceType_SchemaName_TableName_ColumnName(Company, DatasourceType, SchemaName, TableName, ColumnName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SecColumn item
   Description: Calls GetByID to retrieve the SecColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SecColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SecColumnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/SecColumns(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SecColumns_Company_DatasourceType_SchemaName_TableName_ColumnName(Company, DatasourceType, SchemaName, TableName, ColumnName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SecColumn for the service
   Description: Calls UpdateExt to update SecColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SecColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
      :param SchemaName: Desc: SchemaName   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param ColumnName: Desc: ColumnName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SecColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/SecColumns(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + "," + ColumnName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SecColumns_Company_DatasourceType_SchemaName_TableName_ColumnName(Company, DatasourceType, SchemaName, TableName, ColumnName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SecColumn item
   Description: Call UpdateExt to delete SecColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SecColumn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DatasourceType: Desc: DatasourceType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/SecColumns(" + Company + "," + DatasourceType + "," + SchemaName + "," + TableName + "," + ColumnName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SecColumnListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSecColumn, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSecColumn=" + whereClauseSecColumn
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, datasourceType, schemaName, tableName, columnName, epicorHeaders = None):
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
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "datasourceType=" + datasourceType
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "columnName=" + columnName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GlobalRecordFound(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GlobalRecordFound
   Description: Determines if a matching record exists for all companies in tenant or database
   OperationID: GlobalRecordFound
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GlobalRecordFound_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlobalRecordFound_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetSecColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetSecColumn
   Description: Reset security column to defaults.
   OperationID: ResetSecColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetSecColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetSecColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NewSecColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NewSecColumn
   Description: Wrapper for Get New
   OperationID: NewSecColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NewSecColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NewSecColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddFieldInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddFieldInfo
   OperationID: AddFieldInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddFieldInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddFieldInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FieldChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FieldChanged
   OperationID: FieldChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FieldChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDefaultUserAcces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDefaultUserAcces
   OperationID: SetDefaultUserAcces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDefaultUserAcces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDefaultUserAcces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUserRows(epicorHeaders = None):
   """  
   Summary: Invoke method AddUserRows
   OperationID: AddUserRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SetMaskPreview(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetMaskPreview
   Description: update mask preview
   OperationID: SetMaskPreview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetMaskPreview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetMaskPreview_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMask
   Description: validate is mask is valid
   OperationID: ValidateMask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetMask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetMask
   Description: Reset Mask
   OperationID: ResetMask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSecColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSecColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSecColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSecColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSecColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SecColumnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecColumnListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SecColumnListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SecColumnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SecColumnRow] = obj["value"]
      pass

class Ice_Tablesets_SecColumnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  Name of the database table that this row refers to. This field can't be blank.  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Name of the database column that this row refers to. This field can't be blank.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  Name of the database table that this row refers to. This field can't be blank.  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Name of the database column that this row refers to. This field can't be blank.  """  
      self.WriteAllowList:str = obj["WriteAllowList"]
      """  List of users and security groups which are allowed write access.  """  
      self.WriteDenyList:str = obj["WriteDenyList"]
      """  List of users and security groups which are denied write access.  """  
      self.ReadAllowList:str = obj["ReadAllowList"]
      """  List of users and security groups which are allowed read access.  """  
      self.ReadDenyList:str = obj["ReadDenyList"]
      """  List of users and security groups which are denied read access.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Mask:str = obj["Mask"]
      """  Mask  """  
      self.UnmaskedAllowList:str = obj["UnmaskedAllowList"]
      """  UnmaskedAllowList  """  
      self.UnmaskedDenyList:str = obj["UnmaskedDenyList"]
      """  UnmaskedDenyList  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.Access:str = obj["Access"]
      self.CalcWidth:int = obj["CalcWidth"]
      self.DataType:str = obj["DataType"]
      self.Format:str = obj["Format"]
      self.MaskChar:str = obj["MaskChar"]
      self.MaskingSupported:bool = obj["MaskingSupported"]
      self.MaskPreview:str = obj["MaskPreview"]
      self.MaskSampleSource:str = obj["MaskSampleSource"]
      self.PadLeft:int = obj["PadLeft"]
      self.PadRight:int = obj["PadRight"]
      self.Width:int = obj["Width"]
      self.Repeated:int = obj["Repeated"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.Description:str = obj["Description"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddFieldInfo_input:
   """ Required : 
   ds
   dsSsecurityList
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      self.dsSsecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSsecurityList"]
      pass

class AddFieldInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      self.dsSsecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSsecurityList"]
      pass

      """  output parameters  """  

class AddUserRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecurityAccessTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   company
   datasourceType
   schemaName
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.datasourceType:str = obj["datasourceType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class FieldChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

class FieldChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   company
   datasourceType
   schemaName
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.datasourceType:str = obj["datasourceType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecColumnTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SecColumnTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SecColumnTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SecColumnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSecColumn_input:
   """ Required : 
   ds
   company
   datasourceType
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.datasourceType:str = obj["datasourceType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class GetNewSecColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSecColumn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSecColumn:str = obj["whereClauseSecColumn"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SecColumnTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GlobalRecordFound_input:
   """ Required : 
   dataSourceType
   schemaName
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.dataSourceType:str = obj["dataSourceType"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class GlobalRecordFound_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.company:str = obj["parameters"]
      self.CompanyVisibility:int = obj["parameters"]
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

class Ice_Tablesets_GroupAccessRow:
   def __init__(self, obj):
      self.Access:str = obj["Access"]
      self.SecGroupCode:str = obj["SecGroupCode"]
      self.SecGroupDesc:str = obj["SecGroupDesc"]
      self.Select:bool = obj["Select"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecColumnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  Name of the database table that this row refers to. This field can't be blank.  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Name of the database column that this row refers to. This field can't be blank.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecColumnListTableset:
   def __init__(self, obj):
      self.SecColumnList:list[Ice_Tablesets_SecColumnListRow] = obj["SecColumnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SecColumnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DatasourceType:str = obj["DatasourceType"]
      """  DatasourceType  """  
      self.SchemaName:str = obj["SchemaName"]
      """  SchemaName  """  
      self.TableName:str = obj["TableName"]
      """  Name of the database table that this row refers to. This field can't be blank.  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Name of the database column that this row refers to. This field can't be blank.  """  
      self.WriteAllowList:str = obj["WriteAllowList"]
      """  List of users and security groups which are allowed write access.  """  
      self.WriteDenyList:str = obj["WriteDenyList"]
      """  List of users and security groups which are denied write access.  """  
      self.ReadAllowList:str = obj["ReadAllowList"]
      """  List of users and security groups which are allowed read access.  """  
      self.ReadDenyList:str = obj["ReadDenyList"]
      """  List of users and security groups which are denied read access.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Mask:str = obj["Mask"]
      """  Mask  """  
      self.UnmaskedAllowList:str = obj["UnmaskedAllowList"]
      """  UnmaskedAllowList  """  
      self.UnmaskedDenyList:str = obj["UnmaskedDenyList"]
      """  UnmaskedDenyList  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.Access:str = obj["Access"]
      self.CalcWidth:int = obj["CalcWidth"]
      self.DataType:str = obj["DataType"]
      self.Format:str = obj["Format"]
      self.MaskChar:str = obj["MaskChar"]
      self.MaskingSupported:bool = obj["MaskingSupported"]
      self.MaskPreview:str = obj["MaskPreview"]
      self.MaskSampleSource:str = obj["MaskSampleSource"]
      self.PadLeft:int = obj["PadLeft"]
      self.PadRight:int = obj["PadRight"]
      self.Width:int = obj["Width"]
      self.Repeated:int = obj["Repeated"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.Description:str = obj["Description"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SecColumnTableset:
   def __init__(self, obj):
      self.SecColumn:list[Ice_Tablesets_SecColumnRow] = obj["SecColumn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SecurityAccessTableset:
   def __init__(self, obj):
      self.GroupAccess:list[Ice_Tablesets_GroupAccessRow] = obj["GroupAccess"]
      self.UserAccess:list[Ice_Tablesets_UserAccessRow] = obj["UserAccess"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtSecColumnTableset:
   def __init__(self, obj):
      self.SecColumn:list[Ice_Tablesets_SecColumnRow] = obj["SecColumn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UserAccessRow:
   def __init__(self, obj):
      self.Access:str = obj["Access"]
      self.Name:str = obj["Name"]
      self.SecurityMgr:bool = obj["SecurityMgr"]
      self.UserID:str = obj["UserID"]
      self.Select:bool = obj["Select"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class NewSecColumn_input:
   """ Required : 
   ds
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      pass

class NewSecColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   dsSsecurityList
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      self.dsSsecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSsecurityList"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      self.dsSsecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSsecurityList"]
      pass

      """  output parameters  """  

class ResetMask_input:
   """ Required : 
   ds
   previousAccess
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      self.previousAccess:str = obj["previousAccess"]
      pass

class ResetMask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ResetSecColumn_input:
   """ Required : 
   schemaName
   tableName
   columnName
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      self.columnName:str = obj["columnName"]
      pass

class ResetSecColumn_output:
   def __init__(self, obj):
      pass

class SetDefaultUserAcces_input:
   """ Required : 
   dsSsecurityList
   """  
   def __init__(self, obj):
      self.dsSsecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSsecurityList"]
      pass

class SetDefaultUserAcces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSsecurityList:list[Ice_Tablesets_SecurityAccessTableset] = obj["dsSsecurityList"]
      pass

      """  output parameters  """  

class SetMaskPreview_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

class SetMaskPreview_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSecColumnTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSecColumnTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SecColumnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateMask_input:
   """ Required : 
   rightPadding
   leftPadding
   repeatedBy
   maskedChar
   fieldLength
   """  
   def __init__(self, obj):
      self.rightPadding:int = obj["rightPadding"]
      self.leftPadding:int = obj["leftPadding"]
      self.repeatedBy:int = obj["repeatedBy"]
      self.maskedChar:str = obj["maskedChar"]
      self.fieldLength:int = obj["fieldLength"]
      pass

class ValidateMask_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.validationError:str = obj["parameters"]
      pass

      """  output parameters  """  

