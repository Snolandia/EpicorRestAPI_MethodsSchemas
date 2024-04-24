import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PipeLineSvc
// Description: PipeLineSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", {
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
   Summary: Invoke method BuildPipeLine
   Description: Call this method to build the Pipeline grid for a Salesperson.
   OperationID: BuildPipeLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildPipeLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildPipeLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildPipeLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/BuildPipeLine", {
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
   Summary: Invoke method CompanyActualQuota
   Description: Company Actual Quota.
   OperationID: CompanyActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CompanyActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CompanyActualQuota(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/CompanyActualQuota", {
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
   Summary: Invoke method GetActuals
   Description: Call the correct method to retrieve Actuals data based on the Actuals Type.
   OperationID: GetActuals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActuals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActuals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetActuals(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/GetActuals", {
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
   Summary: Invoke method GetComboValues
   Description: Call this method to get list of Region, Territory and Sales Rep
There are three levels of access:
View All: This is enabled when the user's SalesRepID has 'View Company Pipeline' turned on in
Workforce Maintenance.
Can view aggregate totals of Actuals by Company, Region, Territory or SalesRep for ALL
regions, territories, salesreps in the company
Sales Manager:  This is enabled when the user's SalesRepID is entered as the Sales Manager for one
or more Regions in Sales Region Maintenance.
Can view aggregate totals of Actuals by Region, Territory or SalesRep for the
regions for which they are Sales Manager
In this situation:
pcTypeList contains Region, Territory, SalesManager and SalesRep
pcRegionList contains the Regions for which the current user is Sales Manager
pcTerritoryList contains the territories for their Regions
pcSalesRepList contains only the SalesReps that "Report To" the current user
Sales Rep:  This is the level of access granted when neither of the other two levels apply.
Can view only their own totals, and NOT aggregated by Region, or Territory
In this situation:
pcTypeList contains only the "SalesRep" choice
pcRegionList and pcTerritoryList are empty
pcSalesRepList contains only the SalesRep associated with the current user
   OperationID: GetComboValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetComboValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComboValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetComboValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/GetComboValues", {
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
   Summary: Invoke method GetDates
   OperationID: GetDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDates(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/GetDates", {
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

   /**  
   Summary: Invoke method GetQuarter
   Description: This method returns the Fiscal Quarter for given Company and FiscalPeriod.
   OperationID: GetQuarter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuarter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuarter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuarter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/GetQuarter", {
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
   Summary: Invoke method GetTypeList
   Description: Call this method to get list of Region, Territory and Sales Rep
There are three levels of access:
View All: This is enabled when the user's SalesRepID has 'View Company Pipeline' turned on in
Workforce Maintenance.
Can view aggregate totals of Actuals by Company, Region, Territory or SalesRep for ALL
regions, territories, salesreps in the company
Sales Manager:  This is enabled when the user's SalesRepID is entered as the Sales Manager for one
or more Regions in Sales Region Maintenance.
Can view aggregate totals of Actuals by Region, Territory or SalesRep for the
regions for which they are Sales Manager
In this situation:
pcTypeList contains Region, Territory, SalesManager and SalesRep
pcRegionList contains the Regions for which the current user is Sales Manager
pcTerritoryList contains the territories for their Regions
pcSalesRepList contains only the SalesReps that "Report To" the current user
Sales Rep:  This is the level of access granted when neither of the other two levels apply.
Can view only their own totals, and NOT aggregated by Region, or Territory
In this situation:
pcTypeList contains only the "SalesRep" choice
pcRegionList and pcTerritoryList are empty
pcSalesRepList contains only the SalesRep associated with the current user
   OperationID: GetTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/GetTypeList", {
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

   /**  
   Summary: Invoke method GetComboValuesDataset
   Description: Get the valid region, territory, and sales rep values and populate them in the combo boxes.
   OperationID: GetComboValuesDataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetComboValuesDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComboValuesDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetComboValuesDataset(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/GetComboValuesDataset", {
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
   Summary: Invoke method RegionActualQuota
   Description: This method displays the Regional Actual Quota
   OperationID: RegionActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegionActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegionActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RegionActualQuota(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/RegionActualQuota", {
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
   Summary: Invoke method SalesManagerActualQuota
   Description: This method displays Sales Manager Actual Quota.
   OperationID: SalesManagerActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesManagerActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesManagerActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesManagerActualQuota(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/SalesManagerActualQuota", {
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
   Summary: Invoke method SalesRepActualQuota
   Description: This method displays Sales Rep's Actual Quota.
   OperationID: SalesRepActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesRepActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesRepActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesRepActualQuota(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/SalesRepActualQuota", {
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
   Summary: Invoke method SetupPipeLineControlTable
   Description: Initialize the PipeLineControl table.
   OperationID: SetupPipeLineControlTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetupPipeLineControlTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetupPipeLineControlTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetupPipeLineControlTable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/SetupPipeLineControlTable", {
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
   Summary: Invoke method TerritoryActualQuota
   Description: This method displays Territory Actual Quota
   OperationID: TerritoryActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TerritoryActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TerritoryActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TerritoryActualQuota(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/TerritoryActualQuota", {
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
   /** Required : 
      @param pdtFromFilterDate
      @param pdtToFilterDate
      @param piFiscalYear
      @param piFiscalPeriod
   */  
export interface BuildPipeLine_input{
      /**  From Filter Date  */  
   pdtFromFilterDate:string,
      /**  To Filter Date  */  
   pdtToFilterDate:string,
      /**  Fiscal Year  */  
   piFiscalYear:number,
      /**  Fiscal Period  */  
   piFiscalPeriod:number,
}

export interface BuildPipeLine_output{
   returnObj:Erp_Tablesets_PipeLineTableset[],
}

   /** Required : 
      @param piFiscalYear
      @param pcFiscalYearSuffix
      @param piFiscalPeriod
      @param pdtFromFilterDate
      @param pdtToFilterDate
      @param ds
   */  
export interface CompanyActualQuota_input{
      /**  Fiscal Year  */  
   piFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   pcFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   piFiscalPeriod:number,
      /**  From Filter Date  */  
   pdtFromFilterDate:string,
      /**  To Filter Date  */  
   pdtToFilterDate:string,
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}

export interface CompanyActualQuota_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}
}

export interface Erp_Tablesets_PipeLineControlRow{
      /**  Type of Actuals to show in Salesperson Pipeline  */  
   AType:string,
      /**  Delimited list of available Actual Types  */  
   ATypeList:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   FromDate:string,
   Period:number,
   Quarter:number,
   Region:string,
      /**  Delimited list of regions (RegionCode`Description~RegionCode`Description)  */  
   RegionList:string,
   SalesRep:string,
      /**  Delimited list of available Sales Reps  */  
   SalesRepList:string,
   Territory:string,
      /**  Delimited list of available Territories  */  
   TerritoryList:string,
   ToDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PipeLineGridRow{
      /**  Company x  */  
   Company:string,
      /**  Region Code  */  
   RegionCode:string,
   TerritoryID:string,
   SalesRepCode:string,
   ActiveTaskID:string,
   QuoteNum:number,
   CustID:string,
   Manager:string,
   ExpectedClose:string,
   PrimeRep:boolean,
   IsConsolidated:boolean,
   PipeLineExpected:number,
   PipeLineAdjusted:number,
   SalesRepName:string,
   CustomerName:string,
   CurrentMileStoneDesc:string,
   dummyKeyField:string,
   PipeLineBestCs:number,
   PipeLineWorstCs:number,
   SysRowID:string,
   ManagerName:string,
   RegionDescription:string,
   TerritoryIDTerritoryDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PipeLineTableset{
   PipeLineGrid:Erp_Tablesets_PipeLineGridRow[],
   PipeLineControl:Erp_Tablesets_PipeLineControlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PipeLineTotalsRow{
   MTDQuota:number,
   MTDActual:number,
   QTDQuota:number,
   QTDActual:number,
   YTDQuota:number,
   YTDActual:number,
   OverDue:number,
   DueToday:number,
   DueThisWeek:number,
   DueNextWeek:number,
   DueThisMonth:number,
   DueNextMonth:number,
   dummyKeyField:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PipeLineTotalsTableset{
   PipeLineTotals:Erp_Tablesets_PipeLineTotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param actualsType
      @param fiscalYear
      @param fiscalYearSuffix
      @param fiscalPeriod
      @param fromDate
      @param toDate
      @param salesRepCode
      @param regionCode
      @param territoryID
      @param ds
   */  
export interface GetActuals_input{
      /**  Type of actuals to retrieve  */  
   actualsType:string,
      /**  Selected fiscal year  */  
   fiscalYear:number,
      /**  Suffix for the fiscal year  */  
   fiscalYearSuffix:string,
      /**  Selected fiscal period  */  
   fiscalPeriod:number,
      /**  Date from which we filter resultsDate from which we filter results  */  
   fromDate:string,
      /**  Date up to which we filter results  */  
   toDate:string,
   salesRepCode:string,
   regionCode:string,
   territoryID:string,
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}

export interface GetActuals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}
}

   /** Required : 
      @param actualsType
      @param ds
   */  
export interface GetComboValuesDataset_input{
      /**  Type of actuals to populate  */  
   actualsType:string,
   ds:Erp_Tablesets_PipeLineTableset[],
}

export interface GetComboValuesDataset_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTableset[],
}
}

   /** Required : 
      @param pcActualsType
   */  
export interface GetComboValues_input{
      /**  Type (aggregation-level). One of: Company, Region, Territory, SalesManager, SalesRep  */  
   pcActualsType:string,
}

export interface GetComboValues_output{
parameters : {
      /**  output parameters  */  
   pcRegionList:string,
   pcTerritoryList:string,
   pcSalesRepList:string,
}
}

export interface GetDates_output{
parameters : {
      /**  output parameters  */  
   piFiscalYear:number,
   pcFiscalYearSuffix:string,
   piFiscalPeriod:number,
   pdtFromFilterDate:string,
   pdtToFilterDate:string,
}
}

   /** Required : 
      @param piFiscalYear
      @param pcFiscalYearSuffix
      @param piFiscalPeriod
   */  
export interface GetQuarter_input{
      /**  Fiscal Year  */  
   piFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   pcFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   piFiscalPeriod:number,
}

export interface GetQuarter_output{
parameters : {
      /**  output parameters  */  
   piFiscalQtr:number,
}
}

export interface GetTypeList_output{
parameters : {
      /**  output parameters  */  
   pcTypeList:string,
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
      @param pcSalesRepCode
      @param pcRegionCode
      @param piFiscalYear
      @param pcFiscalYearSuffix
      @param piFiscalPeriod
      @param pdtFromFilterDate
      @param pdtToFilterDate
      @param ds
   */  
export interface RegionActualQuota_input{
      /**  SalesRep Code  */  
   pcSalesRepCode:string,
      /**  Region Code  */  
   pcRegionCode:string,
      /**  Fiscal Year  */  
   piFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   pcFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   piFiscalPeriod:number,
      /**  From Filter Date  */  
   pdtFromFilterDate:string,
      /**  To Filter Date  */  
   pdtToFilterDate:string,
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}

export interface RegionActualQuota_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}
}

   /** Required : 
      @param pcSalesRepCode
      @param piFiscalYear
      @param pcFiscalYearSuffix
      @param piFiscalPeriod
      @param pdtFromFilterDate
      @param pdtToFilterDate
      @param ds
   */  
export interface SalesManagerActualQuota_input{
      /**  SalesRep Code  */  
   pcSalesRepCode:string,
      /**  Fiscal Year  */  
   piFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   pcFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   piFiscalPeriod:number,
      /**  From Filter Date  */  
   pdtFromFilterDate:string,
      /**  To Filter Date  */  
   pdtToFilterDate:string,
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}

export interface SalesManagerActualQuota_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}
}

   /** Required : 
      @param pcSalesRepCode
      @param pcTerritoryID
      @param piFiscalYear
      @param pcFiscalYearSuffix
      @param piFiscalPeriod
      @param pdtFromFilterDate
      @param pdtToFilterDate
      @param ds
   */  
