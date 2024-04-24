import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PerConLnkSearchSvc
// Description: The PerConLnkSearch BO combines data from PerCon and PerConLnk.
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConLnkSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkSearchListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetRows
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria. This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetRows
      @param whereClausePerConSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param whereClausePerConLnkSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param pageSize Desc: The page size, used only for UI adaptor   Required: True
      @param absolutePage Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePerConSearch:string, whereClausePerConLnkSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePerConSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerConSearch=" + whereClausePerConSearch
   }
   if(typeof whereClausePerConLnkSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerConLnkSearch=" + whereClausePerConLnkSearch
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListExcludeInactive
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria, excluding inactive Customer Contacts,
Supplier Contacts, Workforces and Buyers. This method will try to mirror the functionality
of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetListExcludeInactive
      @param whereClause Desc: The where clause to restrict data for.   Required: True   Allow empty value : True
      @param pageSize Desc: The page size, used only for UI adaptor   Required: True
      @param absolutePage Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListExcludeInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetListExcludeInactive(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/GetListExcludeInactive" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsExcludeInactive
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria, excluding inactive Customer Contacts,
Supplier Contacts, Workforces and Buyers. This method will try to mirror the
functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetRowsExcludeInactive
      @param whereClausePerConSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param whereClausePerConLnkSearch Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param pageSize Desc: The page size, used only for UI adapter   Required: True
      @param absolutePage Desc: The absolute page, used only for the UI adapter   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsExcludeInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsExcludeInactive(whereClausePerConSearch:string, whereClausePerConLnkSearch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePerConSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerConSearch=" + whereClausePerConSearch
   }
   if(typeof whereClausePerConLnkSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerConLnkSearch=" + whereClausePerConLnkSearch
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/GetRowsExcludeInactive" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria. This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: Get_GetList
      @param whereClause Desc: The where clause to restrict data for.   Required: True   Allow empty value : True
      @param pageSize Desc: The page size, used only for UI adaptor   Required: True
      @param absolutePage Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCustom
   Description: This methods will return all of the PerConLnkSearch records which will be a subset
of the PerCon records that meet the selection criteria. This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table (PerConLnkSearch) we need our own public method.
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/GetRowsCustom", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsPaging
   Description: Method to return PerConLnk rows.  This method supports server paging.
   OperationID: Get_GetRowsPaging
      @param whereClause Desc: Where clause for data retrieval   Required: True   Allow empty value : True
      @param pageSize Desc: Page size   Required: True
      @param absolutePage Desc: Absolute page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsPaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsPaging(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConLnkSearchSvc/GetRowsPaging" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkSearchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerConLnkSearchListRow[],
}

export interface Erp_Tablesets_PerConLnkSearchListRow{
   "Company":string,
   "PerConID":number,
   "ContextLink":string,
   "LinkSysRowID":string,
   "Name":string,
   "Address1":string,
   "Address2":string,
   "Address3":string,
   "City":string,
   "State":string,
   "Zip":string,
   "Country":string,
   "CountryNum":number,
   "SysRowID":string,
      /**  Buyer ID from the PurAgent table.  */  
   "BuyerID":string,
      /**  Name of the buyer.  */  
   "BuyerName":string,
      /**  Name of the Customer Contact.  */  
   "CustContactName":string,
      /**  Customer ID from Customer table.  */  
   "CustID":string,
      /**  Full name of the customer.  */  
   "CustName":string,
   "EmpID":string,
   "EmpName":string,
   "PurPoint":string,
   "PurPointName":string,
   "SalesRepCode":string,
   "SalesRepName":string,
   "ShipToName":string,
   "ShipToNum":string,
   "VendorContactName":string,
   "VendorID":string,
   "VendorName":string,
   "PREmpID":string,
   "PREmpName":string,
   "PrimaryContext":boolean,
      /**  Name in the linked record.  */  
   "LinkName":string,
   "FirstName":string,
   "MiddleName":string,
   "LastName":string,
   "Inactive":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_PerConLnkSearchListRow{
   Company:string,
   PerConID:number,
   ContextLink:string,
   LinkSysRowID:string,
   Name:string,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
   State:string,
   Zip:string,
   Country:string,
   CountryNum:number,
   SysRowID:string,
      /**  Buyer ID from the PurAgent table.  */  
   BuyerID:string,
      /**  Name of the buyer.  */  
   BuyerName:string,
      /**  Name of the Customer Contact.  */  
   CustContactName:string,
      /**  Customer ID from Customer table.  */  
   CustID:string,
      /**  Full name of the customer.  */  
   CustName:string,
   EmpID:string,
   EmpName:string,
   PurPoint:string,
   PurPointName:string,
   SalesRepCode:string,
   SalesRepName:string,
   ShipToName:string,
   ShipToNum:string,
   VendorContactName:string,
   VendorID:string,
   VendorName:string,
   PREmpID:string,
   PREmpName:string,
   PrimaryContext:boolean,
      /**  Name in the linked record.  */  
   LinkName:string,
   FirstName:string,
   MiddleName:string,
   LastName:string,
   Inactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerConLnkSearchListTableset{
   PerConLnkSearchList:Erp_Tablesets_PerConLnkSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PerConLnkSearchRow{
   Company:string,
   PerConID:number,
   ContextLink:string,
   LinkSysRowID:string,
   Name:string,
   Address1:string,
   Address2:string,
   Address3:string,
   City:string,
   State:string,
   Zip:string,
   Country:string,
   CountryNum:number,
   SysRowID:string,
      /**  Buyer ID from the PurAgent table.  */  
   BuyerID:string,
      /**  Name of the buyer.  */  
   BuyerName:string,
      /**  Name of the Customer Contact.  */  
   CustContactName:string,
      /**  Customer ID from Customer table.  */  
   CustID:string,
      /**  Full name of the customer.  */  
   CustName:string,
   EmpID:string,
   EmpName:string,
   PurPoint:string,
   PurPointName:string,
   SalesRepCode:string,
   SalesRepName:string,
   ShipToName:string,
   ShipToNum:string,
   VendorContactName:string,
   VendorID:string,
   VendorName:string,
   PREmpID:string,
   PREmpName:string,
   PrimaryContext:boolean,
      /**  Name in the linked record.  */  
   LinkName:string,
   FirstName:string,
   MiddleName:string,
   LastName:string,
   Inactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerConLnkSearchTableset{
   PerConLnkSearch:Erp_Tablesets_PerConLnkSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListExcludeInactive_input{
      /**  The where clause to restrict data for.  */  
   whereClause:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetListExcludeInactive_output{
   returnObj:Erp_Tablesets_PerConLnkSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  The where clause to restrict data for.  */  
   whereClause:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_PerConLnkSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePerConSearch
      @param whereClausePerConLnkSearch
      @param inactives
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  The where clause to restrict data for  */  
   whereClausePerConSearch:string,
      /**  The where clause to restrict data for  */  
   whereClausePerConLnkSearch:string,
      /**  Include inactive context links  */  
   inactives:boolean,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_PerConLnkSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePerConSearch
      @param whereClausePerConLnkSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsExcludeInactive_input{
      /**  The where clause to restrict data for  */  
   whereClausePerConSearch:string,
      /**  The where clause to restrict data for  */  
   whereClausePerConLnkSearch:string,
      /**  The page size, used only for UI adapter  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adapter  */  
   absolutePage:number,
}

export interface GetRowsExcludeInactive_output{
   returnObj:Erp_Tablesets_PerConLnkSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsPaging_input{
      /**  Where clause for data retrieval  */  
   whereClause:string,
      /**  Page size  */  
   pageSize:number,
      /**  Absolute page  */  
   absolutePage:number,
}

export interface GetRowsPaging_output{
   returnObj:Erp_Tablesets_PerConLnkSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePerConSearch
      @param whereClausePerConLnkSearch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  The where clause to restrict data for  */  
   whereClausePerConSearch:string,
      /**  The where clause to restrict data for  */  
   whereClausePerConLnkSearch:string,
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PerConLnkSearchTableset[],
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

