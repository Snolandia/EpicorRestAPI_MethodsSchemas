import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.StockProvisionFormatSvc
# Description: BL logic for Stock Provision Format Maintenance
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_StockProvisionFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get StockProvisionFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_StockProvisionFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.StockProvisionFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats",headers=creds) as resp:
           return await resp.json()

async def post_StockProvisionFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_StockProvisionFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.StockProvisionFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.StockProvisionFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_StockProvisionFormats_Company_StockProvFmtCode(Company, StockProvFmtCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the StockProvisionFormat item
   Description: Calls GetByID to retrieve the StockProvisionFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_StockProvisionFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param StockProvFmtCode: Desc: StockProvFmtCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.StockProvisionFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats(" + Company + "," + StockProvFmtCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_StockProvisionFormats_Company_StockProvFmtCode(Company, StockProvFmtCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update StockProvisionFormat for the service
   Description: Calls UpdateExt to update StockProvisionFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_StockProvisionFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param StockProvFmtCode: Desc: StockProvFmtCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.StockProvisionFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats(" + Company + "," + StockProvFmtCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_StockProvisionFormats_Company_StockProvFmtCode(Company, StockProvFmtCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete StockProvisionFormat item
   Description: Call UpdateExt to delete StockProvisionFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_StockProvisionFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param StockProvFmtCode: Desc: StockProvFmtCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/StockProvisionFormats(" + Company + "," + StockProvFmtCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.StockProvisionFormatListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseStockProvisionFormat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseStockProvisionFormat=" + whereClauseStockProvisionFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(stockProvFmtCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "stockProvFmtCode=" + stockProvFmtCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetTranTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetTranTypeList
   Description: This method provides a list of values and description for Tran Types.
   OperationID: GetTranTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeActive
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">The StockProvisionFormat data set</param>
   OperationID: OnChangeActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeType
   Description: This method validates the StockProvisionFormat.Type when changed in UI form.
           ///
   OperationID: OnChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTimeModifierCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTimeModifierCodeDescList
   Description: Purpose: Gets the list of codes/descriptions for Time Modifier combo-box
Parameters: none
   OperationID: GetTimeModifierCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTimeModifierCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTimeModifierCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadTranTypeDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadTranTypeDS
   Description: Seperates delimeted list into individual IDs
   OperationID: LoadTranTypeDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadTranTypeDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadTranTypeDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewStockProvisionFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewStockProvisionFormat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewStockProvisionFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewStockProvisionFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewStockProvisionFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.StockProvisionFormatSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_StockProvisionFormatListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_StockProvisionFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_StockProvisionFormatRow] = obj["value"]
      pass

class Erp_Tablesets_StockProvisionFormatListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StockProvFmtCode:str = obj["StockProvFmtCode"]
      """  The unique identifier for a stock provision format code. (PK)  """  
      self.Description:str = obj["Description"]
      """  Stock Provision report format description  """  
      self.Type:str = obj["Type"]
      """  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  """  
      self.ComparedTo:str = obj["ComparedTo"]
      """  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  """  
      self.TimeModifier:str = obj["TimeModifier"]
      """  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  """  
      self.Bucket1Start:int = obj["Bucket1Start"]
      """  Based on the time modifier, it indicates the starting date of the first bucket  """  
      self.Bucket1End:int = obj["Bucket1End"]
      """  Based on the time modifier, it indicates the ending date of the first bucket  """  
      self.Bucket1Rate:int = obj["Bucket1Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  """  
      self.Bucket1Caption:str = obj["Bucket1Caption"]
      """  Contains the column heading used to describe the first bucket  """  
      self.Bucket2Active:bool = obj["Bucket2Active"]
      """  Flag which indicate if the second bucked will be used  """  
      self.Bucket2End:int = obj["Bucket2End"]
      """  Based on the ?time modifier?, it indicates the ending date of the second bucket  """  
      self.Bucket2Rate:int = obj["Bucket2Rate"]
      """  Based on the time modifier, it indicates the ending date of the second bucket  """  
      self.Bucket2Caption:str = obj["Bucket2Caption"]
      """  Contains the column heading used to describe the second bucket  """  
      self.Bucket3Active:bool = obj["Bucket3Active"]
      """  Flag which indicate if the third bucked will be used  """  
      self.Bucket3End:int = obj["Bucket3End"]
      """  Based on the time modifier, it indicates the ending date of the third bucket  """  
      self.Bucket3Rate:int = obj["Bucket3Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  """  
      self.Bucket3Caption:str = obj["Bucket3Caption"]
      """  Contains the column heading used to describe the third bucket  """  
      self.Bucket4Active:bool = obj["Bucket4Active"]
      """  Flag which indicate if the fourth bucked will be used  """  
      self.Bucket4End:int = obj["Bucket4End"]
      """  Based on the time modifier, it indicates the ending date of the fourth bucket  """  
      self.Bucket4Rate:int = obj["Bucket4Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  """  
      self.Bucket4Caption:str = obj["Bucket4Caption"]
      """  Contains the column heading used to describe the fourth bucket  """  
      self.Bucket5Active:bool = obj["Bucket5Active"]
      """  Flag which indicate if the fifth bucked will be used  """  
      self.Bucket5End:int = obj["Bucket5End"]
      """  Based on the time modifier, it indicates the ending date of the fifth bucket  """  
      self.Bucket5Rate:int = obj["Bucket5Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  """  
      self.Bucket5Caption:str = obj["Bucket5Caption"]
      """  Contains the column heading used to describe the fifth bucket  """  
      self.Bucket6Active:bool = obj["Bucket6Active"]
      """  Flag which indicate if the sixth bucked will be used  """  
      self.Bucket6End:int = obj["Bucket6End"]
      """  Based on the time modifier, it indicates the ending date of the sixth bucket  """  
      self.Bucket6Rate:int = obj["Bucket6Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  """  
      self.Bucket6Caption:str = obj["Bucket6Caption"]
      """  Contains the column heading used to describe the sixth bucket  """  
      self.PartTranTypes:str = obj["PartTranTypes"]
      """  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  """  
      self.GlobalStockProvisionFormat:bool = obj["GlobalStockProvisionFormat"]
      """  Marks this StockProvisionFormat as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableType:bool = obj["EnableType"]
      """  Indicates whether Type field should be enabled in the UI.  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  Type description  """  
      self.ComparedToDesc:str = obj["ComparedToDesc"]
      """  ComparedTo description  """  
      self.TimeModifierDesc:str = obj["TimeModifierDesc"]
      """  TimeModifier description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_StockProvisionFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StockProvFmtCode:str = obj["StockProvFmtCode"]
      """  The unique identifier for a stock provision format code. (PK)  """  
      self.Description:str = obj["Description"]
      """  Stock Provision report format description  """  
      self.Type:str = obj["Type"]
      """  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  """  
      self.ComparedTo:str = obj["ComparedTo"]
      """  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  """  
      self.TimeModifier:str = obj["TimeModifier"]
      """  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  """  
      self.Bucket1Start:int = obj["Bucket1Start"]
      """  Based on the time modifier, it indicates the starting date of the first bucket  """  
      self.Bucket1End:int = obj["Bucket1End"]
      """  Based on the time modifier, it indicates the ending date of the first bucket  """  
      self.Bucket1Rate:int = obj["Bucket1Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  """  
      self.Bucket1Caption:str = obj["Bucket1Caption"]
      """  Contains the column heading used to describe the first bucket  """  
      self.Bucket2Active:bool = obj["Bucket2Active"]
      """  Flag which indicate if the second bucked will be used  """  
      self.Bucket2End:int = obj["Bucket2End"]
      """  Based on the ?time modifier?, it indicates the ending date of the second bucket  """  
      self.Bucket2Rate:int = obj["Bucket2Rate"]
      """  Based on the time modifier, it indicates the ending date of the second bucket  """  
      self.Bucket2Caption:str = obj["Bucket2Caption"]
      """  Contains the column heading used to describe the second bucket  """  
      self.Bucket3Active:bool = obj["Bucket3Active"]
      """  Flag which indicate if the third bucked will be used  """  
      self.Bucket3End:int = obj["Bucket3End"]
      """  Based on the time modifier, it indicates the ending date of the third bucket  """  
      self.Bucket3Rate:int = obj["Bucket3Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  """  
      self.Bucket3Caption:str = obj["Bucket3Caption"]
      """  Contains the column heading used to describe the third bucket  """  
      self.Bucket4Active:bool = obj["Bucket4Active"]
      """  Flag which indicate if the fourth bucked will be used  """  
      self.Bucket4End:int = obj["Bucket4End"]
      """  Based on the time modifier, it indicates the ending date of the fourth bucket  """  
      self.Bucket4Rate:int = obj["Bucket4Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  """  
      self.Bucket4Caption:str = obj["Bucket4Caption"]
      """  Contains the column heading used to describe the fourth bucket  """  
      self.Bucket5Active:bool = obj["Bucket5Active"]
      """  Flag which indicate if the fifth bucked will be used  """  
      self.Bucket5End:int = obj["Bucket5End"]
      """  Based on the time modifier, it indicates the ending date of the fifth bucket  """  
      self.Bucket5Rate:int = obj["Bucket5Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  """  
      self.Bucket5Caption:str = obj["Bucket5Caption"]
      """  Contains the column heading used to describe the fifth bucket  """  
      self.Bucket6Active:bool = obj["Bucket6Active"]
      """  Flag which indicate if the sixth bucked will be used  """  
      self.Bucket6End:int = obj["Bucket6End"]
      """  Based on the time modifier, it indicates the ending date of the sixth bucket  """  
      self.Bucket6Rate:int = obj["Bucket6Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  """  
      self.Bucket6Caption:str = obj["Bucket6Caption"]
      """  Contains the column heading used to describe the sixth bucket  """  
      self.PartTranTypes:str = obj["PartTranTypes"]
      """  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  """  
      self.GlobalStockProvisionFormat:bool = obj["GlobalStockProvisionFormat"]
      """  Marks this StockProvisionFormat as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableType:bool = obj["EnableType"]
      """  Indicates whether Type field should be enabled in the UI.  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  Type description  """  
      self.ComparedToDesc:str = obj["ComparedToDesc"]
      """  ComparedTo description  """  
      self.TimeModifierDesc:str = obj["TimeModifierDesc"]
      """  TimeModifier description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   stockProvFmtCode
   """  
   def __init__(self, obj):
      self.stockProvFmtCode:str = obj["stockProvFmtCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_StockProvisionFormatListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StockProvFmtCode:str = obj["StockProvFmtCode"]
      """  The unique identifier for a stock provision format code. (PK)  """  
      self.Description:str = obj["Description"]
      """  Stock Provision report format description  """  
      self.Type:str = obj["Type"]
      """  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  """  
      self.ComparedTo:str = obj["ComparedTo"]
      """  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  """  
      self.TimeModifier:str = obj["TimeModifier"]
      """  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  """  
      self.Bucket1Start:int = obj["Bucket1Start"]
      """  Based on the time modifier, it indicates the starting date of the first bucket  """  
      self.Bucket1End:int = obj["Bucket1End"]
      """  Based on the time modifier, it indicates the ending date of the first bucket  """  
      self.Bucket1Rate:int = obj["Bucket1Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  """  
      self.Bucket1Caption:str = obj["Bucket1Caption"]
      """  Contains the column heading used to describe the first bucket  """  
      self.Bucket2Active:bool = obj["Bucket2Active"]
      """  Flag which indicate if the second bucked will be used  """  
      self.Bucket2End:int = obj["Bucket2End"]
      """  Based on the ?time modifier?, it indicates the ending date of the second bucket  """  
      self.Bucket2Rate:int = obj["Bucket2Rate"]
      """  Based on the time modifier, it indicates the ending date of the second bucket  """  
      self.Bucket2Caption:str = obj["Bucket2Caption"]
      """  Contains the column heading used to describe the second bucket  """  
      self.Bucket3Active:bool = obj["Bucket3Active"]
      """  Flag which indicate if the third bucked will be used  """  
      self.Bucket3End:int = obj["Bucket3End"]
      """  Based on the time modifier, it indicates the ending date of the third bucket  """  
      self.Bucket3Rate:int = obj["Bucket3Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  """  
      self.Bucket3Caption:str = obj["Bucket3Caption"]
      """  Contains the column heading used to describe the third bucket  """  
      self.Bucket4Active:bool = obj["Bucket4Active"]
      """  Flag which indicate if the fourth bucked will be used  """  
      self.Bucket4End:int = obj["Bucket4End"]
      """  Based on the time modifier, it indicates the ending date of the fourth bucket  """  
      self.Bucket4Rate:int = obj["Bucket4Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  """  
      self.Bucket4Caption:str = obj["Bucket4Caption"]
      """  Contains the column heading used to describe the fourth bucket  """  
      self.Bucket5Active:bool = obj["Bucket5Active"]
      """  Flag which indicate if the fifth bucked will be used  """  
      self.Bucket5End:int = obj["Bucket5End"]
      """  Based on the time modifier, it indicates the ending date of the fifth bucket  """  
      self.Bucket5Rate:int = obj["Bucket5Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  """  
      self.Bucket5Caption:str = obj["Bucket5Caption"]
      """  Contains the column heading used to describe the fifth bucket  """  
      self.Bucket6Active:bool = obj["Bucket6Active"]
      """  Flag which indicate if the sixth bucked will be used  """  
      self.Bucket6End:int = obj["Bucket6End"]
      """  Based on the time modifier, it indicates the ending date of the sixth bucket  """  
      self.Bucket6Rate:int = obj["Bucket6Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  """  
      self.Bucket6Caption:str = obj["Bucket6Caption"]
      """  Contains the column heading used to describe the sixth bucket  """  
      self.PartTranTypes:str = obj["PartTranTypes"]
      """  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  """  
      self.GlobalStockProvisionFormat:bool = obj["GlobalStockProvisionFormat"]
      """  Marks this StockProvisionFormat as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableType:bool = obj["EnableType"]
      """  Indicates whether Type field should be enabled in the UI.  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  Type description  """  
      self.ComparedToDesc:str = obj["ComparedToDesc"]
      """  ComparedTo description  """  
      self.TimeModifierDesc:str = obj["TimeModifierDesc"]
      """  TimeModifier description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_StockProvisionFormatListTableset:
   def __init__(self, obj):
      self.StockProvisionFormatList:list[Erp_Tablesets_StockProvisionFormatListRow] = obj["StockProvisionFormatList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_StockProvisionFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StockProvFmtCode:str = obj["StockProvFmtCode"]
      """  The unique identifier for a stock provision format code. (PK)  """  
      self.Description:str = obj["Description"]
      """  Stock Provision report format description  """  
      self.Type:str = obj["Type"]
      """  Indicates if the format is used on slow moving or excess or aging report. It can be "S" = Slow Moving, "E" = Excess or "A" = Aging  """  
      self.ComparedTo:str = obj["ComparedTo"]
      """  Indicates if an excess report will be compared to consumption, forecast entries or future sales orders. . It can be C= Consumption, F= Forecast, S= Future sales orders  """  
      self.TimeModifier:str = obj["TimeModifier"]
      """  Indicates if the time periods for the buckets are defines in days or months. It can be D= Days, M=Months  """  
      self.Bucket1Start:int = obj["Bucket1Start"]
      """  Based on the time modifier, it indicates the starting date of the first bucket  """  
      self.Bucket1End:int = obj["Bucket1End"]
      """  Based on the time modifier, it indicates the ending date of the first bucket  """  
      self.Bucket1Rate:int = obj["Bucket1Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the first bucket.  """  
      self.Bucket1Caption:str = obj["Bucket1Caption"]
      """  Contains the column heading used to describe the first bucket  """  
      self.Bucket2Active:bool = obj["Bucket2Active"]
      """  Flag which indicate if the second bucked will be used  """  
      self.Bucket2End:int = obj["Bucket2End"]
      """  Based on the ?time modifier?, it indicates the ending date of the second bucket  """  
      self.Bucket2Rate:int = obj["Bucket2Rate"]
      """  Based on the time modifier, it indicates the ending date of the second bucket  """  
      self.Bucket2Caption:str = obj["Bucket2Caption"]
      """  Contains the column heading used to describe the second bucket  """  
      self.Bucket3Active:bool = obj["Bucket3Active"]
      """  Flag which indicate if the third bucked will be used  """  
      self.Bucket3End:int = obj["Bucket3End"]
      """  Based on the time modifier, it indicates the ending date of the third bucket  """  
      self.Bucket3Rate:int = obj["Bucket3Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the third bucket.  """  
      self.Bucket3Caption:str = obj["Bucket3Caption"]
      """  Contains the column heading used to describe the third bucket  """  
      self.Bucket4Active:bool = obj["Bucket4Active"]
      """  Flag which indicate if the fourth bucked will be used  """  
      self.Bucket4End:int = obj["Bucket4End"]
      """  Based on the time modifier, it indicates the ending date of the fourth bucket  """  
      self.Bucket4Rate:int = obj["Bucket4Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fourth bucket.  """  
      self.Bucket4Caption:str = obj["Bucket4Caption"]
      """  Contains the column heading used to describe the fourth bucket  """  
      self.Bucket5Active:bool = obj["Bucket5Active"]
      """  Flag which indicate if the fifth bucked will be used  """  
      self.Bucket5End:int = obj["Bucket5End"]
      """  Based on the time modifier, it indicates the ending date of the fifth bucket  """  
      self.Bucket5Rate:int = obj["Bucket5Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the fifth bucket.  """  
      self.Bucket5Caption:str = obj["Bucket5Caption"]
      """  Contains the column heading used to describe the fifth bucket  """  
      self.Bucket6Active:bool = obj["Bucket6Active"]
      """  Flag which indicate if the sixth bucked will be used  """  
      self.Bucket6End:int = obj["Bucket6End"]
      """  Based on the time modifier, it indicates the ending date of the sixth bucket  """  
      self.Bucket6Rate:int = obj["Bucket6Rate"]
      """  Indicates the rate to calculate the provision for the stock that falls in the sixth bucket.  """  
      self.Bucket6Caption:str = obj["Bucket6Caption"]
      """  Contains the column heading used to describe the sixth bucket  """  
      self.PartTranTypes:str = obj["PartTranTypes"]
      """  Delimited list of PartTran Transaction Types to be used for this Stock Provision Format to calculate last movement date.  """  
      self.GlobalStockProvisionFormat:bool = obj["GlobalStockProvisionFormat"]
      """  Marks this StockProvisionFormat as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableType:bool = obj["EnableType"]
      """  Indicates whether Type field should be enabled in the UI.  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  Type description  """  
      self.ComparedToDesc:str = obj["ComparedToDesc"]
      """  ComparedTo description  """  
      self.TimeModifierDesc:str = obj["TimeModifierDesc"]
      """  TimeModifier description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_StockProvisionFormatTableset:
   def __init__(self, obj):
      self.StockProvisionFormat:list[Erp_Tablesets_StockProvisionFormatRow] = obj["StockProvisionFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TranTypeRow:
   def __init__(self, obj):
      self.TranID:str = obj["TranID"]
      """  Transaction Type ID  """  
      self.Description:str = obj["Description"]
      """  Description of the Transaction Type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranTypeTableset:
   def __init__(self, obj):
      self.TranType:list[Erp_Tablesets_TranTypeRow] = obj["TranType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtStockProvisionFormatTableset:
   def __init__(self, obj):
      self.StockProvisionFormat:list[Erp_Tablesets_StockProvisionFormatRow] = obj["StockProvisionFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   stockProvFmtCode
   """  
   def __init__(self, obj):
      self.stockProvFmtCode:str = obj["stockProvFmtCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_StockProvisionFormatListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewStockProvisionFormat_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

class GetNewStockProvisionFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseStockProvisionFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseStockProvisionFormat:str = obj["whereClauseStockProvisionFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTimeModifierCodeDescList_input:
   """ Required : 
   typeValue
   """  
   def __init__(self, obj):
      self.typeValue:str = obj["typeValue"]
      pass

class GetTimeModifierCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of Time Modifier codes/descriptions  """  
      pass

class GetTranTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.TranTypeAndDesc:str = obj["parameters"]
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

class LoadTranTypeDS_input:
   """ Required : 
   TranTypes
   """  
   def __init__(self, obj):
      self.TranTypes:str = obj["TranTypes"]
      """  Dataset of TranTypes Temp Table  """  
      pass

class LoadTranTypeDS_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TranTypeTableset] = obj["returnObj"]
      pass

class OnChangeActive_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

class OnChangeActive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeType_input:
   """ Required : 
   ipType
   ds
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      """  Proposed Type value  """  
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

class OnChangeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtStockProvisionFormatTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtStockProvisionFormatTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_StockProvisionFormatTableset] = obj["ds"]
      pass

      """  output parameters  """  

