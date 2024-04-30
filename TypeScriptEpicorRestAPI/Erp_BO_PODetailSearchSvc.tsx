import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PODetailSearchSvc
// Description: PO Detail Search
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PoDetailSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PoDetailSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PoDetailSearchListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetRows
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: Get_GetRows
      @param whereClausePoHeaderSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param whereClausePoDetailSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param pageSize Desc: The page size, used only for UI adaptor   Required: True
      @param absolutePage Desc: The absolute page, used only for the UI adaptor   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePoHeaderSearch:string, whereClausePoDetailSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePoHeaderSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePoHeaderSearch=" + whereClausePoHeaderSearch
   }
   if(typeof whereClausePoDetailSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePoDetailSearch=" + whereClausePoDetailSearch
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: Get_GetList
      @param whereClausePoHeaderSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param whereClausePoDetailSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param pageSize Desc: The page size, used only for UI adaptor   Required: True
      @param absolutePage Desc: The absolute page, used only for the UI adaptor   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClausePoHeaderSearch:string, whereClausePoDetailSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePoHeaderSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePoHeaderSearch=" + whereClausePoHeaderSearch
   }
   if(typeof whereClausePoDetailSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePoDetailSearch=" + whereClausePoDetailSearch
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListDropShipmentPO
   Description: Get List of POs with DropShip = true for the corresponding OrderRel.
   OperationID: GetListDropShipmentPO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListDropShipmentPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListDropShipmentPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListDropShipmentPO(requestBody:GetListDropShipmentPO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListDropShipmentPO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/GetListDropShipmentPO", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListDropShipmentPO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListsFromSelectedKeys
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: GetListsFromSelectedKeys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListsFromSelectedKeys(requestBody:GetListsFromSelectedKeys_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListsFromSelectedKeys_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/GetListsFromSelectedKeys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListsFromSelectedKeys_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the PoDetailSearch records which will be a subset
of the PoHeader records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PoDetailSearch) we need our own public method.
   OperationID: GetRowsFromSelectedKeys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromSelectedKeys(requestBody:GetRowsFromSelectedKeys_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsFromSelectedKeys_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/GetRowsFromSelectedKeys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsFromSelectedKeys_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOLineSearchRows
   Description: Populates POLineSearchTableset for use in search
   OperationID: GetPOLineSearchRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPOLineSearchRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOLineSearchRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOLineSearchRows(requestBody:GetPOLineSearchRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPOLineSearchRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PODetailSearchSvc/GetPOLineSearchRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPOLineSearchRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PoDetailSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PoDetailSearchListRow,
}

export interface Erp_Tablesets_PoDetailSearchListRow{
   "Company":string,
   "PoNum":number,
   "SupplierID":string,
   "PurchasePoint":string,
   "OrderDate":string,
   "BuyerName":string,
   "SupplierName":string,
   "PartNum":string,
   "POLine":number,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  */  
   "OpenOrder":boolean,
      /**  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  */  
   "VoidOrder":boolean,
   "EntryPerson":string,
   "FOB":string,
   "ShipViaCode":string,
   "TermsCode":string,
      /**  defaults from the company file.  */  
   "ShipName":string,
   "ShipAddress1":string,
   "ShipAddress2":string,
   "ShipAddress3":string,
   "ShipCity":string,
   "ShipState":string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   "ShipCountry":string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   "OrderHeld":boolean,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "ShipToConName":string,
      /**  Indicates if the PO can be printed. Print functions are not available if this is = No.  */  
   "ReadyToPrint":boolean,
      /**  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  */  
   "ApprovedDate":string,
      /**  The BuyerID  that approved the PO. (See ApprovedDate for related info)  */  
   "ApprovedBy":string,
      /**   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  */  
   "Approve":boolean,
      /**   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  */  
   "ApprovalStatus":string,
   "VendorVendorID":string,
   "VendorName":string,
   "POHeaderRowIdent":string,
      /**  Contract Quantity of PO Detail  */  
   "ContractQty":number,
      /**  Contract End Date of POHeader  */  
   "ContractEndDate":string,
      /**  Contract Start Date of PO Header  */  
   "ContractStartDate":string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "LineDesc":string,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  */  
   "CalcOurQty":number,
      /**  (Our) Unit Of Measure.  */  
   "IUM":string,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable.  */  
   "VendorQty":number,
      /**  Part number from the supplier.  */  
   "VenPartNum":string,
      /**   Indicates the costing per quantity. It can be "E" = per each, 
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "CostPerCode":string,
      /**  Unit Of Measure  */  
   "PUM":string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   "BuyerIDName":string,
      /**  Full description of the FOB Code.  */  
   "FOBDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   "TermsCodeDescription":string,
   "Confirmed":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_PODetailSearchTableset{
   PoDetailSearch:Erp_Tablesets_PoDetailSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_POLineSearchRow{
   PONum:number,
   POLine:number,
   DueDate:string,
   BuyerName:string,
   VendorID:string,
   VendorName:string,
   UnitPrice:number,
   IUM:string,
   XOrderQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POLineSearchTableset{
   POLineSearch:Erp_Tablesets_POLineSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PoDetailSearchListRow{
   Company:string,
   PoNum:number,
   SupplierID:string,
   PurchasePoint:string,
   OrderDate:string,
   BuyerName:string,
   SupplierName:string,
   PartNum:string,
   POLine:number,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  */  
   OpenOrder:boolean,
      /**  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  */  
   VoidOrder:boolean,
   EntryPerson:string,
   FOB:string,
   ShipViaCode:string,
   TermsCode:string,
      /**  defaults from the company file.  */  
   ShipName:string,
   ShipAddress1:string,
   ShipAddress2:string,
   ShipAddress3:string,
   ShipCity:string,
   ShipState:string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   ShipCountry:string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   OrderHeld:boolean,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   ShipToConName:string,
      /**  Indicates if the PO can be printed. Print functions are not available if this is = No.  */  
   ReadyToPrint:boolean,
      /**  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  */  
   ApprovedDate:string,
      /**  The BuyerID  that approved the PO. (See ApprovedDate for related info)  */  
   ApprovedBy:string,
      /**   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  */  
   Approve:boolean,
      /**   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  */  
   ApprovalStatus:string,
   VendorVendorID:string,
   VendorName:string,
   POHeaderRowIdent:string,
      /**  Contract Quantity of PO Detail  */  
   ContractQty:number,
      /**  Contract End Date of POHeader  */  
   ContractEndDate:string,
      /**  Contract Start Date of PO Header  */  
   ContractStartDate:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   LineDesc:string,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  */  
   CalcOurQty:number,
      /**  (Our) Unit Of Measure.  */  
   IUM:string,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable.  */  
   VendorQty:number,
      /**  Part number from the supplier.  */  
   VenPartNum:string,
      /**   Indicates the costing per quantity. It can be "E" = per each, 
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  Unit Of Measure  */  
   PUM:string,
      /**  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  */  
   BuyerIDName:string,
      /**  Full description of the FOB Code.  */  
   FOBDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  Full description of the terms which prints on sales orders and invoices.  */  
   TermsCodeDescription:string,
   Confirmed:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PoDetailSearchListTableset{
   PoDetailSearchList:Erp_Tablesets_PoDetailSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PoDetailSearchRow{
   Company:string,
   PoNum:number,
   SupplierID:string,
   PurchasePoint:string,
   OrderDate:string,
   BuyerName:string,
   SupplierName:string,
   PartNum:string,
   POLine:number,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  */  
   OpenOrder:boolean,
      /**  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  */  
   VoidOrder:boolean,
   EntryPerson:string,
   FOB:string,
   ShipViaCode:string,
   TermsCode:string,
      /**  defaults from the company file.  */  
   ShipName:string,
   ShipAddress1:string,
   ShipAddress2:string,
   ShipAddress3:string,
   ShipCity:string,
   ShipState:string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   ShipCountry:string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   OrderHeld:boolean,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   ShipToConName:string,
      /**  Indicates if the PO can be printed. Print functions are not available if this is = No.  */  
   ReadyToPrint:boolean,
      /**  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  */  
   ApprovedDate:string,
      /**  The BuyerID  that approved the PO. (See ApprovedDate for related info)  */  
   ApprovedBy:string,
      /**   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  */  
   Approve:boolean,
      /**   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  */  
   ApprovalStatus:string,
   VendorVendorID:string,
   VendorName:string,
   POHeaderRowIdent:string,
      /**  Contract Quantity of PO Detail  */  
   ContractQty:number,
      /**  Contract End Date of POHeader  */  
   ContractEndDate:string,
      /**  Contract Start Date of PO Header  */  
   ContractStartDate:string,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   LineDesc:string,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  */  
   CalcOurQty:number,
      /**  (Our) Unit Of Measure.  */  
   IUM:string,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable.  */  
   VendorQty:number,
      /**  Part number from the supplier.  */  
   VenPartNum:string,
      /**   Indicates the costing per quantity. It can be "E" = per each, 
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  Unit Of Measure  */  
   PUM:string,
   Confirmed:boolean,
   SysRowID:string,
   BuyerIDName:string,
   FOBDescription:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TermsCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param whereClausePoHeaderSearch
      @param whereClausePoDetailSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetListDropShipmentPO_input{
   whereClausePoHeaderSearch:string,
   whereClausePoDetailSearch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetListDropShipmentPO_output{
   returnObj:Erp_Tablesets_PoDetailSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePoHeaderSearch
      @param whereClausePoDetailSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  The where clause to restrict data for  */  
   whereClausePoHeaderSearch:string,
      /**  The where clause to restrict data for  */  
   whereClausePoDetailSearch:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PoDetailSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetListsFromSelectedKeys_input{
   ds:Erp_Tablesets_PoDetailSearchListTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetListsFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PoDetailSearchListTableset,
   morePages:boolean,
}
}

   /** Required : 
      @param startingPO
      @param partNum
      @param globalPO
      @param pageSize
      @param absolutePage
   */  
export interface GetPOLineSearchRows_input{
      /**  The starting at PO Number entered on the search form  */  
   startingPO:number,
      /**  Part to search for  */  
   partNum:string,
      /**  Whether or not to look at consolidated POs  */  
   globalPO:boolean,
   pageSize:number,
   absolutePage:number,
}

export interface GetPOLineSearchRows_output{
   returnObj:Erp_Tablesets_POLineSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsFromSelectedKeys_input{
   ds:Erp_Tablesets_PODetailSearchTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRowsFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PODetailSearchTableset,
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePoHeaderSearch
      @param whereClausePoDetailSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  The where clause to restrict data for  */  
   whereClausePoHeaderSearch:string,
      /**  The where clause to restrict data for  */  
   whereClausePoDetailSearch:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PODetailSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

