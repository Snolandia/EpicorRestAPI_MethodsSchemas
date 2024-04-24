import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CashFlowSvc
// Description: bo/CashFlow
           Report on weekly cash flow numbers
           Jennifer Johnson
           07/27/04
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/$metadata", {
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
   Description: This method replaces the standard GetRows method
   OperationID: Get_GetRows
      @param bookID Desc: Book ID   Required: True   Allow empty value : True
      @param budgetCodeID Desc: Book ID   Required: True   Allow empty value : True
      @param startingCash Desc: Starting Cash   Required: True
      @param displayType Desc: T = Terms, D = Terms w/Discount, A = Avg Pay Days   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(bookID:string, budgetCodeID:string, startingCash:string, displayType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof bookID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "bookID=" + bookID
   }
   if(typeof budgetCodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "budgetCodeID=" + budgetCodeID
   }
   if(typeof startingCash!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "startingCash=" + startingCash
   }
   if(typeof displayType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "displayType=" + displayType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/GetRows" + params, {
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
   Summary: Invoke method SetCashFlowDefaults
   Description: Set default values for CashFlow Entry.
   OperationID: SetCashFlowDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCashFlowDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCashFlowDefaults(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CashFlowSvc/SetCashFlowDefaults", {
          method: 'post',
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
export interface Erp_Tablesets_CashFlowParametersRow{
      /**  Unique Book Identifier  */  
   BookID:string,
   BudgetCodeID:string,
   Calculation:string,
   StartingCash:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashFlowRow{
   EndDate:string,
   OpenAR:number,
   OpenAP:number,
   Net:number,
   AvailCash:number,
   OpenOrders:number,
   OpenPOs:number,
   BudExp:number,
   ProjNet:number,
   ProjCash:number,
   ShipNotInv:number,
   RecNotInv:number,
   OpenARPI:number,
   OpenAPPI:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashFlowTableset{
   CashFlow:Erp_Tablesets_CashFlowRow[],
   CashFlowParameters:Erp_Tablesets_CashFlowParametersRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param bookID
      @param budgetCodeID
      @param startingCash
      @param displayType
   */  
export interface GetRows_input{
      /**  Book ID  */  
   bookID:string,
      /**  Book ID  */  
   budgetCodeID:string,
      /**  Starting Cash  */  
   startingCash:number,
      /**  T = Terms, D = Terms w/Discount, A = Avg Pay Days  */  
   displayType:string,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CashFlowTableset[],
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

export interface SetCashFlowDefaults_output{
   returnObj:Erp_Tablesets_CashFlowTableset[],
}

