import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PODetailSearchSvc
# Description: PO Detail Search
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PoDetailSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePoHeaderSearch, whereClausePoDetailSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: Get_GetRows
      :param whereClausePoHeaderSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param whereClausePoDetailSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
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
   params += "whereClausePoHeaderSearch=" + whereClausePoHeaderSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePoDetailSearch=" + whereClausePoDetailSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClausePoHeaderSearch, whereClausePoDetailSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: Get_GetList
      :param whereClausePoHeaderSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param whereClausePoDetailSearch: Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      :param pageSize: Desc: The page size, used only for UI adaptor   Required: True
      :param absolutePage: Desc: The absolute page, used only for the UI adaptor   Required: True
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
   params += "whereClausePoHeaderSearch=" + whereClausePoHeaderSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePoDetailSearch=" + whereClausePoDetailSearch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListDropShipmentPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListDropShipmentPO
   Description: Get List of POs with DropShip = true for the corresponding OrderRel.
   OperationID: GetListDropShipmentPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListDropShipmentPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListDropShipmentPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListsFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListsFromSelectedKeys
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: GetListsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFromSelectedKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOLineSearchRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOLineSearchRows
   Description: Populates POLineSearchTableset for use in search
   OperationID: GetPOLineSearchRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOLineSearchRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOLineSearchRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PoDetailSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PoDetailSearchListRow] = obj["value"]
      pass

