import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RFQSuggSvc
# Description: Search engine for RFQ Entry, no maintenance allowed
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RFQSuggs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQSuggs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQSuggs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSuggRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs",headers=creds) as resp:
           return await resp.json()

async def post_RFQSuggs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQSuggs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQSuggs_Company_SugNum(Company, SugNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQSugg item
   Description: Calls GetByID to retrieve the RFQSugg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQSugg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs(" + Company + "," + SugNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQSuggs_Company_SugNum(Company, SugNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQSugg for the service
   Description: Calls UpdateExt to update RFQSugg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQSugg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQSuggRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs(" + Company + "," + SugNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQSuggs_Company_SugNum(Company, SugNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQSugg item
   Description: Call UpdateExt to delete RFQSugg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQSugg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SugNum: Desc: SugNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/RFQSuggs(" + Company + "," + SugNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQSuggListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRFQSugg, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRFQSugg=" + whereClauseRFQSugg
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sugNum, epicorHeaders = None):
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
   params += "sugNum=" + sugNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQSugg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQSugg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQSugg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQSugg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQSugg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQSuggSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQSuggListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQSuggRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQSuggRow] = obj["value"]
      pass

class Erp_Tablesets_RFQSuggListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.LineDesc:str = obj["LineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.IUM:str = obj["IUM"]
      """  Issue (our) unit of measure.  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal part number for this item.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  """  
      self.Class:str = obj["Class"]
      """  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  """  
      self.JobNum:str = obj["JobNum"]
      """  Related job number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Related Customer QuoteNum.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  """  
      self.ItemType:str = obj["ItemType"]
      """  Mtl = Material, Sub = Subcontract  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required.  """  
      self.ProcessRFQ:bool = obj["ProcessRFQ"]
      """  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Used to initialize RFQVend records  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  """  
      self.QtyList:str = obj["QtyList"]
      """  Delimited list of Quantity breaks to default the RFQQty table  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received.  Used when create PODetail records  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.GlbJobPartNum:str = obj["GlbJobPartNum"]
      """  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  """  
      self.GlbJobRevisionNum:str = obj["GlbJobRevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.GlbJobPartDescription:str = obj["GlbJobPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.GlbJobProdQty:int = obj["GlbJobProdQty"]
      """  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  """  
      self.GlbJobStartDate:str = obj["GlbJobStartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.GlbJobProjectID:str = obj["GlbJobProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.GlbQuoteDueDate:str = obj["GlbQuoteDueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.GlbQuoteQuoted:bool = obj["GlbQuoteQuoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.GlbQuoteDateQuoted:str = obj["GlbQuoteDateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.GlbQuoteExpirationDate:str = obj["GlbQuoteExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  """  
      self.GlbQuoteFollowUpDate:str = obj["GlbQuoteFollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.GlbQuoteReference:str = obj["GlbQuoteReference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.GlbQuoteName:str = obj["GlbQuoteName"]
      """  The full name of the customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Full description of the part class.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.vrClassDescription:str = obj["vrClassDescription"]
      """  Full description of the part class.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQSuggRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.LineDesc:str = obj["LineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.IUM:str = obj["IUM"]
      """  Issue (our) unit of measure.  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal part number for this item.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  """  
      self.Class:str = obj["Class"]
      """  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  """  
      self.JobNum:str = obj["JobNum"]
      """  Related job number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Related Customer QuoteNum.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  """  
      self.ItemType:str = obj["ItemType"]
      """  Mtl = Material, Sub = Subcontract  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required.  """  
      self.ProcessRFQ:bool = obj["ProcessRFQ"]
      """  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Used to initialize RFQVend records  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  """  
      self.QtyList:str = obj["QtyList"]
      """  Delimited list of Quantity breaks to default the RFQQty table  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received.  Used when create PODetail records  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.GlbJobPartNum:str = obj["GlbJobPartNum"]
      """  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  """  
      self.GlbJobRevisionNum:str = obj["GlbJobRevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.GlbJobPartDescription:str = obj["GlbJobPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.GlbJobProdQty:int = obj["GlbJobProdQty"]
      """  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  """  
      self.GlbJobStartDate:str = obj["GlbJobStartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.GlbJobProjectID:str = obj["GlbJobProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.GlbQuoteDueDate:str = obj["GlbQuoteDueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.GlbQuoteQuoted:bool = obj["GlbQuoteQuoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.GlbQuoteDateQuoted:str = obj["GlbQuoteDateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.GlbQuoteExpirationDate:str = obj["GlbQuoteExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  """  
      self.GlbQuoteFollowUpDate:str = obj["GlbQuoteFollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.GlbQuoteReference:str = obj["GlbQuoteReference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.GlbQuoteName:str = obj["GlbQuoteName"]
      """  The full name of the customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition Number from where the RFQ Suggestion comes from.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition Line from where the RFQ Suggestion comes from.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The Id that links to the Purchasing Agent master file.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.vrClassDescription:str = obj["vrClassDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sugNum
   """  
   def __init__(self, obj):
      self.sugNum:int = obj["sugNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RFQSuggListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.LineDesc:str = obj["LineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.IUM:str = obj["IUM"]
      """  Issue (our) unit of measure.  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal part number for this item.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  """  
      self.Class:str = obj["Class"]
      """  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  """  
      self.JobNum:str = obj["JobNum"]
      """  Related job number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Related Customer QuoteNum.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  """  
      self.ItemType:str = obj["ItemType"]
      """  Mtl = Material, Sub = Subcontract  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required.  """  
      self.ProcessRFQ:bool = obj["ProcessRFQ"]
      """  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Used to initialize RFQVend records  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  """  
      self.QtyList:str = obj["QtyList"]
      """  Delimited list of Quantity breaks to default the RFQQty table  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received.  Used when create PODetail records  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.GlbJobPartNum:str = obj["GlbJobPartNum"]
      """  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  """  
      self.GlbJobRevisionNum:str = obj["GlbJobRevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.GlbJobPartDescription:str = obj["GlbJobPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.GlbJobProdQty:int = obj["GlbJobProdQty"]
      """  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  """  
      self.GlbJobStartDate:str = obj["GlbJobStartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.GlbJobProjectID:str = obj["GlbJobProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.GlbQuoteDueDate:str = obj["GlbQuoteDueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.GlbQuoteQuoted:bool = obj["GlbQuoteQuoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.GlbQuoteDateQuoted:str = obj["GlbQuoteDateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.GlbQuoteExpirationDate:str = obj["GlbQuoteExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  """  
      self.GlbQuoteFollowUpDate:str = obj["GlbQuoteFollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.GlbQuoteReference:str = obj["GlbQuoteReference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.GlbQuoteName:str = obj["GlbQuoteName"]
      """  The full name of the customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Full description of the part class.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.vrClassDescription:str = obj["vrClassDescription"]
      """  Full description of the part class.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQSuggListTableset:
   def __init__(self, obj):
      self.RFQSuggList:list[Erp_Tablesets_RFQSuggListRow] = obj["RFQSuggList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RFQSuggRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  An integer used as a component of the unique index.  Assigned by the system as Last # on file + 1.  """  
      self.LineDesc:str = obj["LineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.IUM:str = obj["IUM"]
      """  Issue (our) unit of measure.  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal part number for this item.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the item. These will be printed on the RFQ. Defaults  from the related JobOper, JobMtl or Part file.  """  
      self.Class:str = obj["Class"]
      """  The foreign key to the PartClass file.  May be blank, if entered must be valid in PartClass file.  """  
      self.JobNum:str = obj["JobNum"]
      """  Related job number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Related Customer QuoteNum.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Job Seq of the requirement. Represents the operation sequence for subcontract operations, or the material sequence for materials.  """  
      self.ItemType:str = obj["ItemType"]
      """  Mtl = Material, Sub = Subcontract  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractor's or Job Material's VendorNum that ties back to the Vendor master file.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required.  """  
      self.ProcessRFQ:bool = obj["ProcessRFQ"]
      """  Used in RFQ Suggestions to determine if this suggestion should be processed into a RFQ.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Used to initialize RFQVend records  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  """  
      self.QtyList:str = obj["QtyList"]
      """  Delimited list of Quantity breaks to default the RFQQty table  """  
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      """  Global Suggestion flag.  Used in Consolidated Purchasing.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity from the source record (JobMtl/JobOper/QuoteMtl/QuoteOpr) used to create PORel.  Not user updatable.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received.  Used when create PODetail records  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.GlbJobPartNum:str = obj["GlbJobPartNum"]
      """  Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.  """  
      self.GlbJobRevisionNum:str = obj["GlbJobRevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.GlbJobPartDescription:str = obj["GlbJobPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.GlbJobProdQty:int = obj["GlbJobProdQty"]
      """  This field is not directly maintainable.  Instead it is a summary of the production quantities for sales orders (JobProd.ProdQty) plus the production quantity for inventory (JobHead.StockQty).  We keep a summary so that during detail entry we can easily calculate the exploded quantity.  It is also used to trigger a refresh of the detail exploded quantities when changes are made to the production quantity.  """  
      self.GlbJobStartDate:str = obj["GlbJobStartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.GlbJobProjectID:str = obj["GlbJobProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.GlbQuoteDueDate:str = obj["GlbQuoteDueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.GlbQuoteQuoted:bool = obj["GlbQuoteQuoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.GlbQuoteDateQuoted:str = obj["GlbQuoteDateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.GlbQuoteExpirationDate:str = obj["GlbQuoteExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.
This date is also used as part of the quote purging criteria testing.  """  
      self.GlbQuoteFollowUpDate:str = obj["GlbQuoteFollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.GlbQuoteReference:str = obj["GlbQuoteReference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.GlbQuoteName:str = obj["GlbQuoteName"]
      """  The full name of the customer.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition Number from where the RFQ Suggestion comes from.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition Line from where the RFQ Suggestion comes from.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The Id that links to the Purchasing Agent master file.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.vrClassDescription:str = obj["vrClassDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQSuggTableset:
   def __init__(self, obj):
      self.RFQSugg:list[Erp_Tablesets_RFQSuggRow] = obj["RFQSugg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRFQSuggTableset:
   def __init__(self, obj):
      self.RFQSugg:list[Erp_Tablesets_RFQSuggRow] = obj["RFQSugg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   sugNum
   """  
   def __init__(self, obj):
      self.sugNum:int = obj["sugNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQSuggTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQSuggTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQSuggTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQSuggListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRFQSugg_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQSuggTableset] = obj["ds"]
      pass

class GetNewRFQSugg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRFQSugg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRFQSugg:str = obj["whereClauseRFQSugg"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQSuggTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtRFQSuggTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRFQSuggTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQSuggTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQSuggTableset] = obj["ds"]
      pass

      """  output parameters  """  

