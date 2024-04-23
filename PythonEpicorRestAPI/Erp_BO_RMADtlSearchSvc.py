import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RMADtlSearchSvc
# Description: Search for RMADtl records
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RMADtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RMADtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RMADtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_RMADtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RMADtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RMADtlSearches_Company_RMANum_RMALine(Company, RMANum, RMALine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RMADtlSearch item
   Description: Calls GetByID to retrieve the RMADtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RMADtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches(" + Company + "," + RMANum + "," + RMALine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RMADtlSearches_Company_RMANum_RMALine(Company, RMANum, RMALine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RMADtlSearch for the service
   Description: Calls UpdateExt to update RMADtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RMADtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RMADtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches(" + Company + "," + RMANum + "," + RMALine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RMADtlSearches_Company_RMANum_RMALine(Company, RMANum, RMALine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RMADtlSearch item
   Description: Call UpdateExt to delete RMADtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RMADtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RMANum: Desc: RMANum   Required: True
      :param RMALine: Desc: RMALine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/RMADtlSearches(" + Company + "," + RMANum + "," + RMALine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RMADtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRMADtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRMADtl=" + whereClauseRMADtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rmANum, rmALine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "rmANum=" + rmANum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rmALine=" + rmALine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Calls the normal GetRows method and then if a customer ID has been passed, it screens out only the appropriate rows.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTrackerAndSort(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTrackerAndSort
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the customer tracker.
   OperationID: GetRowsCustomerTrackerAndSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTrackerAndSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTrackerAndSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Calls the normal GetRows method and then if a customer ID has been passed, it screens out only the appropriate rows.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsProjectTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsProjectTracker
   Description: Get all RMA's associated with orders for this projectID
   OperationID: GetRowsProjectTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsProjectTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsProjectTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRMADtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRMADtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRMADtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRMADtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRMADtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RMADtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMADtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RMADtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RMADtlRow] = obj["value"]
      pass

class Erp_Tablesets_RMADtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Mirror image of RMAHead.OpenRMA.  """  
      self.OpenDtl:bool = obj["OpenDtl"]
      """  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.Note:str = obj["Note"]
      """   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.RefInvoiceNum:int = obj["RefInvoiceNum"]
      """  Reference Invoice number used for finding Tax Category  """  
      self.RefInvoiceLine:int = obj["RefInvoiceLine"]
      """  Reference invoice line - Used to obtain the correct tax category  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number that the RMA line was created from.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Reference AR Invoice Line Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  From RMAHead.DebitMemoRef, used by Customer Tracker  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  From RMAHead.HDCaseNum, used by Customer Tracker  """  
      self.RMADate:str = obj["RMADate"]
      """  Set from RMAHead.RMADate, used by Customer Tracker  """  
      self.RMARcptExists:bool = obj["RMARcptExists"]
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      self.CustomerName:str = obj["CustomerName"]
      self.ShipToName:str = obj["ShipToName"]
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ReturnReasonCodeDescription:str = obj["ReturnReasonCodeDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Mirror image of RMAHead.OpenRMA.  """  
      self.OpenDtl:bool = obj["OpenDtl"]
      """  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.Note:str = obj["Note"]
      """   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.RefInvoiceNum:int = obj["RefInvoiceNum"]
      """  Reference Invoice number used for finding Tax Category  """  
      self.RefInvoiceLine:int = obj["RefInvoiceLine"]
      """  Reference invoice line - Used to obtain the correct tax category  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number that the RMA line was created from.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Reference AR Invoice Line Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECC RMA Comment  """  
      self.ECCRMANum:str = obj["ECCRMANum"]
      """  ECC RMA Num  """  
      self.ECCRMALine:int = obj["ECCRMALine"]
      """  ECC RMA Line  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  """  
      self.ConsolidateOneRelease:bool = obj["ConsolidateOneRelease"]
      """  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  """  
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      """  The name for the ship to location.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  From RMAHead.DebitMemoRef, used by Customer Tracker  """  
      self.EnableAddCreditMemo:bool = obj["EnableAddCreditMemo"]
      """  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the RMA is synchronized with Epicor FSA application.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceType:str = obj["FSAServiceType"]
      """  Serivce Type  """  
      self.FSATechnician:str = obj["FSATechnician"]
      """  Technician  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  From RMAHead.HDCaseNum, used by Customer Tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LocalizationFlag:str = obj["LocalizationFlag"]
      self.RMADate:str = obj["RMADate"]
      """  Set from RMAHead.RMADate, used by Customer Tracker  """  
      self.RMARcptExists:bool = obj["RMARcptExists"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  The customer ID.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.AttrValueSetDescription:str = obj["AttrValueSetDescription"]
      self.AttrValueSetShortDescription:str = obj["AttrValueSetShortDescription"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ReturnReasonCodeDescription:str = obj["ReturnReasonCodeDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   rmANum
   rmALine
   """  
   def __init__(self, obj):
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RMADtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Mirror image of RMAHead.OpenRMA.  """  
      self.OpenDtl:bool = obj["OpenDtl"]
      """  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.Note:str = obj["Note"]
      """   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.RefInvoiceNum:int = obj["RefInvoiceNum"]
      """  Reference Invoice number used for finding Tax Category  """  
      self.RefInvoiceLine:int = obj["RefInvoiceLine"]
      """  Reference invoice line - Used to obtain the correct tax category  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number that the RMA line was created from.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Reference AR Invoice Line Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  From RMAHead.DebitMemoRef, used by Customer Tracker  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  From RMAHead.HDCaseNum, used by Customer Tracker  """  
      self.RMADate:str = obj["RMADate"]
      """  Set from RMAHead.RMADate, used by Customer Tracker  """  
      self.RMARcptExists:bool = obj["RMARcptExists"]
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      self.CustomerName:str = obj["CustomerName"]
      self.ShipToName:str = obj["ShipToName"]
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ReturnReasonCodeDescription:str = obj["ReturnReasonCodeDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADtlListTableset:
   def __init__(self, obj):
      self.RMADtlList:list[Erp_Tablesets_RMADtlListRow] = obj["RMADtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RMADtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRMA:bool = obj["OpenRMA"]
      """  Mirror image of RMAHead.OpenRMA.  """  
      self.OpenDtl:bool = obj["OpenDtl"]
      """  Indicates the Open/Closed status of the RMADtl.  This gets set to closed when there are no pending actions to be taken on related receipts.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.Note:str = obj["Note"]
      """   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.RefInvoiceNum:int = obj["RefInvoiceNum"]
      """  Reference Invoice number used for finding Tax Category  """  
      self.RefInvoiceLine:int = obj["RefInvoiceLine"]
      """  Reference invoice line - Used to obtain the correct tax category  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number that the RMA line was created from.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference AR Invoice Number  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Reference AR Invoice Line Number  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECC RMA Comment  """  
      self.ECCRMANum:str = obj["ECCRMANum"]
      """  ECC RMA Num  """  
      self.ECCRMALine:int = obj["ECCRMALine"]
      """  ECC RMA Line  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  Indicates that the line of the invoice has multiple packs consolidated. Details of the pack should be reviewied in InvcDtlPack table  """  
      self.ConsolidateOneRelease:bool = obj["ConsolidateOneRelease"]
      """  Indicates that the invoice line has consolidated shipment lines that are related to the same release of the sales order  """  
      self.CustomerContactEMailAddress:str = obj["CustomerContactEMailAddress"]
      self.CustomerName:str = obj["CustomerName"]
      """  The full customer's name.  """  
      self.CustomerShipToName:str = obj["CustomerShipToName"]
      """  The name for the ship to location.  """  
      self.DebitMemoRef:str = obj["DebitMemoRef"]
      """  From RMAHead.DebitMemoRef, used by Customer Tracker  """  
      self.EnableAddCreditMemo:bool = obj["EnableAddCreditMemo"]
      """  If company parameter 'Allow Multiple Credit Invoices' is off and there is a least one credit memo then another credit memo adding is not allowed.  """  
      self.EnableDelete:bool = obj["EnableDelete"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Flag to determine if Serial Numbers are required for this transaction.  """  
      self.EnableUpdate:bool = obj["EnableUpdate"]
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the RMA is synchronized with Epicor FSA application.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceType:str = obj["FSAServiceType"]
      """  Serivce Type  """  
      self.FSATechnician:str = obj["FSATechnician"]
      """  Technician  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  From RMAHead.HDCaseNum, used by Customer Tracker  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LocalizationFlag:str = obj["LocalizationFlag"]
      self.RMADate:str = obj["RMADate"]
      """  Set from RMAHead.RMADate, used by Customer Tracker  """  
      self.RMARcptExists:bool = obj["RMARcptExists"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.CustomerContactName:str = obj["CustomerContactName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  The customer ID.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.BitFlag:int = obj["BitFlag"]
      self.AttrValueSetDescription:str = obj["AttrValueSetDescription"]
      self.AttrValueSetShortDescription:str = obj["AttrValueSetShortDescription"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ReturnReasonCodeDescription:str = obj["ReturnReasonCodeDescription"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RMADtlSearchTableset:
   def __init__(self, obj):
      self.RMADtl:list[Erp_Tablesets_RMADtlRow] = obj["RMADtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRMADtlSearchTableset:
   def __init__(self, obj):
      self.RMADtl:list[Erp_Tablesets_RMADtlRow] = obj["RMADtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   rmANum
   rmALine
   """  
   def __init__(self, obj):
      self.rmANum:int = obj["rmANum"]
      self.rmALine:int = obj["rmALine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RMADtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRMADtl_input:
   """ Required : 
   ds
   rmANum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADtlSearchTableset] = obj["ds"]
      self.rmANum:int = obj["rmANum"]
      pass

class GetNewRMADtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseRMADtl
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRMADtl:str = obj["whereClauseRMADtl"]
      """  Whereclause for RMADtl table.  """  
      self.contactName:str = obj["contactName"]
      """  The contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTrackerAndSort_input:
   """ Required : 
   whereClauseRMADtl
   whereClauseRMAHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRMADtl:str = obj["whereClauseRMADtl"]
      """  Whereclause for RMADtl table.  """  
      self.whereClauseRMAHead:str = obj["whereClauseRMAHead"]
      """  Whereclause for RMAHead table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTrackerAndSort_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseRMADtl
   whereClauseRMAHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRMADtl:str = obj["whereClauseRMADtl"]
      """  Whereclause for RMADtl table.  """  
      self.whereClauseRMAHead:str = obj["whereClauseRMAHead"]
      """  Whereclause for RMAHead table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsProjectTracker_input:
   """ Required : 
   ipProjectID
   """  
   def __init__(self, obj):
      self.ipProjectID:str = obj["ipProjectID"]
      """  The Project ID  """  
      pass

class GetRowsProjectTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseRMADtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRMADtl:str = obj["whereClauseRMADtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RMADtlSearchTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRMADtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRMADtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RMADtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RMADtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

