import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PODetailTrackerSearchSvc
# Description: PoDetail Tracker Search Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PODetailTrackerSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PODetailTrackerSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailTrackerSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches",headers=creds) as resp:
           return await resp.json()

async def post_PODetailTrackerSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailTrackerSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PODetailTrackerSearches_Company_PONUM_POLine(Company, PONUM, POLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PODetailTrackerSearch item
   Description: Calls GetByID to retrieve the PODetailTrackerSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailTrackerSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches(" + Company + "," + PONUM + "," + POLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PODetailTrackerSearches_Company_PONUM_POLine(Company, PONUM, POLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PODetailTrackerSearch for the service
   Description: Calls UpdateExt to update PODetailTrackerSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailTrackerSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches(" + Company + "," + PONUM + "," + POLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PODetailTrackerSearches_Company_PONUM_POLine(Company, PONUM, POLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PODetailTrackerSearch item
   Description: Call UpdateExt to delete PODetailTrackerSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailTrackerSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONUM: Desc: PONUM   Required: True
      :param POLine: Desc: POLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/PODetailTrackerSearches(" + Company + "," + PONUM + "," + POLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePODetail, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePODetail=" + whereClausePODetail
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(poNUM, poLine, epicorHeaders = None):
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
   params += "poNUM=" + poNUM
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "poLine=" + poLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsByVendorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsByVendorNum
   Description: Calls the normal GetRows method and then constructs a custom data set combining Job and Order fields for the supplier tracker.
   OperationID: GetRowsByVendorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPODetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPODetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailTrackerSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PODetailListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PODetailRow] = obj["value"]
      pass

class Erp_Tablesets_PODetailListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.AdvancePayBal:int = obj["AdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.DocAdvancePayBal:int = obj["DocAdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.DateChgReq:bool = obj["DateChgReq"]
      """  Indicates this line has a pending date change  """  
      self.QtyChgReq:bool = obj["QtyChgReq"]
      """  Indicates this line has a pending qty change  """  
      self.PartNumChgReq:str = obj["PartNumChgReq"]
      """  Requested pending partnumber change  """  
      self.RevisionNumChgReq:str = obj["RevisionNumChgReq"]
      """  Requested pending revision change  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  Date Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web" or "client"  """  
      self.PrcChgReq:int = obj["PrcChgReq"]
      """  Requested Price change.  SRM  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order line.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractActive:bool = obj["ContractActive"]
      """  Is this line active on the Contract Purchase Order?  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Quantity for this Contract Purchase Order Line.  """  
      self.ContractUnitCost:int = obj["ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line.  """  
      self.ContractDocUnitCost:int = obj["ContractDocUnitCost"]
      """  Document Unit Price for this Contract Purchase Order Line.  """  
      self.Rpt1AdvancePayBal:int = obj["Rpt1AdvancePayBal"]
      """  Advanced Payments Balance in Rpt1 currency.  """  
      self.Rpt2AdvancePayBal:int = obj["Rpt2AdvancePayBal"]
      """  Advanced Payments Balance in Rpt2 currency.  """  
      self.Rpt3AdvancePayBal:int = obj["Rpt3AdvancePayBal"]
      """  Advanced Payments Balance in Rpt3 currency.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt1 currency.  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt2 currency.  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt3 currency.  """  
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  Unit Of Measure of the ContractQty.  """  
      self.Rpt1ContractUnitCost:int = obj["Rpt1ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  """  
      self.Rpt2ContractUnitCost:int = obj["Rpt2ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  """  
      self.Rpt3ContractUnitCost:int = obj["Rpt3ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.VendorPartOpts:str = obj["VendorPartOpts"]
      """   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.MfgPartOpts:str = obj["MfgPartOpts"]
      """   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.SubPartOpts:str = obj["SubPartOpts"]
      """   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  """  
      self.MfgNum:int = obj["MfgNum"]
      """  Manufacturer Unique ID  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  Manufacturer's Part Number.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Substitute Part Number  """  
      self.SubPartType:str = obj["SubPartType"]
      """   Substitute Part Type
O = Original
S = Substitute  """  
      self.ConfigUnitCost:int = obj["ConfigUnitCost"]
      """   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitCost:int = obj["ConfigBaseUnitCost"]
      """  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.CalcPurchasingFactor:int = obj["CalcPurchasingFactor"]
      """  purchasing factor  """  
      self.CalcJobSeq:int = obj["CalcJobSeq"]
      self.CalcAssemblySeq:int = obj["CalcAssemblySeq"]
      self.CalcDueDate:str = obj["CalcDueDate"]
      self.CalcJobNum:str = obj["CalcJobNum"]
      self.CalcJobSeqType:str = obj["CalcJobSeqType"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.calcLeadTime:int = obj["calcLeadTime"]
      self.calcMinOrderQty:int = obj["calcMinOrderQty"]
      self.calcPartPUM:str = obj["calcPartPUM"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.CalcTranType:str = obj["CalcTranType"]
      self.CPFactor:int = obj["CPFactor"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.MultiRel:bool = obj["MultiRel"]
      self.CalcMfg:str = obj["CalcMfg"]
      self.CalcMfgPart:str = obj["CalcMfgPart"]
      self.PriceBrkBTNSensitive:bool = obj["PriceBrkBTNSensitive"]
      self.SetCheveron:bool = obj["SetCheveron"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.SubAvail:bool = obj["SubAvail"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  False if vendor or class requires inspection, otherwise true.  """  
      self.ExpChart:str = obj["ExpChart"]
      """  The Chart ID component of the default G/L account.  """  
      self.ExpDivision:str = obj["ExpDivision"]
      """  The Division Component of the default expence G/L account.  """  
      self.ExpGLDept:str = obj["ExpGLDept"]
      """  The Department component of the default G/L account.  """  
      self.ReferenceCode:str = obj["ReferenceCode"]
      """  Link to the related code in GlRefCod.RefCode  """  
      self.DispExpAccount:str = obj["DispExpAccount"]
      """  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  """  
      self.DispAcctDescription:str = obj["DispAcctDescription"]
      """  Display Account Description.  """  
      self.AskRefCode:bool = obj["AskRefCode"]
      """  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  Reference Code Description  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase Point used in the Supplier Tracker.  """  
      self.CalcPurchasingFactorDirection:str = obj["CalcPurchasingFactorDirection"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      self.DisablePartRevBtn:bool = obj["DisablePartRevBtn"]
      self.PORelOneOpenRelease:bool = obj["PORelOneOpenRelease"]
      """  True if there is only one release and it's open.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CalcMangCustNum:int = obj["CalcMangCustNum"]
      self.CalcMangCustID:str = obj["CalcMangCustID"]
      self.CalcMangCustName:str = obj["CalcMangCustName"]
      self.CostPerCodeContract:str = obj["CostPerCodeContract"]
      """  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Full description of the part class.  """  
      self.GlPurchPurchDesc:str = obj["GlPurchPurchDesc"]
      """  Description of the purchase type. Appears in drop-down lists for selection.  """  
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      """  User assigned Manufacturer ID  """  
      self.MfgNumName:str = obj["MfgNumName"]
      """  Manufacturer Name  """  
      self.PONUMShipName:str = obj["PONUMShipName"]
      """  defaults from the company file.  """  
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PODetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.AdvancePayBal:int = obj["AdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.DocAdvancePayBal:int = obj["DocAdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.DateChgReq:bool = obj["DateChgReq"]
      """  Indicates this line has a pending date change  """  
      self.QtyChgReq:bool = obj["QtyChgReq"]
      """  Indicates this line has a pending qty change  """  
      self.PartNumChgReq:str = obj["PartNumChgReq"]
      """  Requested pending partnumber change  """  
      self.RevisionNumChgReq:str = obj["RevisionNumChgReq"]
      """  Requested pending revision change  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  Date Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web" or "client"  """  
      self.PrcChgReq:int = obj["PrcChgReq"]
      """  Requested Price change.  SRM  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order line.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractActive:bool = obj["ContractActive"]
      """  Is this line active on the Contract Purchase Order?  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Quantity for this Contract Purchase Order Line.  """  
      self.ContractUnitCost:int = obj["ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line.  """  
      self.ContractDocUnitCost:int = obj["ContractDocUnitCost"]
      """  Document Unit Price for this Contract Purchase Order Line.  """  
      self.Rpt1AdvancePayBal:int = obj["Rpt1AdvancePayBal"]
      """  Advanced Payments Balance in Rpt1 currency.  """  
      self.Rpt2AdvancePayBal:int = obj["Rpt2AdvancePayBal"]
      """  Advanced Payments Balance in Rpt2 currency.  """  
      self.Rpt3AdvancePayBal:int = obj["Rpt3AdvancePayBal"]
      """  Advanced Payments Balance in Rpt3 currency.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt1 currency.  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt2 currency.  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt3 currency.  """  
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  Unit Of Measure of the ContractQty.  """  
      self.Rpt1ContractUnitCost:int = obj["Rpt1ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  """  
      self.Rpt2ContractUnitCost:int = obj["Rpt2ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  """  
      self.Rpt3ContractUnitCost:int = obj["Rpt3ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.VendorPartOpts:str = obj["VendorPartOpts"]
      """   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.MfgPartOpts:str = obj["MfgPartOpts"]
      """   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.SubPartOpts:str = obj["SubPartOpts"]
      """   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  """  
      self.MfgNum:int = obj["MfgNum"]
      """  Manufacturer Unique ID  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  Manufacturer's Part Number.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Substitute Part Number  """  
      self.SubPartType:str = obj["SubPartType"]
      """   Substitute Part Type
O = Original
S = Substitute  """  
      self.ConfigUnitCost:int = obj["ConfigUnitCost"]
      """   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitCost:int = obj["ConfigBaseUnitCost"]
      """  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.Per:str = obj["Per"]
      """  Per  """  
      self.MaintainPricingUnits:bool = obj["MaintainPricingUnits"]
      """  MaintainPricingUnits  """  
      self.OverrideConversion:bool = obj["OverrideConversion"]
      """  OverrideConversion  """  
      self.RowsManualFactor:bool = obj["RowsManualFactor"]
      """  RowsManualFactor  """  
      self.KeepRowsManualFactorTmp:bool = obj["KeepRowsManualFactorTmp"]
      """  KeepRowsManualFactorTmp  """  
      self.ShipToSupplierDate:str = obj["ShipToSupplierDate"]
      """  ShipToSupplierDate  """  
      self.Factor:int = obj["Factor"]
      """  Factor  """  
      self.PricingQty:int = obj["PricingQty"]
      """  PricingQty  """  
      self.PricingUnitPrice:int = obj["PricingUnitPrice"]
      """  PricingUnitPrice  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.DocPricingUnitPrice:int = obj["DocPricingUnitPrice"]
      """  DocPricingUnitPrice  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.OrigComment:str = obj["OrigComment"]
      """  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  """  
      self.SmartString:str = obj["SmartString"]
      """  SmartString  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  SmartStringProcessed  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.SelCurrPricingUnitPrice:int = obj["SelCurrPricingUnitPrice"]
      """  SelCurrPricingUnitPrice  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date and time that the record was last changed  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.InUnitCost:int = obj["InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in base currency.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in document currency.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.InAdvancePayBal:int = obj["InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in base currency.  """  
      self.DocInAdvancePayBal:int = obj["DocInAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in document currency.  """  
      self.Rpt1InAdvancePayBal:int = obj["Rpt1InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InAdvancePayBal:int = obj["Rpt2InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InAdvancePayBal:int = obj["Rpt3InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt3 currency.  """  
      self.InContractUnitCost:int = obj["InContractUnitCost"]
      """  Contract unit cost inclusive of tax in base currency.  """  
      self.DocInContractUnitCost:int = obj["DocInContractUnitCost"]
      """  Contract unit cost inclusive of tax in document currency.  """  
      self.Rpt1InContractUnitCost:int = obj["Rpt1InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InContractUnitCost:int = obj["Rpt2InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InContractUnitCost:int = obj["Rpt3InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt3 currency.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  """  
      self.DocMiscCost:int = obj["DocMiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  """  
      self.MiscCost:int = obj["MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  """  
      self.Rpt1MiscCost:int = obj["Rpt1MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  """  
      self.Rpt2MiscCost:int = obj["Rpt2MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  """  
      self.Rpt3MiscCost:int = obj["Rpt3MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.EDIAckCode:str = obj["EDIAckCode"]
      """  Acknowledge code received from EDI  """  
      self.EDIAckComment:str = obj["EDIAckComment"]
      """  Additional comments to send with Acknowledge  """  
      self.AskRefCode:bool = obj["AskRefCode"]
      """  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  """  
      self.CalcAssemblySeq:int = obj["CalcAssemblySeq"]
      self.CalcDocTotalCost:int = obj["CalcDocTotalCost"]
      self.CalcDueDate:str = obj["CalcDueDate"]
      self.CalcJobNum:str = obj["CalcJobNum"]
      self.CalcJobSeq:int = obj["CalcJobSeq"]
      self.CalcJobSeqType:str = obj["CalcJobSeqType"]
      self.calcLeadTime:int = obj["calcLeadTime"]
      self.CalcMangCustID:str = obj["CalcMangCustID"]
      self.CalcMangCustName:str = obj["CalcMangCustName"]
      self.CalcMangCustNum:int = obj["CalcMangCustNum"]
      self.CalcMfg:str = obj["CalcMfg"]
      self.CalcMfgPart:str = obj["CalcMfgPart"]
      self.calcMinOrderQty:int = obj["calcMinOrderQty"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.calcPartPUM:str = obj["calcPartPUM"]
      self.CalcPurchasingFactor:int = obj["CalcPurchasingFactor"]
      """  purchasing factor  """  
      self.CalcPurchasingFactorDirection:str = obj["CalcPurchasingFactorDirection"]
      self.CalcTotalCost:int = obj["CalcTotalCost"]
      self.CalcTranType:str = obj["CalcTranType"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.Configured:str = obj["Configured"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerCodeContract:str = obj["CostPerCodeContract"]
      """  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.CPFactor:int = obj["CPFactor"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DisablePartRevBtn:bool = obj["DisablePartRevBtn"]
      self.DispAcctDescription:str = obj["DispAcctDescription"]
      """  Display Account Description.  """  
      self.DispExpAccount:str = obj["DispExpAccount"]
      """  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  False if vendor or class requires inspection, otherwise true.  """  
      self.ExpChart:str = obj["ExpChart"]
      """  The Chart ID component of the default G/L account.  """  
      self.ExpDivision:str = obj["ExpDivision"]
      """  The Division Component of the default expence G/L account.  """  
      self.ExpGLDept:str = obj["ExpGLDept"]
      """  The Department component of the default G/L account.  """  
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.LinkedSOConfig:bool = obj["LinkedSOConfig"]
      self.MultiRel:bool = obj["MultiRel"]
      self.NonMasterPart:bool = obj["NonMasterPart"]
      self.OpCode:str = obj["OpCode"]
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.PORelOneOpenRelease:bool = obj["PORelOneOpenRelease"]
      """  True if there is only one release and it's open.  """  
      self.PriceBrkBTNSensitive:bool = obj["PriceBrkBTNSensitive"]
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  Reference Code Description  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.ReferenceCode:str = obj["ReferenceCode"]
      """  Link to the related code in GlRefCod.RefCode  """  
      self.Rpt1CalcTotalCost:int = obj["Rpt1CalcTotalCost"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      self.Rpt2CalcTotalCost:int = obj["Rpt2CalcTotalCost"]
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      self.Rpt3CalcTotalCost:int = obj["Rpt3CalcTotalCost"]
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      self.ScrUnitCost:int = obj["ScrUnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.SetCheveron:bool = obj["SetCheveron"]
      self.SubAvail:bool = obj["SubAvail"]
      self.UpdateRelRecords:bool = obj["UpdateRelRecords"]
      self.UpdateRelTaxable:bool = obj["UpdateRelTaxable"]
      """  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase Point used in the Supplier Tracker.  """  
      self.AllowPORecon:bool = obj["AllowPORecon"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.CalcJobMtlSeq:int = obj["CalcJobMtlSeq"]
      self.CalcJobOprSeq:int = obj["CalcJobOprSeq"]
      self.HasBuyToOrderRelease:bool = obj["HasBuyToOrderRelease"]
      """  Flag to indicate the current PO Line has at least one Buy To Order Release  """  
      self.LineAmtCalcd:bool = obj["LineAmtCalcd"]
      """  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassInactive:bool = obj["ClassInactive"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.GlPurchPurchDesc:str = obj["GlPurchPurchDesc"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PONUMCurrencyCode:str = obj["PONUMCurrencyCode"]
      self.PONUMOrderDate:str = obj["PONUMOrderDate"]
      self.PONUMInPrice:bool = obj["PONUMInPrice"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.DeliveryInstructions_c:str = obj["DeliveryInstructions_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   poNUM
   poLine
   """  
   def __init__(self, obj):
      self.poNUM:int = obj["poNUM"]
      self.poLine:int = obj["poLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PODetailListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.AdvancePayBal:int = obj["AdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.DocAdvancePayBal:int = obj["DocAdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.DateChgReq:bool = obj["DateChgReq"]
      """  Indicates this line has a pending date change  """  
      self.QtyChgReq:bool = obj["QtyChgReq"]
      """  Indicates this line has a pending qty change  """  
      self.PartNumChgReq:str = obj["PartNumChgReq"]
      """  Requested pending partnumber change  """  
      self.RevisionNumChgReq:str = obj["RevisionNumChgReq"]
      """  Requested pending revision change  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  Date Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web" or "client"  """  
      self.PrcChgReq:int = obj["PrcChgReq"]
      """  Requested Price change.  SRM  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order line.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractActive:bool = obj["ContractActive"]
      """  Is this line active on the Contract Purchase Order?  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Quantity for this Contract Purchase Order Line.  """  
      self.ContractUnitCost:int = obj["ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line.  """  
      self.ContractDocUnitCost:int = obj["ContractDocUnitCost"]
      """  Document Unit Price for this Contract Purchase Order Line.  """  
      self.Rpt1AdvancePayBal:int = obj["Rpt1AdvancePayBal"]
      """  Advanced Payments Balance in Rpt1 currency.  """  
      self.Rpt2AdvancePayBal:int = obj["Rpt2AdvancePayBal"]
      """  Advanced Payments Balance in Rpt2 currency.  """  
      self.Rpt3AdvancePayBal:int = obj["Rpt3AdvancePayBal"]
      """  Advanced Payments Balance in Rpt3 currency.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt1 currency.  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt2 currency.  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt3 currency.  """  
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  Unit Of Measure of the ContractQty.  """  
      self.Rpt1ContractUnitCost:int = obj["Rpt1ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  """  
      self.Rpt2ContractUnitCost:int = obj["Rpt2ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  """  
      self.Rpt3ContractUnitCost:int = obj["Rpt3ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.VendorPartOpts:str = obj["VendorPartOpts"]
      """   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.MfgPartOpts:str = obj["MfgPartOpts"]
      """   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.SubPartOpts:str = obj["SubPartOpts"]
      """   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  """  
      self.MfgNum:int = obj["MfgNum"]
      """  Manufacturer Unique ID  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  Manufacturer's Part Number.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Substitute Part Number  """  
      self.SubPartType:str = obj["SubPartType"]
      """   Substitute Part Type
O = Original
S = Substitute  """  
      self.ConfigUnitCost:int = obj["ConfigUnitCost"]
      """   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitCost:int = obj["ConfigBaseUnitCost"]
      """  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.CalcPurchasingFactor:int = obj["CalcPurchasingFactor"]
      """  purchasing factor  """  
      self.CalcJobSeq:int = obj["CalcJobSeq"]
      self.CalcAssemblySeq:int = obj["CalcAssemblySeq"]
      self.CalcDueDate:str = obj["CalcDueDate"]
      self.CalcJobNum:str = obj["CalcJobNum"]
      self.CalcJobSeqType:str = obj["CalcJobSeqType"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.calcLeadTime:int = obj["calcLeadTime"]
      self.calcMinOrderQty:int = obj["calcMinOrderQty"]
      self.calcPartPUM:str = obj["calcPartPUM"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.CalcTranType:str = obj["CalcTranType"]
      self.CPFactor:int = obj["CPFactor"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.MultiRel:bool = obj["MultiRel"]
      self.CalcMfg:str = obj["CalcMfg"]
      self.CalcMfgPart:str = obj["CalcMfgPart"]
      self.PriceBrkBTNSensitive:bool = obj["PriceBrkBTNSensitive"]
      self.SetCheveron:bool = obj["SetCheveron"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.SubAvail:bool = obj["SubAvail"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  False if vendor or class requires inspection, otherwise true.  """  
      self.ExpChart:str = obj["ExpChart"]
      """  The Chart ID component of the default G/L account.  """  
      self.ExpDivision:str = obj["ExpDivision"]
      """  The Division Component of the default expence G/L account.  """  
      self.ExpGLDept:str = obj["ExpGLDept"]
      """  The Department component of the default G/L account.  """  
      self.ReferenceCode:str = obj["ReferenceCode"]
      """  Link to the related code in GlRefCod.RefCode  """  
      self.DispExpAccount:str = obj["DispExpAccount"]
      """  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  """  
      self.DispAcctDescription:str = obj["DispAcctDescription"]
      """  Display Account Description.  """  
      self.AskRefCode:bool = obj["AskRefCode"]
      """  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  Reference Code Description  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase Point used in the Supplier Tracker.  """  
      self.CalcPurchasingFactorDirection:str = obj["CalcPurchasingFactorDirection"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      self.DisablePartRevBtn:bool = obj["DisablePartRevBtn"]
      self.PORelOneOpenRelease:bool = obj["PORelOneOpenRelease"]
      """  True if there is only one release and it's open.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CalcMangCustNum:int = obj["CalcMangCustNum"]
      self.CalcMangCustID:str = obj["CalcMangCustID"]
      self.CalcMangCustName:str = obj["CalcMangCustName"]
      self.CostPerCodeContract:str = obj["CostPerCodeContract"]
      """  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Full description of the part class.  """  
      self.GlPurchPurchDesc:str = obj["GlPurchPurchDesc"]
      """  Description of the purchase type. Appears in drop-down lists for selection.  """  
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      """  User assigned Manufacturer ID  """  
      self.MfgNumName:str = obj["MfgNumName"]
      """  Manufacturer Name  """  
      self.PONUMShipName:str = obj["PONUMShipName"]
      """  defaults from the company file.  """  
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PODetailListTableset:
   def __init__(self, obj):
      self.PODetailList:list[Erp_Tablesets_PODetailListRow] = obj["PODetailList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PODetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.PUM:str = obj["PUM"]
      """  Purchasing UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  """  
      self.ClassID:str = obj["ClassID"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.AdvancePayBal:int = obj["AdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.DocAdvancePayBal:int = obj["DocAdvancePayBal"]
      """  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.DateChgReq:bool = obj["DateChgReq"]
      """  Indicates this line has a pending date change  """  
      self.QtyChgReq:bool = obj["QtyChgReq"]
      """  Indicates this line has a pending qty change  """  
      self.PartNumChgReq:str = obj["PartNumChgReq"]
      """  Requested pending partnumber change  """  
      self.RevisionNumChgReq:str = obj["RevisionNumChgReq"]
      """  Requested pending revision change  """  
      self.ConfirmDate:str = obj["ConfirmDate"]
      """  Date Supplier Confirmed the PO  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web" or "client"  """  
      self.PrcChgReq:int = obj["PrcChgReq"]
      """  Requested Price change.  SRM  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order line.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.ContractActive:bool = obj["ContractActive"]
      """  Is this line active on the Contract Purchase Order?  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Quantity for this Contract Purchase Order Line.  """  
      self.ContractUnitCost:int = obj["ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line.  """  
      self.ContractDocUnitCost:int = obj["ContractDocUnitCost"]
      """  Document Unit Price for this Contract Purchase Order Line.  """  
      self.Rpt1AdvancePayBal:int = obj["Rpt1AdvancePayBal"]
      """  Advanced Payments Balance in Rpt1 currency.  """  
      self.Rpt2AdvancePayBal:int = obj["Rpt2AdvancePayBal"]
      """  Advanced Payments Balance in Rpt2 currency.  """  
      self.Rpt3AdvancePayBal:int = obj["Rpt3AdvancePayBal"]
      """  Advanced Payments Balance in Rpt3 currency.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt1 currency.  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt2 currency.  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Unit price in the vendors unit of measure and Rpt3 currency.  """  
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  Unit Of Measure of the ContractQty.  """  
      self.Rpt1ContractUnitCost:int = obj["Rpt1ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  """  
      self.Rpt2ContractUnitCost:int = obj["Rpt2ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  """  
      self.Rpt3ContractUnitCost:int = obj["Rpt3ContractUnitCost"]
      """  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.VendorPartOpts:str = obj["VendorPartOpts"]
      """   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.MfgPartOpts:str = obj["MfgPartOpts"]
      """   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  """  
      self.SubPartOpts:str = obj["SubPartOpts"]
      """   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  """  
      self.MfgNum:int = obj["MfgNum"]
      """  Manufacturer Unique ID  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  Manufacturer's Part Number.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Substitute Part Number  """  
      self.SubPartType:str = obj["SubPartType"]
      """   Substitute Part Type
O = Original
S = Substitute  """  
      self.ConfigUnitCost:int = obj["ConfigUnitCost"]
      """   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitCost:int = obj["ConfigBaseUnitCost"]
      """  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.ConvOverRide:bool = obj["ConvOverRide"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.Direction:str = obj["Direction"]
      """  Direction  """  
      self.Per:str = obj["Per"]
      """  Per  """  
      self.MaintainPricingUnits:bool = obj["MaintainPricingUnits"]
      """  MaintainPricingUnits  """  
      self.OverrideConversion:bool = obj["OverrideConversion"]
      """  OverrideConversion  """  
      self.RowsManualFactor:bool = obj["RowsManualFactor"]
      """  RowsManualFactor  """  
      self.KeepRowsManualFactorTmp:bool = obj["KeepRowsManualFactorTmp"]
      """  KeepRowsManualFactorTmp  """  
      self.ShipToSupplierDate:str = obj["ShipToSupplierDate"]
      """  ShipToSupplierDate  """  
      self.Factor:int = obj["Factor"]
      """  Factor  """  
      self.PricingQty:int = obj["PricingQty"]
      """  PricingQty  """  
      self.PricingUnitPrice:int = obj["PricingUnitPrice"]
      """  PricingUnitPrice  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.DocPricingUnitPrice:int = obj["DocPricingUnitPrice"]
      """  DocPricingUnitPrice  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.OrigComment:str = obj["OrigComment"]
      """  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  """  
      self.SmartString:str = obj["SmartString"]
      """  SmartString  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  SmartStringProcessed  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.SelCurrPricingUnitPrice:int = obj["SelCurrPricingUnitPrice"]
      """  SelCurrPricingUnitPrice  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date and time that the record was last changed  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  """  
      self.InUnitCost:int = obj["InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in base currency.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in document currency.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  """  
      self.InAdvancePayBal:int = obj["InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in base currency.  """  
      self.DocInAdvancePayBal:int = obj["DocInAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in document currency.  """  
      self.Rpt1InAdvancePayBal:int = obj["Rpt1InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InAdvancePayBal:int = obj["Rpt2InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InAdvancePayBal:int = obj["Rpt3InAdvancePayBal"]
      """  Advanced Payments Balance inclusive of tax in Rpt3 currency.  """  
      self.InContractUnitCost:int = obj["InContractUnitCost"]
      """  Contract unit cost inclusive of tax in base currency.  """  
      self.DocInContractUnitCost:int = obj["DocInContractUnitCost"]
      """  Contract unit cost inclusive of tax in document currency.  """  
      self.Rpt1InContractUnitCost:int = obj["Rpt1InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt1 currency.  """  
      self.Rpt2InContractUnitCost:int = obj["Rpt2InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt2 currency.  """  
      self.Rpt3InContractUnitCost:int = obj["Rpt3InContractUnitCost"]
      """  Contract unit cost inclusive of tax in Rpt3 currency.  """  
      self.DocExtCost:int = obj["DocExtCost"]
      """  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  """  
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      """  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  """  
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      """  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  """  
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      """  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  """  
      self.DocMiscCost:int = obj["DocMiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  """  
      self.MiscCost:int = obj["MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  """  
      self.Rpt1MiscCost:int = obj["Rpt1MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  """  
      self.Rpt2MiscCost:int = obj["Rpt2MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  """  
      self.Rpt3MiscCost:int = obj["Rpt3MiscCost"]
      """  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.EDIAckCode:str = obj["EDIAckCode"]
      """  Acknowledge code received from EDI  """  
      self.EDIAckComment:str = obj["EDIAckComment"]
      """  Additional comments to send with Acknowledge  """  
      self.AskRefCode:bool = obj["AskRefCode"]
      """  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  """  
      self.CalcAssemblySeq:int = obj["CalcAssemblySeq"]
      self.CalcDocTotalCost:int = obj["CalcDocTotalCost"]
      self.CalcDueDate:str = obj["CalcDueDate"]
      self.CalcJobNum:str = obj["CalcJobNum"]
      self.CalcJobSeq:int = obj["CalcJobSeq"]
      self.CalcJobSeqType:str = obj["CalcJobSeqType"]
      self.calcLeadTime:int = obj["calcLeadTime"]
      self.CalcMangCustID:str = obj["CalcMangCustID"]
      self.CalcMangCustName:str = obj["CalcMangCustName"]
      self.CalcMangCustNum:int = obj["CalcMangCustNum"]
      self.CalcMfg:str = obj["CalcMfg"]
      self.CalcMfgPart:str = obj["CalcMfgPart"]
      self.calcMinOrderQty:int = obj["calcMinOrderQty"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.calcPartPUM:str = obj["calcPartPUM"]
      self.CalcPurchasingFactor:int = obj["CalcPurchasingFactor"]
      """  purchasing factor  """  
      self.CalcPurchasingFactorDirection:str = obj["CalcPurchasingFactorDirection"]
      self.CalcTotalCost:int = obj["CalcTotalCost"]
      self.CalcTranType:str = obj["CalcTranType"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.Configured:str = obj["Configured"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerCodeContract:str = obj["CostPerCodeContract"]
      """  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.CPFactor:int = obj["CPFactor"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DisablePartRevBtn:bool = obj["DisablePartRevBtn"]
      self.DispAcctDescription:str = obj["DispAcctDescription"]
      """  Display Account Description.  """  
      self.DispExpAccount:str = obj["DispExpAccount"]
      """  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  False if vendor or class requires inspection, otherwise true.  """  
      self.ExpChart:str = obj["ExpChart"]
      """  The Chart ID component of the default G/L account.  """  
      self.ExpDivision:str = obj["ExpDivision"]
      """  The Division Component of the default expence G/L account.  """  
      self.ExpGLDept:str = obj["ExpGLDept"]
      """  The Department component of the default G/L account.  """  
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.LinkedSOConfig:bool = obj["LinkedSOConfig"]
      self.MultiRel:bool = obj["MultiRel"]
      self.NonMasterPart:bool = obj["NonMasterPart"]
      self.OpCode:str = obj["OpCode"]
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.PORelOneOpenRelease:bool = obj["PORelOneOpenRelease"]
      """  True if there is only one release and it's open.  """  
      self.PriceBrkBTNSensitive:bool = obj["PriceBrkBTNSensitive"]
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  Reference Code Description  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Reference Code Status  """  
      self.ReferenceCode:str = obj["ReferenceCode"]
      """  Link to the related code in GlRefCod.RefCode  """  
      self.Rpt1CalcTotalCost:int = obj["Rpt1CalcTotalCost"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      self.Rpt2CalcTotalCost:int = obj["Rpt2CalcTotalCost"]
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      self.Rpt3CalcTotalCost:int = obj["Rpt3CalcTotalCost"]
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      self.ScrUnitCost:int = obj["ScrUnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.SetCheveron:bool = obj["SetCheveron"]
      self.SubAvail:bool = obj["SubAvail"]
      self.UpdateRelRecords:bool = obj["UpdateRelRecords"]
      self.UpdateRelTaxable:bool = obj["UpdateRelTaxable"]
      """  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase Point used in the Supplier Tracker.  """  
      self.AllowPORecon:bool = obj["AllowPORecon"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.CalcJobMtlSeq:int = obj["CalcJobMtlSeq"]
      self.CalcJobOprSeq:int = obj["CalcJobOprSeq"]
      self.HasBuyToOrderRelease:bool = obj["HasBuyToOrderRelease"]
      """  Flag to indicate the current PO Line has at least one Buy To Order Release  """  
      self.LineAmtCalcd:bool = obj["LineAmtCalcd"]
      """  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassInactive:bool = obj["ClassInactive"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.GlPurchPurchDesc:str = obj["GlPurchPurchDesc"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PONUMCurrencyCode:str = obj["PONUMCurrencyCode"]
      self.PONUMOrderDate:str = obj["PONUMOrderDate"]
      self.PONUMInPrice:bool = obj["PONUMInPrice"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.DeliveryInstructions_c:str = obj["DeliveryInstructions_c"]
      pass

class Erp_Tablesets_PODetailTrackerSearchTableset:
   def __init__(self, obj):
      self.PODetail:list[Erp_Tablesets_PODetailRow] = obj["PODetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPODetailTrackerSearchTableset:
   def __init__(self, obj):
      self.PODetail:list[Erp_Tablesets_PODetailRow] = obj["PODetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   poNUM
   poLine
   """  
   def __init__(self, obj):
      self.poNUM:int = obj["poNUM"]
      self.poLine:int = obj["poLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PODetailListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPODetail_input:
   """ Required : 
   ds
   poNUM
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["ds"]
      self.poNUM:int = obj["poNUM"]
      pass

class GetNewPODetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsByVendorNum_input:
   """ Required : 
   vendNum
   type
   fromOrderDate
   toOrderDate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.vendNum:int = obj["vendNum"]
      """  POHeader Vendor Number  """  
      self.type:str = obj["type"]
      """  Current tab selected: All / Open / Closed.  """  
      self.fromOrderDate:str = obj["fromOrderDate"]
      """  POHeader from OrderDate  """  
      self.toOrderDate:str = obj["toOrderDate"]
      """  POHeader to OrderDate  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsByVendorNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePODetail
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePODetail:str = obj["whereClausePODetail"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPODetailTrackerSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPODetailTrackerSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PODetailTrackerSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

