import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RFQEntryQuoteSearchSvc
# Description: This is a QuoteSearch object for RFQEntr.
It is used to display Quotes which are relevant in
Add From Quote functionality of RFQEntry.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RFQEntryQuoteSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQEntryQuoteSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQEntryQuoteSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches",headers=creds) as resp:
           return await resp.json()

async def post_RFQEntryQuoteSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQEntryQuoteSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQEntryQuoteSearches_Company_QuoteNum(Company, QuoteNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQEntryQuoteSearch item
   Description: Calls GetByID to retrieve the RFQEntryQuoteSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQEntryQuoteSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches(" + Company + "," + QuoteNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQEntryQuoteSearches_Company_QuoteNum(Company, QuoteNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQEntryQuoteSearch for the service
   Description: Calls UpdateExt to update RFQEntryQuoteSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQEntryQuoteSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches(" + Company + "," + QuoteNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQEntryQuoteSearches_Company_QuoteNum(Company, QuoteNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQEntryQuoteSearch item
   Description: Call UpdateExt to delete RFQEntryQuoteSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQEntryQuoteSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/RFQEntryQuoteSearches(" + Company + "," + QuoteNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQuoteHed, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseQuoteHed=" + whereClauseQuoteHed
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(quoteNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "quoteNum=" + quoteNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQEntryQuoteSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteHedRow] = obj["value"]
      pass

class Erp_Tablesets_QuoteHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description for CurrentStage field  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill to customer id.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill to customer name.  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CustomerName:str = obj["CustomerName"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the overall Quote. These will be printed on the Quote form.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """  Optional check off # 2.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """  Optional check off # 3.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional check off # 4.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional check off # 5.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.FlwAlrtSnt:bool = obj["FlwAlrtSnt"]
      """  System maintained flag - set to yes when the quote follow up alert has been sent.  """  
      self.DueAlrtSnt:bool = obj["DueAlrtSnt"]
      """  System maintained flag - set to yes when the quote due date alert has been sent.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LeadRating:str = obj["LeadRating"]
      """  A = High, Z = Low  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.ParentQuoteNum:int = obj["ParentQuoteNum"]
      """  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ExpectedClose:str = obj["ExpectedClose"]
      """  The date this quote is expected to close.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.QuoteClosed:bool = obj["QuoteClosed"]
      """  This quote is no longer updatable.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The date that the Quote was closed.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.ApplyOrderBasedDisc:bool = obj["ApplyOrderBasedDisc"]
      """  Indicates if order based discounting needs to be applied to the quote.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this quote.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.LockRate:bool = obj["LockRate"]
      """  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.QuoteAmt:int = obj["QuoteAmt"]
      """  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  """  
      self.DocQuoteAmt:int = obj["DocQuoteAmt"]
      """  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1QuoteAmt:int = obj["Rpt1QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2QuoteAmt:int = obj["Rpt2QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3QuoteAmt:int = obj["Rpt3QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready.  """  
      self.EDIQuote:bool = obj["EDIQuote"]
      """  Quote created from EDI interfaced module.  """  
      self.EDIAck:bool = obj["EDIAck"]
      """  Updated from EDI module this type of document is created.  """  
      self.OutboundQuoteDocCtr:int = obj["OutboundQuoteDocCtr"]
      """  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.LastTCtrlNum:str = obj["LastTCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.LastBatchNum:str = obj["LastBatchNum"]
      """  EDI Batch Control Number  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.DropShip:bool = obj["DropShip"]
      """  Freight charges will not be returned if 'yes'  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number that uniquely identifies the purchase order.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote header is linked to an inter-company PO header.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.VoidQuote:bool = obj["VoidQuote"]
      """  Indicates that the Quote item was closed before any shipments were made against it.  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.TotalDiscPct:int = obj["TotalDiscPct"]
      """  Total discount percent.  """  
      self.TotalExpected:int = obj["TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.TotalGrossValue:int = obj["TotalGrossValue"]
      self.TotalMiscAmt:int = obj["TotalMiscAmt"]
      self.TotalPotential:int = obj["TotalPotential"]
      self.TotalWorstCs:int = obj["TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.DocTotalBestCs:int = obj["DocTotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      self.DocTotalDiscPct:int = obj["DocTotalDiscPct"]
      """  Total discount percent.  """  
      self.DocTotalExpected:int = obj["DocTotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.DocTotalGrossValue:int = obj["DocTotalGrossValue"]
      self.DocTotalMiscAmt:int = obj["DocTotalMiscAmt"]
      self.DocTotalPotential:int = obj["DocTotalPotential"]
      self.DocTotalWorstCs:int = obj["DocTotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt1TotalBestCs:int = obj["Rpt1TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      self.Rpt1TotalDiscPct:int = obj["Rpt1TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt1TotalExpected:int = obj["Rpt1TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt1TotalGrossValue:int = obj["Rpt1TotalGrossValue"]
      self.Rpt1TotalMiscAmt:int = obj["Rpt1TotalMiscAmt"]
      self.Rpt1TotalPotential:int = obj["Rpt1TotalPotential"]
      self.Rpt1TotalWorstCs:int = obj["Rpt1TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt2TotalBestCs:int = obj["Rpt2TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      self.Rpt2TotalDiscPct:int = obj["Rpt2TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt2TotalExpected:int = obj["Rpt2TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt2TotalGrossValue:int = obj["Rpt2TotalGrossValue"]
      self.Rpt2TotalMiscAmt:int = obj["Rpt2TotalMiscAmt"]
      self.Rpt2TotalPotential:int = obj["Rpt2TotalPotential"]
      self.Rpt2TotalWorstCs:int = obj["Rpt2TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt3TotalBestCs:int = obj["Rpt3TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      self.Rpt3TotalDiscPct:int = obj["Rpt3TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt3TotalExpected:int = obj["Rpt3TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt3TotalGrossValue:int = obj["Rpt3TotalGrossValue"]
      self.Rpt3TotalMiscAmt:int = obj["Rpt3TotalMiscAmt"]
      self.Rpt3TotalPotential:int = obj["Rpt3TotalPotential"]
      self.Rpt3TotalWorstCs:int = obj["Rpt3TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.TotalBestCs:int = obj["TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.LOQPrepressText:str = obj["LOQPrepressText"]
      """  LOQPrepressText  """  
      self.LOQNewPageOnQuoteLine:bool = obj["LOQNewPageOnQuoteLine"]
      """  LOQNewPageOnQuoteLine  """  
      self.LOQBookPCFinishing:bool = obj["LOQBookPCFinishing"]
      """  LOQBookPCFinishing  """  
      self.LOQBookPCPaper:bool = obj["LOQBookPCPaper"]
      """  LOQBookPCPaper  """  
      self.LOQBookPCPress:bool = obj["LOQBookPCPress"]
      """  LOQBookPCPress  """  
      self.LOQBookPCPlates:bool = obj["LOQBookPCPlates"]
      """  LOQBookPCPlates  """  
      self.LOQVariations:bool = obj["LOQVariations"]
      """  LOQVariations  """  
      self.AEPLOQType:str = obj["AEPLOQType"]
      """  AEPLOQType  """  
      self.LOQPrepressStyle:str = obj["LOQPrepressStyle"]
      """  LOQPrepressStyle  """  
      self.QuoteCSR:str = obj["QuoteCSR"]
      """  QuoteCSR  """  
      self.DueHour:str = obj["DueHour"]
      """  DueHour  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCConfirmed:bool = obj["ECCConfirmed"]
      """  Quote was confirmed/rejected by ECC Web  """  
      self.ECCConfirmedBy:str = obj["ECCConfirmedBy"]
      """  Quote was confirmed/rejected by this ECC user  """  
      self.ECCMsgType:str = obj["ECCMsgType"]
      """  ECC quote message: RFQ or GQR  """  
      self.ECCWebReady:bool = obj["ECCWebReady"]
      """  Quote is ready to be approved by user via ECC web site.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Reference Number  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ECCStatus:str = obj["ECCStatus"]
      """  ECC Quote Status  """  
      self.ECCExpirationDate:str = obj["ECCExpirationDate"]
      """  ECC Expiration Date  """  
      self.ECCCmmtRefSK:str = obj["ECCCmmtRefSK"]
      """  ECCCmmtRefSK  """  
      self.ExternalCRMQuote:bool = obj["ExternalCRMQuote"]
      """  This field defines if the Quote  is synchronized to an External CRM.  """  
      self.ExternalCRMQuoteID:str = obj["ExternalCRMQuoteID"]
      """  This field holds the  id of this quote in the External CRM  """  
      self.ExternalCRMOrderID:str = obj["ExternalCRMOrderID"]
      """  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  """  
      self.ECCSalesRepID:str = obj["ECCSalesRepID"]
      """  Web Sales Rep ID  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  HdrTaxNoUpdt  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  """  
      self.TotalClaimsCredit:int = obj["TotalClaimsCredit"]
      """  Total of claims credit lines  """  
      self.DocTotalClaimsCredit:int = obj["DocTotalClaimsCredit"]
      """  Total of claims credit lines in customer currency  """  
      self.Rpt1TotalClaimsCredit:int = obj["Rpt1TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt2TotalClaimsCredit:int = obj["Rpt2TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt3TotalClaimsCredit:int = obj["Rpt3TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.TotalClaimsTax:int = obj["TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes.  """  
      self.DocTotalClaimsTax:int = obj["DocTotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in customer currency.  """  
      self.Rpt1TotalClaimsTax:int = obj["Rpt1TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt2TotalClaimsTax:int = obj["Rpt2TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt3TotalClaimsTax:int = obj["Rpt3TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.TotalClaimsSATax:int = obj["TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes.  """  
      self.DocTotalClaimsSATax:int = obj["DocTotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt1TotalClaimsSATax:int = obj["Rpt1TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt2TotalClaimsSATax:int = obj["Rpt2TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt3TotalClaimsSATax:int = obj["Rpt3TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.TotalClaimsWHTax:int = obj["TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes.  """  
      self.DocTotalClaimsWHTax:int = obj["DocTotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in customer currency.  """  
      self.Rpt1TotalClaimsWHTax:int = obj["Rpt1TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt2TotalClaimsWHTax:int = obj["Rpt2TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt3TotalClaimsWHTax:int = obj["Rpt3TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.AddrList:str = obj["AddrList"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill To Customer Name.  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  Audit Log change description  """  
      self.CheckOffLabel1:str = obj["CheckOffLabel1"]
      self.CheckOffLabel2:str = obj["CheckOffLabel2"]
      self.CheckOffLabel3:str = obj["CheckOffLabel3"]
      self.CheckOffLabel4:str = obj["CheckOffLabel4"]
      self.CheckOffLabel5:str = obj["CheckOffLabel5"]
      self.Conclusion:str = obj["Conclusion"]
      self.ConName:str = obj["ConName"]
      """  Primary Contact Name  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description of the CurrentStage field  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Value of the Customer.AllowOTS (customer allows one time shipment)  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.DaysOpen:int = obj["DaysOpen"]
      """  Number of days Quote has been open  """  
      self.DiscountPercentCalc:int = obj["DiscountPercentCalc"]
      """   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the quote.  """  
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.dspBTCustID:str = obj["dspBTCustID"]
      """  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      self.EnableOrderBasedDisc:bool = obj["EnableOrderBasedDisc"]
      """  Indicates if it's okay to enable OrderBased Pricing  """  
      self.ExpectedCsPct:int = obj["ExpectedCsPct"]
      """   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  """  
      self.FaxNum:str = obj["FaxNum"]
      self.FOB:str = obj["FOB"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.HasQuoteLines:bool = obj["HasQuoteLines"]
      """  Used by IU to disabled Currency Code  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  EqSyst.LogChanges  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date  """  
      self.OrderDiscount:int = obj["OrderDiscount"]
      self.OrderPONum:str = obj["OrderPONum"]
      self.OrderShipVia:str = obj["OrderShipVia"]
      self.OrderTerms:str = obj["OrderTerms"]
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PreventQQChange:bool = obj["PreventQQChange"]
      self.RateLabel:str = obj["RateLabel"]
      """  Label for ExchangeRate  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.TotalQuote:int = obj["TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.WorseCsPctCalc:int = obj["WorseCsPctCalc"]
      """   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.BestCsPctCalc:int = obj["BestCsPctCalc"]
      """   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill To Address List.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Customer ID of the bill to customer.  """  
      self.HasCreditLines:bool = obj["HasCreditLines"]
      """  Indicates if the order contains any credit type line  """  
      self.IsValidECC:bool = obj["IsValidECC"]
      """  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  """  
      self.EnableHDCaseNum:bool = obj["EnableHDCaseNum"]
      """  Flag indicating whether to enable CaseNum or not  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  Indicates if the quote can be updated  """  
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Formatted address  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Ship To Address formatted  """  
      self.PromptTaxRegionCode:bool = obj["PromptTaxRegionCode"]
      """  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the quote is inactive.  """  
      self.UpdatePrimContact:bool = obj["UpdatePrimContact"]
      """  Update primary contact on save of the quote header  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActiveTaskTaskDescription:str = obj["ActiveTaskTaskDescription"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyBaseCurr:bool = obj["CurrencyBaseCurr"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCheckDuplicatePO:bool = obj["CustomerCheckDuplicatePO"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.LastTaskTaskDescription:str = obj["LastTaskTaskDescription"]
      self.MktgCpgnCampDescription:str = obj["MktgCpgnCampDescription"]
      self.MktgEventEvntDescription:str = obj["MktgEventEvntDescription"]
      self.OTSCountryNumISOCode:str = obj["OTSCountryNumISOCode"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.OTSCountryNumEUMember:bool = obj["OTSCountryNumEUMember"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ResponseCallTypeDesc:str = obj["ResponseCallTypeDesc"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaInactive:bool = obj["ShipViaInactive"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.XbSystCalcQuoteTax:bool = obj["XbSystCalcQuoteTax"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_QuoteHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description for CurrentStage field  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill to customer id.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill to customer name.  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CustomerName:str = obj["CustomerName"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteHedListTableset:
   def __init__(self, obj):
      self.QuoteHedList:list[Erp_Tablesets_QuoteHedListRow] = obj["QuoteHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuoteHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the overall Quote. These will be printed on the Quote form.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """  Optional check off # 2.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """  Optional check off # 3.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional check off # 4.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional check off # 5.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.FlwAlrtSnt:bool = obj["FlwAlrtSnt"]
      """  System maintained flag - set to yes when the quote follow up alert has been sent.  """  
      self.DueAlrtSnt:bool = obj["DueAlrtSnt"]
      """  System maintained flag - set to yes when the quote due date alert has been sent.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LeadRating:str = obj["LeadRating"]
      """  A = High, Z = Low  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.ParentQuoteNum:int = obj["ParentQuoteNum"]
      """  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ExpectedClose:str = obj["ExpectedClose"]
      """  The date this quote is expected to close.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.QuoteClosed:bool = obj["QuoteClosed"]
      """  This quote is no longer updatable.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The date that the Quote was closed.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.ApplyOrderBasedDisc:bool = obj["ApplyOrderBasedDisc"]
      """  Indicates if order based discounting needs to be applied to the quote.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this quote.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.LockRate:bool = obj["LockRate"]
      """  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.QuoteAmt:int = obj["QuoteAmt"]
      """  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  """  
      self.DocQuoteAmt:int = obj["DocQuoteAmt"]
      """  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1QuoteAmt:int = obj["Rpt1QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2QuoteAmt:int = obj["Rpt2QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3QuoteAmt:int = obj["Rpt3QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready.  """  
      self.EDIQuote:bool = obj["EDIQuote"]
      """  Quote created from EDI interfaced module.  """  
      self.EDIAck:bool = obj["EDIAck"]
      """  Updated from EDI module this type of document is created.  """  
      self.OutboundQuoteDocCtr:int = obj["OutboundQuoteDocCtr"]
      """  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.LastTCtrlNum:str = obj["LastTCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.LastBatchNum:str = obj["LastBatchNum"]
      """  EDI Batch Control Number  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.DropShip:bool = obj["DropShip"]
      """  Freight charges will not be returned if 'yes'  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number that uniquely identifies the purchase order.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote header is linked to an inter-company PO header.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.VoidQuote:bool = obj["VoidQuote"]
      """  Indicates that the Quote item was closed before any shipments were made against it.  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.TotalDiscPct:int = obj["TotalDiscPct"]
      """  Total discount percent.  """  
      self.TotalExpected:int = obj["TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.TotalGrossValue:int = obj["TotalGrossValue"]
      self.TotalMiscAmt:int = obj["TotalMiscAmt"]
      self.TotalPotential:int = obj["TotalPotential"]
      self.TotalWorstCs:int = obj["TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.DocTotalBestCs:int = obj["DocTotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      self.DocTotalDiscPct:int = obj["DocTotalDiscPct"]
      """  Total discount percent.  """  
      self.DocTotalExpected:int = obj["DocTotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.DocTotalGrossValue:int = obj["DocTotalGrossValue"]
      self.DocTotalMiscAmt:int = obj["DocTotalMiscAmt"]
      self.DocTotalPotential:int = obj["DocTotalPotential"]
      self.DocTotalWorstCs:int = obj["DocTotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt1TotalBestCs:int = obj["Rpt1TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      self.Rpt1TotalDiscPct:int = obj["Rpt1TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt1TotalExpected:int = obj["Rpt1TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt1TotalGrossValue:int = obj["Rpt1TotalGrossValue"]
      self.Rpt1TotalMiscAmt:int = obj["Rpt1TotalMiscAmt"]
      self.Rpt1TotalPotential:int = obj["Rpt1TotalPotential"]
      self.Rpt1TotalWorstCs:int = obj["Rpt1TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt2TotalBestCs:int = obj["Rpt2TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      self.Rpt2TotalDiscPct:int = obj["Rpt2TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt2TotalExpected:int = obj["Rpt2TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt2TotalGrossValue:int = obj["Rpt2TotalGrossValue"]
      self.Rpt2TotalMiscAmt:int = obj["Rpt2TotalMiscAmt"]
      self.Rpt2TotalPotential:int = obj["Rpt2TotalPotential"]
      self.Rpt2TotalWorstCs:int = obj["Rpt2TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt3TotalBestCs:int = obj["Rpt3TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      self.Rpt3TotalDiscPct:int = obj["Rpt3TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt3TotalExpected:int = obj["Rpt3TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt3TotalGrossValue:int = obj["Rpt3TotalGrossValue"]
      self.Rpt3TotalMiscAmt:int = obj["Rpt3TotalMiscAmt"]
      self.Rpt3TotalPotential:int = obj["Rpt3TotalPotential"]
      self.Rpt3TotalWorstCs:int = obj["Rpt3TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.TotalBestCs:int = obj["TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.LOQPrepressText:str = obj["LOQPrepressText"]
      """  LOQPrepressText  """  
      self.LOQNewPageOnQuoteLine:bool = obj["LOQNewPageOnQuoteLine"]
      """  LOQNewPageOnQuoteLine  """  
      self.LOQBookPCFinishing:bool = obj["LOQBookPCFinishing"]
      """  LOQBookPCFinishing  """  
      self.LOQBookPCPaper:bool = obj["LOQBookPCPaper"]
      """  LOQBookPCPaper  """  
      self.LOQBookPCPress:bool = obj["LOQBookPCPress"]
      """  LOQBookPCPress  """  
      self.LOQBookPCPlates:bool = obj["LOQBookPCPlates"]
      """  LOQBookPCPlates  """  
      self.LOQVariations:bool = obj["LOQVariations"]
      """  LOQVariations  """  
      self.AEPLOQType:str = obj["AEPLOQType"]
      """  AEPLOQType  """  
      self.LOQPrepressStyle:str = obj["LOQPrepressStyle"]
      """  LOQPrepressStyle  """  
      self.QuoteCSR:str = obj["QuoteCSR"]
      """  QuoteCSR  """  
      self.DueHour:str = obj["DueHour"]
      """  DueHour  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCConfirmed:bool = obj["ECCConfirmed"]
      """  Quote was confirmed/rejected by ECC Web  """  
      self.ECCConfirmedBy:str = obj["ECCConfirmedBy"]
      """  Quote was confirmed/rejected by this ECC user  """  
      self.ECCMsgType:str = obj["ECCMsgType"]
      """  ECC quote message: RFQ or GQR  """  
      self.ECCWebReady:bool = obj["ECCWebReady"]
      """  Quote is ready to be approved by user via ECC web site.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Reference Number  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ECCStatus:str = obj["ECCStatus"]
      """  ECC Quote Status  """  
      self.ECCExpirationDate:str = obj["ECCExpirationDate"]
      """  ECC Expiration Date  """  
      self.ECCCmmtRefSK:str = obj["ECCCmmtRefSK"]
      """  ECCCmmtRefSK  """  
      self.ExternalCRMQuote:bool = obj["ExternalCRMQuote"]
      """  This field defines if the Quote  is synchronized to an External CRM.  """  
      self.ExternalCRMQuoteID:str = obj["ExternalCRMQuoteID"]
      """  This field holds the  id of this quote in the External CRM  """  
      self.ExternalCRMOrderID:str = obj["ExternalCRMOrderID"]
      """  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  """  
      self.ECCSalesRepID:str = obj["ECCSalesRepID"]
      """  Web Sales Rep ID  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  HdrTaxNoUpdt  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  """  
      self.TotalClaimsCredit:int = obj["TotalClaimsCredit"]
      """  Total of claims credit lines  """  
      self.DocTotalClaimsCredit:int = obj["DocTotalClaimsCredit"]
      """  Total of claims credit lines in customer currency  """  
      self.Rpt1TotalClaimsCredit:int = obj["Rpt1TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt2TotalClaimsCredit:int = obj["Rpt2TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt3TotalClaimsCredit:int = obj["Rpt3TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.TotalClaimsTax:int = obj["TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes.  """  
      self.DocTotalClaimsTax:int = obj["DocTotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in customer currency.  """  
      self.Rpt1TotalClaimsTax:int = obj["Rpt1TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt2TotalClaimsTax:int = obj["Rpt2TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt3TotalClaimsTax:int = obj["Rpt3TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.TotalClaimsSATax:int = obj["TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes.  """  
      self.DocTotalClaimsSATax:int = obj["DocTotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt1TotalClaimsSATax:int = obj["Rpt1TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt2TotalClaimsSATax:int = obj["Rpt2TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt3TotalClaimsSATax:int = obj["Rpt3TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.TotalClaimsWHTax:int = obj["TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes.  """  
      self.DocTotalClaimsWHTax:int = obj["DocTotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in customer currency.  """  
      self.Rpt1TotalClaimsWHTax:int = obj["Rpt1TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt2TotalClaimsWHTax:int = obj["Rpt2TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt3TotalClaimsWHTax:int = obj["Rpt3TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.AddrList:str = obj["AddrList"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill To Customer Name.  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  Audit Log change description  """  
      self.CheckOffLabel1:str = obj["CheckOffLabel1"]
      self.CheckOffLabel2:str = obj["CheckOffLabel2"]
      self.CheckOffLabel3:str = obj["CheckOffLabel3"]
      self.CheckOffLabel4:str = obj["CheckOffLabel4"]
      self.CheckOffLabel5:str = obj["CheckOffLabel5"]
      self.Conclusion:str = obj["Conclusion"]
      self.ConName:str = obj["ConName"]
      """  Primary Contact Name  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrentStageDesc:str = obj["CurrentStageDesc"]
      """  Full Description of the CurrentStage field  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Value of the Customer.AllowOTS (customer allows one time shipment)  """  
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.DaysOpen:int = obj["DaysOpen"]
      """  Number of days Quote has been open  """  
      self.DiscountPercentCalc:int = obj["DiscountPercentCalc"]
      """   Display the true discount percent of the quote. It's calculated by dividing the sum Discount Percent over Gross Value.
DiscountPercentCalc = (DocTotalDiscount / TotalGrossValue) *100  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total tax in Doc currency. The sum of all the tax details for the quote.  """  
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.dspBTCustID:str = obj["dspBTCustID"]
      """  Used for screen display. If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      self.EnableOrderBasedDisc:bool = obj["EnableOrderBasedDisc"]
      """  Indicates if it's okay to enable OrderBased Pricing  """  
      self.ExpectedCsPct:int = obj["ExpectedCsPct"]
      """   The expected revenue potential percentage of all lines.
ExpectedCsPct = (TotalExpected / TotalPotential) * 100  """  
      self.FaxNum:str = obj["FaxNum"]
      self.FOB:str = obj["FOB"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.HasQuoteLines:bool = obj["HasQuoteLines"]
      """  Used by IU to disabled Currency Code  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  EqSyst.LogChanges  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Order Date  """  
      self.OrderDiscount:int = obj["OrderDiscount"]
      self.OrderPONum:str = obj["OrderPONum"]
      self.OrderShipVia:str = obj["OrderShipVia"]
      self.OrderTerms:str = obj["OrderTerms"]
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PreventQQChange:bool = obj["PreventQQChange"]
      self.RateLabel:str = obj["RateLabel"]
      """  Label for ExchangeRate  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.TotalQuote:int = obj["TotalQuote"]
      """   Quote total after including taxes.
TotalQuote = TotalPotential +  TotalMiscAmt + TaxAmt  """  
      self.WorseCsPctCalc:int = obj["WorseCsPctCalc"]
      """   Displays the calculated revenue potential percentage (worst case) for the quote line.
WorseCsPctCalc = (TotalWorstCs / TotalPotential) * 100  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for currency "BASE"  """  
      self.BestCsPctCalc:int = obj["BestCsPctCalc"]
      """   Displays the calculated revenue potential percentage (best case) for the quote line.
BestCsPctCalc = (TotalBestCs / TotalPotential) * 100  """  
      self.BTAddressList:str = obj["BTAddressList"]
      """  Bill To Address List.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Customer ID of the bill to customer.  """  
      self.HasCreditLines:bool = obj["HasCreditLines"]
      """  Indicates if the order contains any credit type line  """  
      self.IsValidECC:bool = obj["IsValidECC"]
      """  Returns true if Customer.ECCType is B2C OR Dealer OR Distributor AND Customer.WebCustomer  """  
      self.EnableHDCaseNum:bool = obj["EnableHDCaseNum"]
      """  Flag indicating whether to enable CaseNum or not  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  Indicates if the quote can be updated  """  
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Formatted address  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Ship To Address formatted  """  
      self.PromptTaxRegionCode:bool = obj["PromptTaxRegionCode"]
      """  Indicates if tax region is one of the field changes the user is asked about for propogating changes to lines  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the quote is inactive.  """  
      self.UpdatePrimContact:bool = obj["UpdatePrimContact"]
      """  Update primary contact on save of the quote header  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActiveTaskTaskDescription:str = obj["ActiveTaskTaskDescription"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyBaseCurr:bool = obj["CurrencyBaseCurr"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCheckDuplicatePO:bool = obj["CustomerCheckDuplicatePO"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.LastTaskTaskDescription:str = obj["LastTaskTaskDescription"]
      self.MktgCpgnCampDescription:str = obj["MktgCpgnCampDescription"]
      self.MktgEventEvntDescription:str = obj["MktgEventEvntDescription"]
      self.OTSCountryNumISOCode:str = obj["OTSCountryNumISOCode"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.OTSCountryNumEUMember:bool = obj["OTSCountryNumEUMember"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.ResponseCallTypeDesc:str = obj["ResponseCallTypeDesc"]
      self.ShipToBTName:str = obj["ShipToBTName"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaInactive:bool = obj["ShipViaInactive"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.TerritoryTerritoryDesc:str = obj["TerritoryTerritoryDesc"]
      self.XbSystCalcQuoteTax:bool = obj["XbSystCalcQuoteTax"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQEntryQuoteSearchTableset:
   def __init__(self, obj):
      self.QuoteHed:list[Erp_Tablesets_QuoteHedRow] = obj["QuoteHed"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRFQEntryQuoteSearchTableset:
   def __init__(self, obj):
      self.QuoteHed:list[Erp_Tablesets_QuoteHedRow] = obj["QuoteHed"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   quoteNum
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuoteHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewQuoteHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["ds"]
      pass

class GetNewQuoteHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseQuoteHed
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtRFQEntryQuoteSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRFQEntryQuoteSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQEntryQuoteSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

