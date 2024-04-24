import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.OTSSearchSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OTSSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OTSSearchSvc/$metadata", {
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
   Description: This method will try to mirror the functionality of the base GetRows method but since we are populating
a temp table (BOLSlip) we need our own public method.
Code is based on GetSlips from bo/BOL/BOL.p
   OperationID: Get_GetRows
      @param whereClause Desc: The where clause to restrict data for   Required: True   Allow empty value : True
      @param ipOrderNum Desc: Order Num   Required: True
      @param ipOrderLine Desc: Order Line   Required: True
      @param ipOrderRelNum Desc: Order Rel Num   Required: True
      @param ipPageSize Desc: The page size, used only for UI adaptor   Required: True
      @param ipabsolutePage Desc: The absolute page, used only for the UI adaptor   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClause:string, ipOrderNum:string, ipOrderLine:string, ipOrderRelNum:string, ipPageSize:string, ipabsolutePage:string, epicorHeaders?:Headers){
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
   if(typeof ipOrderNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipOrderNum=" + ipOrderNum
   }
   if(typeof ipOrderLine!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipOrderLine=" + ipOrderLine
   }
   if(typeof ipOrderRelNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipOrderRelNum=" + ipOrderRelNum
   }
   if(typeof ipPageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipPageSize=" + ipPageSize
   }
   if(typeof ipabsolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipabsolutePage=" + ipabsolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OTSSearchSvc/GetRows" + params, {
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



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_OTSSearchRow{
      /**  Address 1  */  
   OTSAddress1:string,
   OTSAddress2:string,
   OTSAddress3:string,
   OTSCity:string,
   OTSContact:string,
   OTSCountryNum:number,
   OTSFaxNum:string,
   OTSName:string,
   OTSPhoneNum:string,
   OTSResaleID:string,
   OTSState:string,
   OTSZIP:string,
   OTSCntryDescription:string,
   TaxRegionCodeDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OTSSearchTableset{
   OTSSearch:Erp_Tablesets_OTSSearchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whereClause
      @param ipOrderNum
      @param ipOrderLine
      @param ipOrderRelNum
      @param ipPageSize
      @param ipabsolutePage
   */  
export interface GetRows_input{
      /**  The where clause to restrict data for  */  
   whereClause:string,
      /**  Order Num  */  
   ipOrderNum:number,
      /**  Order Line  */  
   ipOrderLine:number,
      /**  Order Rel Num  */  
   ipOrderRelNum:number,
      /**  The page size, used only for UI adaptor  */  
   ipPageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   ipabsolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_OTSSearchTableset[],
parameters : {
      /**  output parameters  */  
   opMorePages:boolean,
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