class Erp_Tablesets_PoDetailSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PoNum:int = obj["PoNum"]
      self.SupplierID:str = obj["SupplierID"]
      self.PurchasePoint:str = obj["PurchasePoint"]
      self.OrderDate:str = obj["OrderDate"]
      self.BuyerName:str = obj["BuyerName"]
      self.SupplierName:str = obj["SupplierName"]
      self.PartNum:str = obj["PartNum"]
      self.POLine:int = obj["POLine"]
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      self.FOB:str = obj["FOB"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.TermsCode:str = obj["TermsCode"]
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      self.ShipAddress2:str = obj["ShipAddress2"]
      self.ShipAddress3:str = obj["ShipAddress3"]
      self.ShipCity:str = obj["ShipCity"]
      self.ShipState:str = obj["ShipState"]
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the PO can be printed. Print functions are not available if this is = No.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  The BuyerID  that approved the PO. (See ApprovedDate for related info)  """  
      self.Approve:bool = obj["Approve"]
      """   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  """  
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.POHeaderRowIdent:str = obj["POHeaderRowIdent"]
      self.ContractQty:int = obj["ContractQty"]
      """  Contract Quantity of PO Detail  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  Contract End Date of POHeader  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  Contract Start Date of PO Header  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number from the supplier.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each, 
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PUM:str = obj["PUM"]
      """  Unit Of Measure  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.Confirmed:bool = obj["Confirmed"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PODetailSearchTableset:
   def __init__(self, obj):
      self.PoDetailSearch:list[Erp_Tablesets_PoDetailSearchRow] = obj["PoDetailSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_POLineSearchRow:
   def __init__(self, obj):
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.DueDate:str = obj["DueDate"]
      self.BuyerName:str = obj["BuyerName"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.IUM:str = obj["IUM"]
      self.XOrderQty:int = obj["XOrderQty"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POLineSearchTableset:
   def __init__(self, obj):
      self.POLineSearch:list[Erp_Tablesets_POLineSearchRow] = obj["POLineSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PoDetailSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PoNum:int = obj["PoNum"]
      self.SupplierID:str = obj["SupplierID"]
      self.PurchasePoint:str = obj["PurchasePoint"]
      self.OrderDate:str = obj["OrderDate"]
      self.BuyerName:str = obj["BuyerName"]
      self.SupplierName:str = obj["SupplierName"]
      self.PartNum:str = obj["PartNum"]
      self.POLine:int = obj["POLine"]
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      self.FOB:str = obj["FOB"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.TermsCode:str = obj["TermsCode"]
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      self.ShipAddress2:str = obj["ShipAddress2"]
      self.ShipAddress3:str = obj["ShipAddress3"]
      self.ShipCity:str = obj["ShipCity"]
      self.ShipState:str = obj["ShipState"]
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the PO can be printed. Print functions are not available if this is = No.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  The BuyerID  that approved the PO. (See ApprovedDate for related info)  """  
      self.Approve:bool = obj["Approve"]
      """   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  """  
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.POHeaderRowIdent:str = obj["POHeaderRowIdent"]
      self.ContractQty:int = obj["ContractQty"]
      """  Contract Quantity of PO Detail  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  Contract End Date of POHeader  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  Contract Start Date of PO Header  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number from the supplier.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each, 
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PUM:str = obj["PUM"]
      """  Unit Of Measure  """  
      self.BuyerIDName:str = obj["BuyerIDName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.Confirmed:bool = obj["Confirmed"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PoDetailSearchListTableset:
   def __init__(self, obj):
      self.PoDetailSearchList:list[Erp_Tablesets_PoDetailSearchListRow] = obj["PoDetailSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PoDetailSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PoNum:int = obj["PoNum"]
      self.SupplierID:str = obj["SupplierID"]
      self.PurchasePoint:str = obj["PurchasePoint"]
      self.OrderDate:str = obj["OrderDate"]
      self.BuyerName:str = obj["BuyerName"]
      self.SupplierName:str = obj["SupplierName"]
      self.PartNum:str = obj["PartNum"]
      self.POLine:int = obj["POLine"]
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  """  
      self.VoidOrder:bool = obj["VoidOrder"]
      """  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      self.FOB:str = obj["FOB"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.TermsCode:str = obj["TermsCode"]
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      self.ShipAddress2:str = obj["ShipAddress2"]
      self.ShipAddress3:str = obj["ShipAddress3"]
      self.ShipCity:str = obj["ShipCity"]
      self.ShipState:str = obj["ShipState"]
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Indicates if the PO can be printed. Print functions are not available if this is = No.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  The BuyerID  that approved the PO. (See ApprovedDate for related info)  """  
      self.Approve:bool = obj["Approve"]
      """   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  """  
      self.ApprovalStatus:str = obj["ApprovalStatus"]
      """   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.POHeaderRowIdent:str = obj["POHeaderRowIdent"]
      self.ContractQty:int = obj["ContractQty"]
      """  Contract Quantity of PO Detail  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  Contract End Date of POHeader  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  Contract Start Date of PO Header  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      """  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  """  
      self.IUM:str = obj["IUM"]
      """  (Our) Unit Of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Part number from the supplier.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each, 
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.PUM:str = obj["PUM"]
      """  Unit Of Measure  """  
      self.Confirmed:bool = obj["Confirmed"]
      self.SysRowID:str = obj["SysRowID"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetListDropShipmentPO_input:
   """ Required : 
   whereClausePoHeaderSearch
   whereClausePoDetailSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePoHeaderSearch:str = obj["whereClausePoHeaderSearch"]
      self.whereClausePoDetailSearch:str = obj["whereClausePoDetailSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListDropShipmentPO_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PoDetailSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClausePoHeaderSearch
   whereClausePoDetailSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePoHeaderSearch:str = obj["whereClausePoHeaderSearch"]
      """  The where clause to restrict data for  """  
      self.whereClausePoDetailSearch:str = obj["whereClausePoDetailSearch"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PoDetailSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListsFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PoDetailSearchListTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetListsFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PoDetailSearchListTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetPOLineSearchRows_input:
   """ Required : 
   startingPO
   partNum
   globalPO
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.startingPO:int = obj["startingPO"]
      """  The starting at PO Number entered on the search form  """  
      self.partNum:str = obj["partNum"]
      """  Part to search for  """  
      self.globalPO:bool = obj["globalPO"]
      """  Whether or not to look at consolidated POs  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetPOLineSearchRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POLineSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsFromSelectedKeys_input:
   """ Required : 
   ds
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PODetailSearchTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRowsFromSelectedKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PODetailSearchTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePoHeaderSearch
   whereClausePoDetailSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePoHeaderSearch:str = obj["whereClausePoHeaderSearch"]
      """  The where clause to restrict data for  """  
      self.whereClausePoDetailSearch:str = obj["whereClausePoDetailSearch"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PODetailSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

