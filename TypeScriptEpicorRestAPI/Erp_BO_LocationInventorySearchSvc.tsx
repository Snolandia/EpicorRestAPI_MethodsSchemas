import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.LocationInventorySearchSvc
// Description: Location Inventory Search service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/$metadata", {
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
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetRows
   Description: This methods will return all the LocationInventory records joined with LocationInventoryAddress
This method will try to mirror the functionality of the base GetRows method, but since we are
populating a temp table (LocationInventorySearch) we need our own public method.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseLocInvSearch:string, whereClauseLocInvAddrSearch:string, whereClauseLocMtl:string, whereClauseDynAttr:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLocInvSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocInvSearch=" + whereClauseLocInvSearch
   }
   if(typeof whereClauseLocInvAddrSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocInvAddrSearch=" + whereClauseLocInvAddrSearch
   }
   if(typeof whereClauseLocMtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLocMtl=" + whereClauseLocMtl
   }
   if(typeof whereClauseDynAttr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynAttr=" + whereClauseDynAttr
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/GetRows" + params, {
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
   Summary: Invoke method GetRowsWithAttributeList
   Description: Takes a list of attributes as a delimited string and converts to a SQL whereClause to pass into GetRows
   OperationID: GetRowsWithAttributeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWithAttributeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithAttributeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsWithAttributeList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LocationInventorySearchSvc/GetRowsWithAttributeList", {
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



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_LocationInventorySearchRow{
   Address1:string,
   Address2:string,
   Address3:string,
   AddressType:string,
   City:string,
   Company:string,
      /**  Contact  */  
   Contact:string,
   CountryNum:number,
   CustNum:number,
   CustShipToNum:string,
   EmailAddress:string,
   FaxNum:string,
   IDNum:string,
   JobNum:string,
   LineDesc:string,
   Listing:string,
   ListingStartDate:string,
   LocationNum:number,
   Name:string,
   OrderLine:number,
   OrderNum:number,
   OrderRelNum:number,
   PackLine:number,
   PackNum:number,
   PartNum:string,
   PhoneNum:string,
   Plant:string,
   SerialNumber:string,
   State:string,
   UseOTS:boolean,
   WarrantyCode:string,
      /**  Warranty Expiration Date  */  
   WarrantyExpirationDate:string,
   WarrantyStartDate:string,
   Zip:string,
   LotNum:string,
      /**  Full address list  */  
   AddressList:string,
      /**  Country description  */  
   Country:string,
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LocationInventorySearchTableset{
   LocationInventorySearch:Erp_Tablesets_LocationInventorySearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whereClauseLocInvSearch
      @param whereClauseLocInvAddrSearch
      @param whereClauseLocMtl
      @param whereClauseDynAttr
      @param attrClassID
      @param attributeListString
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsWithAttributeList_input{
   whereClauseLocInvSearch:string,
   whereClauseLocInvAddrSearch:string,
   whereClauseLocMtl:string,
   whereClauseDynAttr:string,
      /**  AttrClassID value  */  
   attrClassID:string,
      /**  A list of attributes separated by ~.  Each attribute is made up of the following separated by `:
            1. SysRowID of DynAttrClassDtl record
            2. "From" if its a starting filter, "To" if an end filter, "Val" if its a single filter
            3. The attribute value to filter on  */  
   attributeListString:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsWithAttributeList_output{
   returnObj:Erp_Tablesets_LocationInventorySearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseLocInvSearch
      @param whereClauseLocInvAddrSearch
      @param whereClauseLocMtl
      @param whereClauseDynAttr
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLocInvSearch:string,
   whereClauseLocInvAddrSearch:string,
   whereClauseLocMtl:string,
   whereClauseDynAttr:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LocationInventorySearchTableset[],
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

