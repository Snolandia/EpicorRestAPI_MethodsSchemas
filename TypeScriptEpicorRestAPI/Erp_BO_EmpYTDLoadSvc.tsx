import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.EmpYTDLoadSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/$metadata", {
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
   Summary: Invoke method DeleteEmpYTDLoad
   Description: Deletes the PRCheck record.  The delete trigger for PRCheck deletes the
PRChkDtl, PRChkTax and PRChkDed records.
   OperationID: DeleteEmpYTDLoad
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteEmpYTDLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteEmpYTDLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteEmpYTDLoad(requestBody:DeleteEmpYTDLoad_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteEmpYTDLoad_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/DeleteEmpYTDLoad", {
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
         resolve(data as DeleteEmpYTDLoad_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEmpYTDLoadForEmpID
   Description: Gets the data for Deductions, Earnings, and Tax for a specific employee id.
   OperationID: GetEmpYTDLoadForEmpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEmpYTDLoadForEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpYTDLoadForEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmpYTDLoadForEmpID(requestBody:GetEmpYTDLoadForEmpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEmpYTDLoadForEmpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/GetEmpYTDLoadForEmpID", {
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
         resolve(data as GetEmpYTDLoadForEmpID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEmpYTDLoad
   Description: Gets the data for the Deductions, Earnings and Tax temp tables based on the
employee ID's from the Employee ID temp table.
   OperationID: GetEmpYTDLoad
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEmpYTDLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpYTDLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmpYTDLoad(requestBody:GetEmpYTDLoad_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEmpYTDLoad_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/GetEmpYTDLoad", {
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
         resolve(data as GetEmpYTDLoad_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEmployeeList
   Description: This method is only to be used in the BL Tester to get a EmployeeList
record for employee 100.
   OperationID: GetNewEmployeeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmployeeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmployeeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEmployeeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/GetNewEmployeeList", {
          method: 'post',
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
         resolve(data as GetNewEmployeeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetEmpYTDLoad
   Description: Updates the appropriate tables with the data for the Deductions, Earnings and
Tax temp tables.
   OperationID: SetEmpYTDLoad
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetEmpYTDLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEmpYTDLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetEmpYTDLoad(requestBody:SetEmpYTDLoad_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetEmpYTDLoad_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/SetEmpYTDLoad", {
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
         resolve(data as SetEmpYTDLoad_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPRPeriodEndDate
   OperationID: GetPRPeriodEndDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPRPeriodEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPRPeriodEndDate(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPRPeriodEndDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/GetPRPeriodEndDate", {
          method: 'post',
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
         resolve(data as GetPRPeriodEndDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEmpYTDLoadTotals
   Description: Calculates Employee YTD Load totals and returns the values in a dataset
   OperationID: GetEmpYTDLoadTotals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetEmpYTDLoadTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmpYTDLoadTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmpYTDLoadTotals(requestBody:GetEmpYTDLoadTotals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEmpYTDLoadTotals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpYTDLoadSvc/GetEmpYTDLoadTotals", {
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
         resolve(data as GetEmpYTDLoadTotals_output)
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
   /** Required : 
      @param EmployeeID
   */  
export interface DeleteEmpYTDLoad_input{
      /**  Employee number  */  
   EmployeeID:string,
}

export interface DeleteEmpYTDLoad_output{
}

export interface Erp_Tablesets_EmpYTDLoadDeductRow{
      /**  Company  */  
   Company:string,
      /**  Employee ID  */  
   EmployeeID:string,
      /**  Payroll deduction ID  */  
   DeductionID:string,
      /**  Deductions description  */  
   DeductionDesc:string,
      /**  Deduction Amount  */  
   DeductionAmt:number,
      /**  Deduction number  */  
   DeductionNum:number,
      /**  Original deduction amount  */  
   OrigDeductionAmt:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpYTDLoadEarnRow{
      /**  Earnings type.  */  
   EarningType:string,
      /**  Earning hours  */  
   EarningsHours:number,
      /**  Earnings amount  */  
   EarningsAmt:number,
      /**  Company  */  
   Company:string,
      /**  Employee ID  */  
   EmployeeID:string,
      /**  Earning type description  */  
   EarningTypeDesc:string,
      /**  Original Premium pay amount  */  
   OrigPremiumPay:number,
      /**  Original Premium base pay amount  */  
   OrigPremiumBasePay:number,
      /**  Original base pay amount  */  
   OrigBasePay:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpYTDLoadTableset{
   EmpYTDLoadDeduct:Erp_Tablesets_EmpYTDLoadDeductRow[],
   EmpYTDLoadEarn:Erp_Tablesets_EmpYTDLoadEarnRow[],
   EmpYTDLoadTax:Erp_Tablesets_EmpYTDLoadTaxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmpYTDLoadTaxRow{
      /**  Company  */  
   Company:string,
      /**  Employee ID  */  
   EmployeeID:string,
      /**  Tax table ID  */  
   TaxTableID:string,
      /**  Tax table description  */  
   TaxTableDesc:string,
      /**  Tax amount  */  
   TaxAmt:number,
      /**  Original tax amount  */  
   OrigTaxAmt:number,
      /**  Tax type from PRTaxMas  */  
   TaxType:string,
      /**  In active status from PREmpTax  */  
   InActive:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpYTDLoadTotalsRow{
   Company:string,
      /**  Deduction Total  */  
   DeductionTotal:number,
      /**  Earnings total  */  
   EarningsTotal:number,
      /**  Hours Total  */  
   HoursTotal:number,
      /**  Tax Total  */  
   TaxTotal:number,
      /**  Employee ID  */  
   EmployeeID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpYTDLoadTotalsTableset{
   EmpYTDLoadTotals:Erp_Tablesets_EmpYTDLoadTotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmployeeIDListRow{
      /**  Company  */  
   Company:string,
      /**  Employee IDs  */  
   EmployeeID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmployeeIDListTableset{
   EmployeeIDList:Erp_Tablesets_EmployeeIDListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param empID
   */  
export interface GetEmpYTDLoadForEmpID_input{
      /**  Employee ID  */  
   empID:string,
}

export interface GetEmpYTDLoadForEmpID_output{
   returnObj:Erp_Tablesets_EmpYTDLoadTableset[],
}

   /** Required : 
      @param empID
      @param ds
   */  
export interface GetEmpYTDLoadTotals_input{
      /**  The employee id to calculate totals for  */  
   empID:string,
   ds:Erp_Tablesets_EmpYTDLoadTableset[],
}

export interface GetEmpYTDLoadTotals_output{
   returnObj:Erp_Tablesets_EmpYTDLoadTotalsTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetEmpYTDLoad_input{
   ds:Erp_Tablesets_EmployeeIDListTableset[],
}

export interface GetEmpYTDLoad_output{
   returnObj:Erp_Tablesets_EmpYTDLoadTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmployeeIDListTableset,
}
}

export interface GetNewEmployeeList_output{
   returnObj:Erp_Tablesets_EmployeeIDListTableset[],
}

export interface GetPRPeriodEndDate_output{
parameters : {
      /**  output parameters  */  
   prPeriodEndDate:string,
   errorMessage:string,
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

   /** Required : 
      @param ds
   */  
export interface SetEmpYTDLoad_input{
   ds:Erp_Tablesets_EmpYTDLoadTableset[],
}

export interface SetEmpYTDLoad_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpYTDLoadTableset,
}
}