export interface SalesRepActualQuota_input{
      /**  SalesRep Code  */  
   pcSalesRepCode:string,
      /**  Territory ID  */  
   pcTerritoryID:string,
      /**  Fiscal Year  */  
   piFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   pcFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   piFiscalPeriod:number,
      /**  From Filter Date  */  
   pdtFromFilterDate:string,
      /**  To Filter Date  */  
   pdtToFilterDate:string,
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}

export interface SalesRepActualQuota_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface SetupPipeLineControlTable_input{
   ds:Erp_Tablesets_PipeLineTableset[],
}

export interface SetupPipeLineControlTable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTableset[],
}
}

   /** Required : 
      @param pcSalesRepCode
      @param pcTerritoryID
      @param piFiscalYear
      @param pcFiscalYearSuffix
      @param piFiscalPeriod
      @param pdtFromFilterDate
      @param pdtToFilterDate
      @param ds
   */  
export interface TerritoryActualQuota_input{
      /**  SalesRep Code  */  
   pcSalesRepCode:string,
      /**  Territory ID  */  
   pcTerritoryID:string,
      /**  Fiscal Year  */  
   piFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   pcFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   piFiscalPeriod:number,
      /**  From Filter Date  */  
   pdtFromFilterDate:string,
      /**  To Filter Date  */  
   pdtToFilterDate:string,
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}

export interface TerritoryActualQuota_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PipeLineTotalsTableset[],
}
}

