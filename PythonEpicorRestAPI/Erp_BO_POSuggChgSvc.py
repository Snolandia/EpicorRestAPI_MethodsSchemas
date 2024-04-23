import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.POSuggChgSvc
# Description: Purchase Order Changes
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_POSuggChgs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POSuggChgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POSuggChgs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPOChgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs",headers=creds) as resp:
           return await resp.json()

async def post_POSuggChgs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POSuggChgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SugPOChgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SugPOChgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POSuggChgs_Company_PONum_POLine_PORelNum_VendorChange(Company, PONum, POLine, PORelNum, VendorChange, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POSuggChg item
   Description: Calls GetByID to retrieve the POSuggChg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POSuggChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param VendorChange: Desc: VendorChange   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SugPOChgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + VendorChange + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POSuggChgs_Company_PONum_POLine_PORelNum_VendorChange(Company, PONum, POLine, PORelNum, VendorChange, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POSuggChg for the service
   Description: Calls UpdateExt to update POSuggChg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POSuggChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param VendorChange: Desc: VendorChange   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SugPOChgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + VendorChange + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POSuggChgs_Company_PONum_POLine_PORelNum_VendorChange(Company, PONum, POLine, PORelNum, VendorChange, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POSuggChg item
   Description: Call UpdateExt to delete POSuggChg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POSuggChg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param VendorChange: Desc: VendorChange   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/POSuggChgs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + VendorChange + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SugPOChgListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSugPOChg, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSugPOChg=" + whereClauseSugPOChg
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(poNum, poLine, poRelNum, vendorChange, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
   Required: True
   Required: True
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
   params += "poNum=" + poNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "poLine=" + poLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "poRelNum=" + poRelNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorChange=" + vendorChange

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_MassAcceptSuggestionChanges(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassAcceptSuggestionChanges
   Description: This methods will accept multiple PO Suggestion changes.
   OperationID: MassAcceptSuggestionChanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAcceptSuggestionChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAcceptSuggestionChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AcceptSuggestionChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AcceptSuggestionChange
   Description: This methods will accept the PO Suggestion change.
   OperationID: AcceptSuggestionChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AcceptSuggestionChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AcceptSuggestionChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTracker(epicorHeaders = None):
   """  
   Summary: Invoke method CheckTracker
   Description: This method does stuff .
   OperationID: CheckTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetSugPOChgCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSugPOChgCount
   Description: This methods will return a count of Change PO Suggestions for the selected Buyer
   OperationID: GetSugPOChgCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSugPOChgCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPOChgCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListPlant
   Description: Returns a list of rows that satisfy the where clause. Use in place of GetList
   OperationID: GetListPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsPlantByPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPlantByPart
   Description: Returns a dataset containing all rows that satisfy the where clauses. Whereclauses are split in case to sort by PartNum
   OperationID: GetRowsPlantByPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPlantByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPlantByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsPlant
   Description: Returns a dataset containing all rows that satisfy the where clauses. use in place of GetRows
   OperationID: GetRowsPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSugPOChg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSugPOChg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSugPOChg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSugPOChg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSugPOChg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POSuggChgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SugPOChgListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SugPOChgRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SugPOChgRow] = obj["value"]
      pass

class Erp_Tablesets_SugPOChgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PoDetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.SuggestionCode:str = obj["SuggestionCode"]
      """   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  """  
      self.BuyerID:str = obj["BuyerID"]
      """   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  """  
      self.RequireDate:str = obj["RequireDate"]
      """  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  """  
      self.SourceName:str = obj["SourceName"]
      """  Human formatted string that contains the original source document of this entry.  """  
      self.SurplusQty:int = obj["SurplusQty"]
      """  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  """  
      self.CancelReason:str = obj["CancelReason"]
      """   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this record.  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.VendorChange:bool = obj["VendorChange"]
      """  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Linked Inter-Company sales order.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Linked Inter-Company Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The linked Inter-Company sale order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.brwPartNum:str = obj["brwPartNum"]
      self.Brw_Exception:str = obj["Brw_Exception"]
      self.brwVendorID:str = obj["brwVendorID"]
      self.brwPurPoint:str = obj["brwPurPoint"]
      self.Rels_OnOrderQty:int = obj["Rels_OnOrderQty"]
      self.IUM:str = obj["IUM"]
      self.DueDate:str = obj["DueDate"]
      self.JobSeqType:str = obj["JobSeqType"]
      self.CancelToggle:bool = obj["CancelToggle"]
      self.ExpediteToggle:bool = obj["ExpediteToggle"]
      self.IncreaseToggle:bool = obj["IncreaseToggle"]
      self.PostponeToggle:bool = obj["PostponeToggle"]
      self.ReduceToggle:bool = obj["ReduceToggle"]
      self.VendorName:str = obj["VendorName"]
      self.BrwPartDesc:str = obj["BrwPartDesc"]
      self.ContainerAllowAccept:bool = obj["ContainerAllowAccept"]
      """  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  """  
      self.SupplierQty:int = obj["SupplierQty"]
      self.PUM:str = obj["PUM"]
      self.SurplusQtyUOM:str = obj["SurplusQtyUOM"]
      """  UOM for SurplusQty  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.brwAttributeSetShortDescription:str = obj["brwAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SugPOChgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PoDetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.SuggestionCode:str = obj["SuggestionCode"]
      """   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  """  
      self.BuyerID:str = obj["BuyerID"]
      """   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  """  
      self.RequireDate:str = obj["RequireDate"]
      """  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  """  
      self.SourceName:str = obj["SourceName"]
      """  Human formatted string that contains the original source document of this entry.  """  
      self.SurplusQty:int = obj["SurplusQty"]
      """  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  """  
      self.CancelReason:str = obj["CancelReason"]
      """   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this record.  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.VendorChange:bool = obj["VendorChange"]
      """  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Linked Inter-Company sales order.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Linked Inter-Company Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The linked Inter-Company sale order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.SuggestionStatus:str = obj["SuggestionStatus"]
      """  SuggestionStatus  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Review:bool = obj["Review"]
      """  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  """  
      self.ReqPromiseDate:str = obj["ReqPromiseDate"]
      """  For suggested changes to Promise Date.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created.  """  
      self.LockDate:bool = obj["LockDate"]
      """  LockDate  """  
      self.LockQty:bool = obj["LockQty"]
      """  LockQty  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  PO Release Arrived Qty (note cannot be a linked field as need to set UOM Properties)  """  
      self.Brw_Exception:str = obj["Brw_Exception"]
      self.brwPartNum:str = obj["brwPartNum"]
      self.brwPurPoint:str = obj["brwPurPoint"]
      self.brwVendorID:str = obj["brwVendorID"]
      self.CancelToggle:bool = obj["CancelToggle"]
      self.ContainerAllowAccept:bool = obj["ContainerAllowAccept"]
      """  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  """  
      self.DueDate:str = obj["DueDate"]
      self.ExpediteToggle:bool = obj["ExpediteToggle"]
      self.IncreaseToggle:bool = obj["IncreaseToggle"]
      self.IUM:str = obj["IUM"]
      self.JobSeqType:str = obj["JobSeqType"]
      self.PostponeToggle:bool = obj["PostponeToggle"]
      self.PUM:str = obj["PUM"]
      self.ReduceToggle:bool = obj["ReduceToggle"]
      self.Rels_OnOrderQty:int = obj["Rels_OnOrderQty"]
      self.SupplierQty:int = obj["SupplierQty"]
      self.SurplusQtyUOM:str = obj["SurplusQtyUOM"]
      """  UOM for SurplusQty  """  
      self.VendorName:str = obj["VendorName"]
      self.XRelQty:int = obj["XRelQty"]
      """  PO Release 'Our Quantity'  """  
      self.BrwPartDesc:str = obj["BrwPartDesc"]
      self.PromiseDate:str = obj["PromiseDate"]
      """  The Promise date set on the PO Release  """  
      self.brwAttributeSetID:int = obj["brwAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.brwAttributeSetShortDescription:str = obj["brwAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.brwAttributeSetDescription:str = obj["brwAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.brwAttrClassID:str = obj["brwAttrClassID"]
      """  ID of parent Attribute Class  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.brwPartTrackInventoryByRevision:bool = obj["brwPartTrackInventoryByRevision"]
      self.brwRevisionNum:str = obj["brwRevisionNum"]
      self.PartClassID:str = obj["PartClassID"]
      self.PartClassDescription:str = obj["PartClassDescription"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.PlantName:str = obj["PlantName"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineRevisionNum:str = obj["POLineRevisionNum"]
      self.PORelContractID:str = obj["PORelContractID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AcceptSuggestionChange_input:
   """ Required : 
   ipPONum
   ipPOLine
   ipPORelNum
   ipVendorChange
   ds
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      """  The po number.  """  
      self.ipPOLine:int = obj["ipPOLine"]
      """  The po line number.  """  
      self.ipPORelNum:int = obj["ipPORelNum"]
      """  The po release number.  """  
      self.ipVendorChange:bool = obj["ipVendorChange"]
      """  The Vendir Change.  """  
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      pass

class AcceptSuggestionChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTracker_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.PartTrackerOK:bool = obj["PartTrackerOK"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   poNum
   poLine
   poRelNum
   vendorChange
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      self.vendorChange:bool = obj["vendorChange"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_POSuggChgTableset:
   def __init__(self, obj):
      self.SugPOChg:list[Erp_Tablesets_SugPOChgRow] = obj["SugPOChg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SugPOChgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PoDetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.SuggestionCode:str = obj["SuggestionCode"]
      """   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  """  
      self.BuyerID:str = obj["BuyerID"]
      """   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  """  
      self.RequireDate:str = obj["RequireDate"]
      """  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  """  
      self.SourceName:str = obj["SourceName"]
      """  Human formatted string that contains the original source document of this entry.  """  
      self.SurplusQty:int = obj["SurplusQty"]
      """  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  """  
      self.CancelReason:str = obj["CancelReason"]
      """   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this record.  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.VendorChange:bool = obj["VendorChange"]
      """  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Linked Inter-Company sales order.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Linked Inter-Company Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The linked Inter-Company sale order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.brwPartNum:str = obj["brwPartNum"]
      self.Brw_Exception:str = obj["Brw_Exception"]
      self.brwVendorID:str = obj["brwVendorID"]
      self.brwPurPoint:str = obj["brwPurPoint"]
      self.Rels_OnOrderQty:int = obj["Rels_OnOrderQty"]
      self.IUM:str = obj["IUM"]
      self.DueDate:str = obj["DueDate"]
      self.JobSeqType:str = obj["JobSeqType"]
      self.CancelToggle:bool = obj["CancelToggle"]
      self.ExpediteToggle:bool = obj["ExpediteToggle"]
      self.IncreaseToggle:bool = obj["IncreaseToggle"]
      self.PostponeToggle:bool = obj["PostponeToggle"]
      self.ReduceToggle:bool = obj["ReduceToggle"]
      self.VendorName:str = obj["VendorName"]
      self.BrwPartDesc:str = obj["BrwPartDesc"]
      self.ContainerAllowAccept:bool = obj["ContainerAllowAccept"]
      """  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  """  
      self.SupplierQty:int = obj["SupplierQty"]
      self.PUM:str = obj["PUM"]
      self.SurplusQtyUOM:str = obj["SurplusQtyUOM"]
      """  UOM for SurplusQty  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.brwAttributeSetShortDescription:str = obj["brwAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SugPOChgListTableset:
   def __init__(self, obj):
      self.SugPOChgList:list[Erp_Tablesets_SugPOChgListRow] = obj["SugPOChgList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SugPOChgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PoDetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.SuggestionCode:str = obj["SuggestionCode"]
      """   Suggested action to be taken for this Purchase Order release.
"X" = Expedite, "P" = Postpone,  "C" = Cancel, "I"= increase qty, "R" = Reduce Qty, "S" for below safety and "Z" for below zero. This field is a 8 char. field it could contain "IP" increase and postpone.  """  
      self.BuyerID:str = obj["BuyerID"]
      """   The Buyer Id that is on the related PO.
Duplicate of POHeader.BuyerID  """  
      self.RequireDate:str = obj["RequireDate"]
      """  Requirement Due Date.  For suggested Cancels or Reduce Quantity this is set to Today.  """  
      self.SourceName:str = obj["SourceName"]
      """  Human formatted string that contains the original source document of this entry.  """  
      self.SurplusQty:int = obj["SurplusQty"]
      """  New Suggested qty (in our UOM). This is the true amount suggested, not the difference between actual and suggested.  This only pertains to increase and reduce qty suggestions.  """  
      self.CancelReason:str = obj["CancelReason"]
      """   Reason for "Cancel" suggestion.  Purchase for stock which
1. OverMax - Stock purchase which surpasses the maximum.
2. No Requirement - Job purchase no open job record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field can not be blank.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this record.  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.VendorChange:bool = obj["VendorChange"]
      """  Indicates that this suggestion was initiated from the supplier Wb.  It is a reference field on time phase and does not add or subtract from the balance.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Linked Inter-Company sales order.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Linked Inter-Company Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The linked Inter-Company sale order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.SuggestionStatus:str = obj["SuggestionStatus"]
      """  SuggestionStatus  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Review:bool = obj["Review"]
      """  A flag that is set by the user to indicate the suggestion has been reviewed.  This is only used to help filter suggestions.  """  
      self.ReqPromiseDate:str = obj["ReqPromiseDate"]
      """  For suggested changes to Promise Date.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Date and time when this record was created.  """  
      self.LockDate:bool = obj["LockDate"]
      """  LockDate  """  
      self.LockQty:bool = obj["LockQty"]
      """  LockQty  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  PO Release Arrived Qty (note cannot be a linked field as need to set UOM Properties)  """  
      self.Brw_Exception:str = obj["Brw_Exception"]
      self.brwPartNum:str = obj["brwPartNum"]
      self.brwPurPoint:str = obj["brwPurPoint"]
      self.brwVendorID:str = obj["brwVendorID"]
      self.CancelToggle:bool = obj["CancelToggle"]
      self.ContainerAllowAccept:bool = obj["ContainerAllowAccept"]
      """  Logical indicating whether or not the suggested update is valid for PO releases tied to a Container.  """  
      self.DueDate:str = obj["DueDate"]
      self.ExpediteToggle:bool = obj["ExpediteToggle"]
      self.IncreaseToggle:bool = obj["IncreaseToggle"]
      self.IUM:str = obj["IUM"]
      self.JobSeqType:str = obj["JobSeqType"]
      self.PostponeToggle:bool = obj["PostponeToggle"]
      self.PUM:str = obj["PUM"]
      self.ReduceToggle:bool = obj["ReduceToggle"]
      self.Rels_OnOrderQty:int = obj["Rels_OnOrderQty"]
      self.SupplierQty:int = obj["SupplierQty"]
      self.SurplusQtyUOM:str = obj["SurplusQtyUOM"]
      """  UOM for SurplusQty  """  
      self.VendorName:str = obj["VendorName"]
      self.XRelQty:int = obj["XRelQty"]
      """  PO Release 'Our Quantity'  """  
      self.BrwPartDesc:str = obj["BrwPartDesc"]
      self.PromiseDate:str = obj["PromiseDate"]
      """  The Promise date set on the PO Release  """  
      self.brwAttributeSetID:int = obj["brwAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.brwAttributeSetShortDescription:str = obj["brwAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.brwAttributeSetDescription:str = obj["brwAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.brwAttrClassID:str = obj["brwAttrClassID"]
      """  ID of parent Attribute Class  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.brwPartTrackInventoryByRevision:bool = obj["brwPartTrackInventoryByRevision"]
      self.brwRevisionNum:str = obj["brwRevisionNum"]
      self.PartClassID:str = obj["PartClassID"]
      self.PartClassDescription:str = obj["PartClassDescription"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.PlantName:str = obj["PlantName"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineRevisionNum:str = obj["POLineRevisionNum"]
      self.PORelContractID:str = obj["PORelContractID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPOSuggChgTableset:
   def __init__(self, obj):
      self.SugPOChg:list[Erp_Tablesets_SugPOChgRow] = obj["SugPOChg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   poNum
   poLine
   poRelNum
   vendorChange
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      self.vendorChange:bool = obj["vendorChange"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POSuggChgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POSuggChgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POSuggChgTableset] = obj["returnObj"]
      pass

class GetListPlant_input:
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

class GetListPlant_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SugPOChgListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_SugPOChgListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSugPOChg_input:
   """ Required : 
   ds
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class GetNewSugPOChg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsPlantByPart_input:
   """ Required : 
   whereClauseSugPOChg
   partNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSugPOChg:str = obj["whereClauseSugPOChg"]
      """  whereClause for SugPOChg table  """  
      self.partNum:str = obj["partNum"]
      """  whereClause for partNum  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetRowsPlantByPart_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POSuggChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsPlant_input:
   """ Required : 
   whereClauseSugPOChg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSugPOChg:str = obj["whereClauseSugPOChg"]
      """  whereClause for SugPOChg table  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetRowsPlant_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POSuggChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSugPOChg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSugPOChg:str = obj["whereClauseSugPOChg"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POSuggChgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSugPOChgCount_input:
   """ Required : 
   buyerID
   """  
   def __init__(self, obj):
      self.buyerID:str = obj["buyerID"]
      """  buyerID  """  
      pass

class GetSugPOChgCount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  Count  """  
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

class MassAcceptSuggestionChanges_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      pass

class MassAcceptSuggestionChanges_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOSuggChgTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOSuggChgTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POSuggChgTableset] = obj["ds"]
      pass

      """  output parameters  """  

