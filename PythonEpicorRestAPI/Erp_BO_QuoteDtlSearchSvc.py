import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuoteDtlSearchSvc
# Description: Quote Detail Search Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuoteDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuoteDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_QuoteDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuoteDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuoteDtlSearches_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuoteDtlSearch item
   Description: Calls GetByID to retrieve the QuoteDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuoteDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches(" + Company + "," + QuoteNum + "," + QuoteLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuoteDtlSearches_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuoteDtlSearch for the service
   Description: Calls UpdateExt to update QuoteDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuoteDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuoteDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches(" + Company + "," + QuoteNum + "," + QuoteLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuoteDtlSearches_Company_QuoteNum_QuoteLine(Company, QuoteNum, QuoteLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuoteDtlSearch item
   Description: Call UpdateExt to delete QuoteDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuoteDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param QuoteNum: Desc: QuoteNum   Required: True
      :param QuoteLine: Desc: QuoteLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/QuoteDtlSearches(" + Company + "," + QuoteNum + "," + QuoteLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuoteDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQuoteDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseQuoteDtl=" + whereClauseQuoteDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(quoteNum, quoteLine, epicorHeaders = None):
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
   params += "quoteNum=" + quoteNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "quoteLine=" + quoteLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: This methods will return all of the QuoteDtlSearch records which will be a subset
of the QuoteDtl records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (QuoteDtlList) we need our own public method.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuoteDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuoteDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuoteDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuoteDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuoteDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuoteDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuoteDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuoteDtlRow] = obj["value"]
      pass

class Erp_Tablesets_QuoteDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of linked project.  Must exist on the Project table. Can be blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MakeDirect:bool = obj["MakeDirect"]
      """  To indicate whether or not the line is make direct  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Must exist on ProjPhase table if entered  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Non-blank value prevents taxes from being calculated for this line item  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpectedRevenue:int = obj["Rpt1ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpectedRevenue:int = obj["Rpt2ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpectedRevenue:int = obj["Rpt3ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpUnitPrice:int = obj["Rpt1ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpUnitPrice:int = obj["Rpt2ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpUnitPrice:int = obj["Rpt3ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the quote line, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.InDiscount:int = obj["InDiscount"]
      """  Reserved for future use  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  Reserved for future use  """  
      self.InExpectedRevenue:int = obj["InExpectedRevenue"]
      """  Reserved for future use  """  
      self.DocInExpectedRevenue:int = obj["DocInExpectedRevenue"]
      """  Reserved for future use  """  
      self.InListPrice:int = obj["InListPrice"]
      """  Reserved for future use  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  Reserved for future use  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExpUnitPrice:int = obj["InExpUnitPrice"]
      """  Reserved for future use  """  
      self.DocInExpUnitPrice:int = obj["DocInExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InExpectedRevenue:int = obj["Rpt1InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt2InExpectedRevenue:int = obj["Rpt2InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt3InExpectedRevenue:int = obj["Rpt3InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt1InExpUnitPrice:int = obj["Rpt1InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InExpUnitPrice:int = obj["Rpt2InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InExpUnitPrice:int = obj["Rpt3InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reserved for future use  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reserved for future use  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reserved for future use  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Reserved for future use  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reserved for future use  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.Rpt1WorstCsRevenue:int = obj["Rpt1WorstCsRevenue"]
      self.Rpt2WorstCsRevenue:int = obj["Rpt2WorstCsRevenue"]
      self.Rpt3WorstCsRevenue:int = obj["Rpt3WorstCsRevenue"]
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Rpt1BestCsRevenue:int = obj["Rpt1BestCsRevenue"]
      self.Rpt2BestCsRevenue:int = obj["Rpt2BestCsRevenue"]
      self.Rpt3BestCsRevenue:int = obj["Rpt3BestCsRevenue"]
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  Demand Contract Line  """  
      self.DemandHedSeq:int = obj["DemandHedSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence number to which this record is related.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote line is linked to an inter-company PO line.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the quote line can be changed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """  Indicates that the line item was closed before any shipments were made against it.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.EstimateGUID:str = obj["EstimateGUID"]
      """  EstimateGUID  """  
      self.EstimateUserID:str = obj["EstimateUserID"]
      """  EstimateUserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.BaseExtPrice:int = obj["BaseExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.BasePotential:int = obj["BasePotential"]
      self.DocPotential:int = obj["DocPotential"]
      self.BaseMiscAmt:int = obj["BaseMiscAmt"]
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      self.Configured:str = obj["Configured"]
      """  Indicates whether the part is/can be configured  """  
      self.RefreshQty:bool = obj["RefreshQty"]
      """  Indicates whether to Refresh the QuoteQty table  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CheckPartDescription:bool = obj["CheckPartDescription"]
      """  If yes, then a new non-standard part was added with no description and validation needs to be run again  """  
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Delimited list of Available Price Lists  """  
      self.OrderWorthy:bool = obj["OrderWorthy"]
      """  If yes, the line will be copied to the Order  """  
      self.LineStatus:str = obj["LineStatus"]
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.OrderUM:str = obj["OrderUM"]
      self.OrderUnitPrice:int = obj["OrderUnitPrice"]
      self.DocOrderUnitPrice:int = obj["DocOrderUnitPrice"]
      self.CodePLM:bool = obj["CodePLM"]
      """  PLM Flag  """  
      self.EnablePLM:bool = obj["EnablePLM"]
      """  Flag indicating whether to enable CodePLM or not  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  The description for Kit Flag. "P" = Parent, "C" = Component.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.Rpt1BasePotential:int = obj["Rpt1BasePotential"]
      self.Rpt2BasePotential:int = obj["Rpt2BasePotential"]
      self.Rpt3BasePotential:int = obj["Rpt3BasePotential"]
      self.Rpt1BaseExtPrice:int = obj["Rpt1BaseExtPrice"]
      self.Rpt2BaseExtPrice:int = obj["Rpt2BaseExtPrice"]
      self.Rpt3BaseExtPrice:int = obj["Rpt3BaseExtPrice"]
      self.Rpt1BaseMiscAmt:int = obj["Rpt1BaseMiscAmt"]
      self.Rpt2BaseMiscAmt:int = obj["Rpt2BaseMiscAmt"]
      self.Rpt3BaseMiscAmt:int = obj["Rpt3BaseMiscAmt"]
      self.Rpt1OrderUnitPrice:int = obj["Rpt1OrderUnitPrice"]
      self.Rpt2OrderUnitPrice:int = obj["Rpt2OrderUnitPrice"]
      self.Rpt3OrderUnitPrice:int = obj["Rpt3OrderUnitPrice"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableDiscounts:bool = obj["DisableDiscounts"]
      """  Indicates if the discount fields should be disabled for the current quote line detail.  """  
      self.DspExpectedUM:str = obj["DspExpectedUM"]
      """  Used to displayed UOM for expected quantity for detail line  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
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
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      """  Description of the price list.  """  
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      """  Price Group description  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      """  Description of the sales category.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      """  Description of the territory.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  The date when this quote expires.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default  """  
      self.DspExpUnitPrice:int = obj["DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.DocDspExpUnitPrice:int = obj["DocDspExpUnitPrice"]
      """  Display Document unit price based on the expected quantity.  """  
      self.Rpt1DspExpUnitPrice:int = obj["Rpt1DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt2DspExpUnitPrice:int = obj["Rpt2DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt3DspExpUnitPrice:int = obj["Rpt3DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of linked project.  Must exist on the Project table. Can be blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MakeDirect:bool = obj["MakeDirect"]
      """  To indicate whether or not the line is make direct  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Must exist on ProjPhase table if entered  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Non-blank value prevents taxes from being calculated for this line item  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpectedRevenue:int = obj["Rpt1ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpectedRevenue:int = obj["Rpt2ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpectedRevenue:int = obj["Rpt3ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpUnitPrice:int = obj["Rpt1ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpUnitPrice:int = obj["Rpt2ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpUnitPrice:int = obj["Rpt3ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the quote line, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.InDiscount:int = obj["InDiscount"]
      """  Reserved for future use  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  Reserved for future use  """  
      self.InExpectedRevenue:int = obj["InExpectedRevenue"]
      """  Reserved for future use  """  
      self.DocInExpectedRevenue:int = obj["DocInExpectedRevenue"]
      """  Reserved for future use  """  
      self.InListPrice:int = obj["InListPrice"]
      """  Reserved for future use  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  Reserved for future use  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExpUnitPrice:int = obj["InExpUnitPrice"]
      """  Reserved for future use  """  
      self.DocInExpUnitPrice:int = obj["DocInExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InExpectedRevenue:int = obj["Rpt1InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt2InExpectedRevenue:int = obj["Rpt2InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt3InExpectedRevenue:int = obj["Rpt3InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt1InExpUnitPrice:int = obj["Rpt1InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InExpUnitPrice:int = obj["Rpt2InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InExpUnitPrice:int = obj["Rpt3InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reserved for future use  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reserved for future use  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reserved for future use  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Reserved for future use  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reserved for future use  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.Rpt1WorstCsRevenue:int = obj["Rpt1WorstCsRevenue"]
      self.Rpt2WorstCsRevenue:int = obj["Rpt2WorstCsRevenue"]
      self.Rpt3WorstCsRevenue:int = obj["Rpt3WorstCsRevenue"]
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Rpt1BestCsRevenue:int = obj["Rpt1BestCsRevenue"]
      self.Rpt2BestCsRevenue:int = obj["Rpt2BestCsRevenue"]
      self.Rpt3BestCsRevenue:int = obj["Rpt3BestCsRevenue"]
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  Demand Contract Line  """  
      self.DemandHedSeq:int = obj["DemandHedSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence number to which this record is related.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote line is linked to an inter-company PO line.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the quote line can be changed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """  Indicates that the line item was closed before any shipments were made against it.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.EstimateGUID:str = obj["EstimateGUID"]
      """  EstimateGUID  """  
      self.RFQCurrBaseEst:str = obj["RFQCurrBaseEst"]
      """  RFQCurrBaseEst  """  
      self.RFQTemplate:str = obj["RFQTemplate"]
      """  RFQTemplate  """  
      self.CreateEstimate:bool = obj["CreateEstimate"]
      """  CreateEstimate  """  
      self.Rating:str = obj["Rating"]
      """  Rating  """  
      self.EstimateUserID:str = obj["EstimateUserID"]
      """  EstimateUserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCQuoteLine:int = obj["ECCQuoteLine"]
      """  ECC Quote Line  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Ref  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  Indicates if no tax recalculation by the system is supposed to be done.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.ExternalCRMQuoteLineID:str = obj["ExternalCRMQuoteLineID"]
      """  This field holds the id of this quote line in the External CRM  """  
      self.ReturnLineType:str = obj["ReturnLineType"]
      """  Type for returns: Blank, (C)redit or (S)tandard  """  
      self.MSRP:int = obj["MSRP"]
      """  Base price before any price breaks and discounts  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1MSRP:int = obj["Rpt1MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt2MSRP:int = obj["Rpt2MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt3MSRP:int = obj["Rpt3MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  Distributor end customer price.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1EndCustomerPrice:int = obj["Rpt1EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt2EndCustomerPrice:int = obj["Rpt2EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt3EndCustomerPrice:int = obj["Rpt3EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  Mark For ShipToNum  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Contact Name  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1PromotionalPrice:int = obj["Rpt1PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt2PromotionalPrice:int = obj["Rpt2PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt3PromotionalPrice:int = obj["Rpt3PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseExtPrice:int = obj["BaseExtPrice"]
      self.BaseMiscAmt:int = obj["BaseMiscAmt"]
      self.BasePotential:int = obj["BasePotential"]
      self.CheckPartDescription:bool = obj["CheckPartDescription"]
      """  If yes, then a new non-standard part was added with no description and validation needs to be run again  """  
      self.CodePLM:bool = obj["CodePLM"]
      """  PLM Flag  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default  """  
      self.ConfigType:str = obj["ConfigType"]
      self.Configured:str = obj["Configured"]
      """  Indicates whether the part is/can be configured  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete.  """  
      self.DisableDiscounts:bool = obj["DisableDiscounts"]
      """  Indicates if the discount fields should be disabled for the current quote line detail.  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDspExpUnitPrice:int = obj["DocDspExpUnitPrice"]
      """  Display Document unit price based on the expected quantity.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      self.DocOrderUnitPrice:int = obj["DocOrderUnitPrice"]
      self.DocPotential:int = obj["DocPotential"]
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DspExpectedUM:str = obj["DspExpectedUM"]
      """  Used to displayed UOM for expected quantity for detail line  """  
      self.EnableRenewalNbr:bool = obj["EnableRenewalNbr"]
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  The date when this quote expires.  """  
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.HasCreditMemo:bool = obj["HasCreditMemo"]
      """  Indicates if this Quote line has an associated credit memo (only for dealer portal)  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  The description for Kit Flag. "P" = Parent, "C" = Component.  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.LineStatus:str = obj["LineStatus"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderUM:str = obj["OrderUM"]
      self.OrderUnitPrice:int = obj["OrderUnitPrice"]
      self.OrderWorthy:bool = obj["OrderWorthy"]
      """  If yes, the line will be copied to the Order  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if the Part is an Inventory Part.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.RefreshQty:bool = obj["RefreshQty"]
      """  Indicates whether to Refresh the QuoteQty table  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  """  
      self.Rpt1BaseExtPrice:int = obj["Rpt1BaseExtPrice"]
      self.Rpt1BaseMiscAmt:int = obj["Rpt1BaseMiscAmt"]
      self.Rpt1BasePotential:int = obj["Rpt1BasePotential"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1DspExpUnitPrice:int = obj["Rpt1DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt1OrderUnitPrice:int = obj["Rpt1OrderUnitPrice"]
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt2BaseExtPrice:int = obj["Rpt2BaseExtPrice"]
      self.Rpt2BaseMiscAmt:int = obj["Rpt2BaseMiscAmt"]
      self.Rpt2BasePotential:int = obj["Rpt2BasePotential"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2DspExpUnitPrice:int = obj["Rpt2DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt2OrderUnitPrice:int = obj["Rpt2OrderUnitPrice"]
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt3BaseExtPrice:int = obj["Rpt3BaseExtPrice"]
      self.Rpt3BaseMiscAmt:int = obj["Rpt3BaseMiscAmt"]
      self.Rpt3BasePotential:int = obj["Rpt3BasePotential"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3DspExpUnitPrice:int = obj["Rpt3DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt3OrderUnitPrice:int = obj["Rpt3OrderUnitPrice"]
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Selected:bool = obj["Selected"]
      """  Selected row  """  
      self.ShipByDate:str = obj["ShipByDate"]
      self.TotalPrice:int = obj["TotalPrice"]
      self.TotalQuote:int = obj["TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.UpdateReq:bool = obj["UpdateReq"]
      """   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  """  
      self.UseQuoteBOM:bool = obj["UseQuoteBOM"]
      """  Indicates that the Quote should be used as the BOM when creating a job for the linked order  """  
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Delimited list of Available Price Lists  """  
      self.DspExpUnitPrice:int = obj["DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.ECCLineCRQ:int = obj["ECCLineCRQ"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Allow enable/disable for the Dynamic Attributes button on a Quote Line  """  
      self.EnablePLM:bool = obj["EnablePLM"]
      """  Flag indicating whether to enable CodePLM or not  """  
      self.MarkForAddressFormatted:str = obj["MarkForAddressFormatted"]
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in Doc currency  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      """   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DiscBreakListCodeListDescription:str = obj["DiscBreakListCodeListDescription"]
      self.DiscBreakListCodeEndDate:str = obj["DiscBreakListCodeEndDate"]
      self.DiscBreakListCodeStartDate:str = obj["DiscBreakListCodeStartDate"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PartNumDefaultAttributeSetID:int = obj["PartNumDefaultAttributeSetID"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.QuoteNumInPrice:bool = obj["QuoteNumInPrice"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_QuoteDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of linked project.  Must exist on the Project table. Can be blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MakeDirect:bool = obj["MakeDirect"]
      """  To indicate whether or not the line is make direct  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Must exist on ProjPhase table if entered  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Non-blank value prevents taxes from being calculated for this line item  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpectedRevenue:int = obj["Rpt1ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpectedRevenue:int = obj["Rpt2ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpectedRevenue:int = obj["Rpt3ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpUnitPrice:int = obj["Rpt1ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpUnitPrice:int = obj["Rpt2ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpUnitPrice:int = obj["Rpt3ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the quote line, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.InDiscount:int = obj["InDiscount"]
      """  Reserved for future use  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  Reserved for future use  """  
      self.InExpectedRevenue:int = obj["InExpectedRevenue"]
      """  Reserved for future use  """  
      self.DocInExpectedRevenue:int = obj["DocInExpectedRevenue"]
      """  Reserved for future use  """  
      self.InListPrice:int = obj["InListPrice"]
      """  Reserved for future use  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  Reserved for future use  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExpUnitPrice:int = obj["InExpUnitPrice"]
      """  Reserved for future use  """  
      self.DocInExpUnitPrice:int = obj["DocInExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InExpectedRevenue:int = obj["Rpt1InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt2InExpectedRevenue:int = obj["Rpt2InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt3InExpectedRevenue:int = obj["Rpt3InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt1InExpUnitPrice:int = obj["Rpt1InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InExpUnitPrice:int = obj["Rpt2InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InExpUnitPrice:int = obj["Rpt3InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reserved for future use  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reserved for future use  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reserved for future use  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Reserved for future use  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reserved for future use  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.Rpt1WorstCsRevenue:int = obj["Rpt1WorstCsRevenue"]
      self.Rpt2WorstCsRevenue:int = obj["Rpt2WorstCsRevenue"]
      self.Rpt3WorstCsRevenue:int = obj["Rpt3WorstCsRevenue"]
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Rpt1BestCsRevenue:int = obj["Rpt1BestCsRevenue"]
      self.Rpt2BestCsRevenue:int = obj["Rpt2BestCsRevenue"]
      self.Rpt3BestCsRevenue:int = obj["Rpt3BestCsRevenue"]
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  Demand Contract Line  """  
      self.DemandHedSeq:int = obj["DemandHedSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence number to which this record is related.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote line is linked to an inter-company PO line.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the quote line can be changed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """  Indicates that the line item was closed before any shipments were made against it.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.EstimateGUID:str = obj["EstimateGUID"]
      """  EstimateGUID  """  
      self.EstimateUserID:str = obj["EstimateUserID"]
      """  EstimateUserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.BaseExtPrice:int = obj["BaseExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.BasePotential:int = obj["BasePotential"]
      self.DocPotential:int = obj["DocPotential"]
      self.BaseMiscAmt:int = obj["BaseMiscAmt"]
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      self.Configured:str = obj["Configured"]
      """  Indicates whether the part is/can be configured  """  
      self.RefreshQty:bool = obj["RefreshQty"]
      """  Indicates whether to Refresh the QuoteQty table  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.CheckPartDescription:bool = obj["CheckPartDescription"]
      """  If yes, then a new non-standard part was added with no description and validation needs to be run again  """  
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Delimited list of Available Price Lists  """  
      self.OrderWorthy:bool = obj["OrderWorthy"]
      """  If yes, the line will be copied to the Order  """  
      self.LineStatus:str = obj["LineStatus"]
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.ShipByDate:str = obj["ShipByDate"]
      self.OrderUM:str = obj["OrderUM"]
      self.OrderUnitPrice:int = obj["OrderUnitPrice"]
      self.DocOrderUnitPrice:int = obj["DocOrderUnitPrice"]
      self.CodePLM:bool = obj["CodePLM"]
      """  PLM Flag  """  
      self.EnablePLM:bool = obj["EnablePLM"]
      """  Flag indicating whether to enable CodePLM or not  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  The description for Kit Flag. "P" = Parent, "C" = Component.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.Rpt1BasePotential:int = obj["Rpt1BasePotential"]
      self.Rpt2BasePotential:int = obj["Rpt2BasePotential"]
      self.Rpt3BasePotential:int = obj["Rpt3BasePotential"]
      self.Rpt1BaseExtPrice:int = obj["Rpt1BaseExtPrice"]
      self.Rpt2BaseExtPrice:int = obj["Rpt2BaseExtPrice"]
      self.Rpt3BaseExtPrice:int = obj["Rpt3BaseExtPrice"]
      self.Rpt1BaseMiscAmt:int = obj["Rpt1BaseMiscAmt"]
      self.Rpt2BaseMiscAmt:int = obj["Rpt2BaseMiscAmt"]
      self.Rpt3BaseMiscAmt:int = obj["Rpt3BaseMiscAmt"]
      self.Rpt1OrderUnitPrice:int = obj["Rpt1OrderUnitPrice"]
      self.Rpt2OrderUnitPrice:int = obj["Rpt2OrderUnitPrice"]
      self.Rpt3OrderUnitPrice:int = obj["Rpt3OrderUnitPrice"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableDiscounts:bool = obj["DisableDiscounts"]
      """  Indicates if the discount fields should be disabled for the current quote line detail.  """  
      self.DspExpectedUM:str = obj["DspExpectedUM"]
      """  Used to displayed UOM for expected quantity for detail line  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      """  Description  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
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
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      """  Description of the price list.  """  
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      """  Price Group description  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      """  Description of the sales category.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      """  Description of the territory.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  The date when this quote expires.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default  """  
      self.DspExpUnitPrice:int = obj["DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.DocDspExpUnitPrice:int = obj["DocDspExpUnitPrice"]
      """  Display Document unit price based on the expected quantity.  """  
      self.Rpt1DspExpUnitPrice:int = obj["Rpt1DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt2DspExpUnitPrice:int = obj["Rpt2DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt3DspExpUnitPrice:int = obj["Rpt3DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlListTableset:
   def __init__(self, obj):
      self.QuoteDtlList:list[Erp_Tablesets_QuoteDtlListRow] = obj["QuoteDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuoteDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of linked project.  Must exist on the Project table. Can be blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MakeDirect:bool = obj["MakeDirect"]
      """  To indicate whether or not the line is make direct  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Must exist on ProjPhase table if entered  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Non-blank value prevents taxes from being calculated for this line item  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpectedRevenue:int = obj["Rpt1ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpectedRevenue:int = obj["Rpt2ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpectedRevenue:int = obj["Rpt3ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpUnitPrice:int = obj["Rpt1ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpUnitPrice:int = obj["Rpt2ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpUnitPrice:int = obj["Rpt3ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the quote line, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.InDiscount:int = obj["InDiscount"]
      """  Reserved for future use  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  Reserved for future use  """  
      self.InExpectedRevenue:int = obj["InExpectedRevenue"]
      """  Reserved for future use  """  
      self.DocInExpectedRevenue:int = obj["DocInExpectedRevenue"]
      """  Reserved for future use  """  
      self.InListPrice:int = obj["InListPrice"]
      """  Reserved for future use  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  Reserved for future use  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExpUnitPrice:int = obj["InExpUnitPrice"]
      """  Reserved for future use  """  
      self.DocInExpUnitPrice:int = obj["DocInExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InExpectedRevenue:int = obj["Rpt1InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt2InExpectedRevenue:int = obj["Rpt2InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt3InExpectedRevenue:int = obj["Rpt3InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt1InExpUnitPrice:int = obj["Rpt1InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InExpUnitPrice:int = obj["Rpt2InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InExpUnitPrice:int = obj["Rpt3InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reserved for future use  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reserved for future use  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reserved for future use  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Reserved for future use  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reserved for future use  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.Rpt1WorstCsRevenue:int = obj["Rpt1WorstCsRevenue"]
      self.Rpt2WorstCsRevenue:int = obj["Rpt2WorstCsRevenue"]
      self.Rpt3WorstCsRevenue:int = obj["Rpt3WorstCsRevenue"]
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Rpt1BestCsRevenue:int = obj["Rpt1BestCsRevenue"]
      self.Rpt2BestCsRevenue:int = obj["Rpt2BestCsRevenue"]
      self.Rpt3BestCsRevenue:int = obj["Rpt3BestCsRevenue"]
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  Demand Contract Line  """  
      self.DemandHedSeq:int = obj["DemandHedSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence number to which this record is related.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote line is linked to an inter-company PO line.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the quote line can be changed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """  Indicates that the line item was closed before any shipments were made against it.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.EstimateGUID:str = obj["EstimateGUID"]
      """  EstimateGUID  """  
      self.RFQCurrBaseEst:str = obj["RFQCurrBaseEst"]
      """  RFQCurrBaseEst  """  
      self.RFQTemplate:str = obj["RFQTemplate"]
      """  RFQTemplate  """  
      self.CreateEstimate:bool = obj["CreateEstimate"]
      """  CreateEstimate  """  
      self.Rating:str = obj["Rating"]
      """  Rating  """  
      self.EstimateUserID:str = obj["EstimateUserID"]
      """  EstimateUserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCQuoteLine:int = obj["ECCQuoteLine"]
      """  ECC Quote Line  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Ref  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  Indicates if no tax recalculation by the system is supposed to be done.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.ExternalCRMQuoteLineID:str = obj["ExternalCRMQuoteLineID"]
      """  This field holds the id of this quote line in the External CRM  """  
      self.ReturnLineType:str = obj["ReturnLineType"]
      """  Type for returns: Blank, (C)redit or (S)tandard  """  
      self.MSRP:int = obj["MSRP"]
      """  Base price before any price breaks and discounts  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1MSRP:int = obj["Rpt1MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt2MSRP:int = obj["Rpt2MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt3MSRP:int = obj["Rpt3MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  Distributor end customer price.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1EndCustomerPrice:int = obj["Rpt1EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt2EndCustomerPrice:int = obj["Rpt2EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt3EndCustomerPrice:int = obj["Rpt3EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  Mark For ShipToNum  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Contact Name  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1PromotionalPrice:int = obj["Rpt1PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt2PromotionalPrice:int = obj["Rpt2PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt3PromotionalPrice:int = obj["Rpt3PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseExtPrice:int = obj["BaseExtPrice"]
      self.BaseMiscAmt:int = obj["BaseMiscAmt"]
      self.BasePotential:int = obj["BasePotential"]
      self.CheckPartDescription:bool = obj["CheckPartDescription"]
      """  If yes, then a new non-standard part was added with no description and validation needs to be run again  """  
      self.CodePLM:bool = obj["CodePLM"]
      """  PLM Flag  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default  """  
      self.ConfigType:str = obj["ConfigType"]
      self.Configured:str = obj["Configured"]
      """  Indicates whether the part is/can be configured  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from QuoteHed  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete.  """  
      self.DisableDiscounts:bool = obj["DisableDiscounts"]
      """  Indicates if the discount fields should be disabled for the current quote line detail.  """  
      self.DocDspDiscount:int = obj["DocDspDiscount"]
      """  Display a Document  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDspExpUnitPrice:int = obj["DocDspExpUnitPrice"]
      """  Display Document unit price based on the expected quantity.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      self.DocOrderUnitPrice:int = obj["DocOrderUnitPrice"]
      self.DocPotential:int = obj["DocPotential"]
      self.DocTotalPrice:int = obj["DocTotalPrice"]
      self.DocTotalQuote:int = obj["DocTotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DspExpectedUM:str = obj["DspExpectedUM"]
      """  Used to displayed UOM for expected quantity for detail line  """  
      self.EnableRenewalNbr:bool = obj["EnableRenewalNbr"]
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  The date when this quote expires.  """  
      self.HasComplement:bool = obj["HasComplement"]
      """  Indicates whether the part has at least one Complement  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.HasCreditMemo:bool = obj["HasCreditMemo"]
      """  Indicates if this Quote line has an associated credit memo (only for dealer portal)  """  
      self.HasDowngrade:bool = obj["HasDowngrade"]
      """  Indicates whether the part has at least one Downgrade  """  
      self.HasSubstitute:bool = obj["HasSubstitute"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.HasUpgrade:bool = obj["HasUpgrade"]
      """  Indicates whether the part has at least one Upgrade  """  
      self.KitChangeParms:bool = obj["KitChangeParms"]
      """  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.KitFlagDescription:str = obj["KitFlagDescription"]
      """  The description for Kit Flag. "P" = Parent, "C" = Component.  """  
      self.KitOrderQtyUOM:str = obj["KitOrderQtyUOM"]
      self.LineStatus:str = obj["LineStatus"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.OrderUM:str = obj["OrderUM"]
      self.OrderUnitPrice:int = obj["OrderUnitPrice"]
      self.OrderWorthy:bool = obj["OrderWorthy"]
      """  If yes, the line will be copied to the Order  """  
      self.PartExists:bool = obj["PartExists"]
      """  Internal flag to identify if the Part is an Inventory Part.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QuantityToOrder:int = obj["QuantityToOrder"]
      self.RefreshQty:bool = obj["RefreshQty"]
      """  Indicates whether to Refresh the QuoteQty table  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The flag to indicate if the logic should delete quote line related manually added and manual taxes if the user populates Tax Exempt field previously blank  """  
      self.Rpt1BaseExtPrice:int = obj["Rpt1BaseExtPrice"]
      self.Rpt1BaseMiscAmt:int = obj["Rpt1BaseMiscAmt"]
      self.Rpt1BasePotential:int = obj["Rpt1BasePotential"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt1DspExpUnitPrice:int = obj["Rpt1DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt1OrderUnitPrice:int = obj["Rpt1OrderUnitPrice"]
      self.Rpt1TotalPrice:int = obj["Rpt1TotalPrice"]
      self.Rpt1TotalQuote:int = obj["Rpt1TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt2BaseExtPrice:int = obj["Rpt2BaseExtPrice"]
      self.Rpt2BaseMiscAmt:int = obj["Rpt2BaseMiscAmt"]
      self.Rpt2BasePotential:int = obj["Rpt2BasePotential"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt2DspExpUnitPrice:int = obj["Rpt2DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt2OrderUnitPrice:int = obj["Rpt2OrderUnitPrice"]
      self.Rpt2TotalPrice:int = obj["Rpt2TotalPrice"]
      self.Rpt2TotalQuote:int = obj["Rpt2TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Rpt3BaseExtPrice:int = obj["Rpt3BaseExtPrice"]
      self.Rpt3BaseMiscAmt:int = obj["Rpt3BaseMiscAmt"]
      self.Rpt3BasePotential:int = obj["Rpt3BasePotential"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      """  Display a  flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.Rpt3DspExpUnitPrice:int = obj["Rpt3DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.Rpt3OrderUnitPrice:int = obj["Rpt3OrderUnitPrice"]
      self.Rpt3TotalPrice:int = obj["Rpt3TotalPrice"]
      self.Rpt3TotalQuote:int = obj["Rpt3TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """  Total Withholding Tax Amount for the Quote Line  """  
      self.Selected:bool = obj["Selected"]
      """  Selected row  """  
      self.ShipByDate:str = obj["ShipByDate"]
      self.TotalPrice:int = obj["TotalPrice"]
      self.TotalQuote:int = obj["TotalQuote"]
      """   Total Quote which includes the total sum of potential, misc charges and taxas.
TotalQuote = Potential + Misc Charges + Tax  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """  Total Withholding Tax amount for the Quote Line  """  
      self.UpdateReq:bool = obj["UpdateReq"]
      """   Indicates that a QuoteAsm.QtyPer field was updated with out updating the RequiredQty field on the sub tables.
*** FUTURE USE  """  
      self.UseQuoteBOM:bool = obj["UseQuoteBOM"]
      """  Indicates that the Quote should be used as the BOM when creating a job for the linked order  """  
      self.AvailPriceLists:str = obj["AvailPriceLists"]
      """  Delimited list of Available Price Lists  """  
      self.DspExpUnitPrice:int = obj["DspExpUnitPrice"]
      """  Display unit price based on the expected quantity.  """  
      self.ECCLineCRQ:int = obj["ECCLineCRQ"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Allow enable/disable for the Dynamic Attributes button on a Quote Line  """  
      self.EnablePLM:bool = obj["EnablePLM"]
      """  Flag indicating whether to enable CodePLM or not  """  
      self.MarkForAddressFormatted:str = obj["MarkForAddressFormatted"]
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      self.LessDiscount:int = obj["LessDiscount"]
      """  The amount of discount for display  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  The amount of discount for display in Doc currency  """  
      self.Rpt1LessDiscount:int = obj["Rpt1LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt2LessDiscount:int = obj["Rpt2LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.Rpt3LessDiscount:int = obj["Rpt3LessDiscount"]
      """  The amount of discount for display in reporting currency  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      """   This flag indicates if taxes can be modified by user:
True: Taxes are from Tax Engine (Vantage). They can be adjusted/deleted.
False: Taxes are from TaxConnect. They cannot be adjusted/deleted.
AllowTaxCodeUpd depends on TaxConnectCalc value. If TaxConnectCalc is True, AllowTaxCodeUpd will be False. Otherwise, it will be True.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DiscBreakListCodeListDescription:str = obj["DiscBreakListCodeListDescription"]
      self.DiscBreakListCodeEndDate:str = obj["DiscBreakListCodeEndDate"]
      self.DiscBreakListCodeStartDate:str = obj["DiscBreakListCodeStartDate"]
      self.MFShipToNumInactive:bool = obj["MFShipToNumInactive"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.PartNumDefaultAttributeSetID:int = obj["PartNumDefaultAttributeSetID"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PriceBreakListDescription:str = obj["PriceBreakListDescription"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.QuoteNumInPrice:bool = obj["QuoteNumInPrice"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TaxRegionTaxConnectCalc:bool = obj["TaxRegionTaxConnectCalc"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuoteDtlSearchTableset:
   def __init__(self, obj):
      self.QuoteDtl:list[Erp_Tablesets_QuoteDtlRow] = obj["QuoteDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtQuoteDtlSearchTableset:
   def __init__(self, obj):
      self.QuoteDtl:list[Erp_Tablesets_QuoteDtlRow] = obj["QuoteDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   quoteNum
   quoteLine
   """  
   def __init__(self, obj):
      self.quoteNum:int = obj["quoteNum"]
      self.quoteLine:int = obj["quoteLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["returnObj"]
      pass

class GetListCustom_input:
   """ Required : 
   whereClauseQuoteDtl
   whereClauseQuoteHed
   whereClauseCustomer
   conclusion
   sortBy
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      """  The where clause to restrict data for QuoteDtl  """  
      self.whereClauseQuoteHed:str = obj["whereClauseQuoteHed"]
      """  The where clause to restrict data for QuoteHed  """  
      self.whereClauseCustomer:str = obj["whereClauseCustomer"]
      """  The where clause to restrict data for Customer  """  
      self.conclusion:str = obj["conclusion"]
      """  Won, NotWon, All  """  
      self.sortBy:str = obj["sortBy"]
      """  sortBy Selected  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adapter  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adapter  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteDtlListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuoteDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewQuoteDtl_input:
   """ Required : 
   ds
   quoteNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["ds"]
      self.quoteNum:int = obj["quoteNum"]
      pass

class GetNewQuoteDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseQuoteDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuoteDtl:str = obj["whereClauseQuoteDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtQuoteDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuoteDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuoteDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

