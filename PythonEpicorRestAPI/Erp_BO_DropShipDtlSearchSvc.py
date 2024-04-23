import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DropShipDtlSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DropShipDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DropShipDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DropShipDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_DropShipDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DropShipDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DropShipDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DropShipDtlSearch item
   Description: Calls GetByID to retrieve the DropShipDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DropShipDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DropShipDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DropShipDtlSearch for the service
   Description: Calls UpdateExt to update DropShipDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DropShipDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DropShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DropShipDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DropShipDtlSearch item
   Description: Call UpdateExt to delete DropShipDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DropShipDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/DropShipDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DropShipDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDropShipDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDropShipDtl=" + whereClauseDropShipDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, purPoint, packSlip, packLine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "purPoint=" + purPoint
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packSlip=" + packSlip
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packLine=" + packLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDropShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDropShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDropShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDropShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDropShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DropShipDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DropShipDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DropShipDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DropShipDtlRow] = obj["value"]
      pass

class Erp_Tablesets_DropShipDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order being drop shipped.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the purchase order being drop shipped.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The release number of the purchase order being drop shipped.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num defaulted from the PO release.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier's part num. Defaulted from the PO release.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Defaulted from the PO release.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Defaulted from the PO release.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Defaulted from the PO release.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Field that contains the customer's revision.  """  
      self.OurQty:int = obj["OurQty"]
      """  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Complete:bool = obj["Complete"]
      """  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  Invoice Number Line from corresponding APInvDtl record.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  Invoice Number from corresponding InvcHead record.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  Invoice Number Line from corresponding InvcDtl record.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment line that is complete and ready to be invoiced.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty comments.  """  
      self.CustNum:int = obj["CustNum"]
      """  Duplicated from DropShipHead.CustNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Duplicated from DropShipHead.ShipTotNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Duplicated from DropShipHead.ShipToCustNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RequestedQty:int = obj["RequestedQty"]
      self.ShippedToDateQty:int = obj["ShippedToDateQty"]
      self.ThisShipmentQty:int = obj["ThisShipmentQty"]
      self.RemainingQty:int = obj["RemainingQty"]
      self.RequestedQtyUOM:str = obj["RequestedQtyUOM"]
      self.ShippedToDateQtyUOM:str = obj["ShippedToDateQtyUOM"]
      self.ThisShipmentQtyUOM:str = obj["ThisShipmentQtyUOM"]
      self.RemainingQtyUOM:str = obj["RemainingQtyUOM"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.POComment:str = obj["POComment"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
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
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order being drop shipped.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the purchase order being drop shipped.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The release number of the purchase order being drop shipped.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num defaulted from the PO release.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier's part num. Defaulted from the PO release.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Defaulted from the PO release.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Defaulted from the PO release.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Defaulted from the PO release.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Field that contains the customer's revision.  """  
      self.OurQty:int = obj["OurQty"]
      """  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Complete:bool = obj["Complete"]
      """  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  Invoice Number Line from corresponding APInvDtl record.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  Invoice Number from corresponding InvcHead record.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  Invoice Number Line from corresponding InvcDtl record.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment line that is complete and ready to be invoiced.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty comments.  """  
      self.CustNum:int = obj["CustNum"]
      """  Duplicated from DropShipHead.CustNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Duplicated from DropShipHead.ShipTotNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Duplicated from DropShipHead.ShipToCustNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXTotalNetWeightKGM:int = obj["MXTotalNetWeightKGM"]
      """  Total Net Weight in kilograms  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.POComment:str = obj["POComment"]
      self.RemainingQty:int = obj["RemainingQty"]
      self.RemainingQtyUOM:str = obj["RemainingQtyUOM"]
      self.RequestedQty:int = obj["RequestedQty"]
      self.RequestedQtyUOM:str = obj["RequestedQtyUOM"]
      self.ShippedToDateQty:int = obj["ShippedToDateQty"]
      self.ShippedToDateQtyUOM:str = obj["ShippedToDateQtyUOM"]
      self.ThisShipmentQty:int = obj["ThisShipmentQty"]
      self.ThisShipmentQtyUOM:str = obj["ThisShipmentQtyUOM"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.BillToAddrFormatted:str = obj["BillToAddrFormatted"]
      """  The formatted bill to address  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DropShipDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order being drop shipped.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the purchase order being drop shipped.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The release number of the purchase order being drop shipped.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num defaulted from the PO release.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier's part num. Defaulted from the PO release.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Defaulted from the PO release.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Defaulted from the PO release.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Defaulted from the PO release.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Field that contains the customer's revision.  """  
      self.OurQty:int = obj["OurQty"]
      """  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Complete:bool = obj["Complete"]
      """  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  Invoice Number Line from corresponding APInvDtl record.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  Invoice Number from corresponding InvcHead record.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  Invoice Number Line from corresponding InvcDtl record.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment line that is complete and ready to be invoiced.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty comments.  """  
      self.CustNum:int = obj["CustNum"]
      """  Duplicated from DropShipHead.CustNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Duplicated from DropShipHead.ShipTotNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Duplicated from DropShipHead.ShipToCustNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RequestedQty:int = obj["RequestedQty"]
      self.ShippedToDateQty:int = obj["ShippedToDateQty"]
      self.ThisShipmentQty:int = obj["ThisShipmentQty"]
      self.RemainingQty:int = obj["RemainingQty"]
      self.RequestedQtyUOM:str = obj["RequestedQtyUOM"]
      self.ShippedToDateQtyUOM:str = obj["ShippedToDateQtyUOM"]
      self.ThisShipmentQtyUOM:str = obj["ThisShipmentQtyUOM"]
      self.RemainingQtyUOM:str = obj["RemainingQtyUOM"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.POComment:str = obj["POComment"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
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
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipDtlListTableset:
   def __init__(self, obj):
      self.DropShipDtlList:list[Erp_Tablesets_DropShipDtlListRow] = obj["DropShipDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DropShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The unique identifier for the drop shipment.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order being drop shipped.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the purchase order being drop shipped.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The release number of the purchase order being drop shipped.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num defaulted from the PO release.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier's part num. Defaulted from the PO release.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Defaulted from the PO release.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Defaulted from the PO release.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Defaulted from the PO release.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the users internal part number. Defaulted from the SO release.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Field that contains the customer's revision.  """  
      self.OurQty:int = obj["OurQty"]
      """  This field will be automatically defaulted to the remaining quantity to be drop shipped. Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Holds any comments about the order line being shipped. This gets duplicated from the OrderDtl.ShipComment.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  These comments will be copied into the Invoice detail.  """  
      self.HeaderShipComment:str = obj["HeaderShipComment"]
      """  Packing slip comments.  These are comments off of the invoice header.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Complete:bool = obj["Complete"]
      """  This flag will be automatically set if the remaining quantity to be drop shipped equals to zero and will be automatically turned off if the remaining quantity is greater than zero.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier that drops shipped the good from their inventory to our customer.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point ID.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Default can be obtained from PODetail.UnitCost.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  Item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the POdetail record.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related DropShipHead.ReceiptDate.  """  
      self.APInvoiced:bool = obj["APInvoiced"]
      """  A\P invoice entry sets this to "Yes" when the drop ship detail line is invoiced.  """  
      self.ARInvoiced:bool = obj["ARInvoiced"]
      """  A\R invoice entry sets this to "Yes" when the receipt detail line is invoiced.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  Invoice Number Line from corresponding APInvDtl record.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  Invoice Number from corresponding InvcHead record.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  Invoice Number Line from corresponding InvcDtl record.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.ReceivedShipped:bool = obj["ReceivedShipped"]
      """  Identifies a drop shipment line that is complete and ready to be invoiced.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty drop shipments.  Defaults as DropShipHead.ReceiptDate. But can be maintained from the Service Call center.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The # of days, months, years the Labor is covered by warranty  """  
      self.LaborExpiration:str = obj["LaborExpiration"]
      """  The date the Labor portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Whether the duration of warranty  is "Days"," Months"," years".  """  
      self.LastExpiration:str = obj["LastExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The # of days, months, years the material is covered by warranty  """  
      self.MaterialExpiration:str = obj["MaterialExpiration"]
      """  The date the material portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Whether the duration of warranty  is for "Days", " Months", "years".  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The # of days, months, years the Misc. Charges are covered by warranty  """  
      self.MiscExpiration:str = obj["MiscExpiration"]
      """  The date the Misc portion of the warranty expires.  Calculates from the effective date using the duration and modifier fields.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Whether the duration of warranty  is for "Days"," Months"," years".  """  
      self.Onsite:bool = obj["Onsite"]
      """  This warranty covers On site visits  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty comments.  """  
      self.CustNum:int = obj["CustNum"]
      """  Duplicated from DropShipHead.CustNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Duplicated from DropShipHead.ShipTotNum.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Duplicated from DropShipHead.ShipToCustNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXTotalNetWeightKGM:int = obj["MXTotalNetWeightKGM"]
      """  Total Net Weight in kilograms  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.POComment:str = obj["POComment"]
      self.RemainingQty:int = obj["RemainingQty"]
      self.RemainingQtyUOM:str = obj["RemainingQtyUOM"]
      self.RequestedQty:int = obj["RequestedQty"]
      self.RequestedQtyUOM:str = obj["RequestedQtyUOM"]
      self.ShippedToDateQty:int = obj["ShippedToDateQty"]
      self.ShippedToDateQtyUOM:str = obj["ShippedToDateQtyUOM"]
      self.ThisShipmentQty:int = obj["ThisShipmentQty"]
      self.ThisShipmentQtyUOM:str = obj["ThisShipmentQtyUOM"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.BillToAddrFormatted:str = obj["BillToAddrFormatted"]
      """  The formatted bill to address  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DropShipDtlSearchTableset:
   def __init__(self, obj):
      self.DropShipDtl:list[Erp_Tablesets_DropShipDtlRow] = obj["DropShipDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDropShipDtlSearchTableset:
   def __init__(self, obj):
      self.DropShipDtl:list[Erp_Tablesets_DropShipDtlRow] = obj["DropShipDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DropShipDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDropShipDtl_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewDropShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDropShipDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDropShipDtl:str = obj["whereClauseDropShipDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtDropShipDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDropShipDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DropShipDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

