import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ProjSummarySvc
// Description: Project Management Code Master File. Establishes the valid Project Mgmt
code for the system. This file provides a description for the project
and allows user to set up project codes to be used during the order entry
and job entry process.
DELETING: Not allowed if referenced in the Job file, or Order files.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/$metadata", {
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
   Summary: Invoke method CalcSummaryOrdered
   Description: Culculates summary orders.
   OperationID: CalcSummaryOrdered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcSummaryOrdered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcSummaryOrdered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcSummaryOrdered(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/CalcSummaryOrdered", {
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
   Summary: Invoke method ProjectCostsHours
   Description: Calculates Project cost hours
   OperationID: ProjectCostsHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProjectCostsHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProjectCostsHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProjectCostsHours(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/ProjectCostsHours", {
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
      @param curProjectID
   */  
export interface CalcSummaryOrdered_input{
      /**  Project ID  */  
   curProjectID:string,
}

export interface CalcSummaryOrdered_output{
parameters : {
      /**  output parameters  */  
   totord:number,
   totinv:number,
   totdep:number,
   totstkmtl:number,
   totstklbr:number,
   totstkbur:number,
   totstksub:number,
   totstkmbur:number,
   totactstk:number,
}
}

export interface Erp_Tablesets_ProjSummaryTableset{
   ProjectCost:Erp_Tablesets_ProjectCostRow[],
   ProjectHour:Erp_Tablesets_ProjectHourRow[],
   ProjectSumry:Erp_Tablesets_ProjectSumryRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProjectCostRow{
   ActMtlCost:number,
   ActSubCost:number,
   Class:string,
   ClassDescription:string,
   EstMtlCost:number,
   EstSubCost:number,
   ProjectID:string,
   QuotedMtlCost:number,
   QuotedSubCost:number,
   EarnedMtlCost:number,
   EarnedSubCost:number,
   EstMtlBurCost:number,
   ActMtlBurCost:number,
   EarnedMtlBurCost:number,
      /**  Actual Other Direct Costs  */  
   ActODCCost:number,
      /**  Estimated Other Direct Cost  */  
   EstODCCost:number,
      /**  Quoted Other Direct cost  */  
   QuotedODCCost:number,
      /**  Earned Other Direct cost  */  
   EarnedODCCost:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProjectHourRow{
   ProjectID:string,
   JCDept:string,
   DeptDescription:string,
   EstBurHours:number,
   EstLbrHours:number,
   QuotedBurHours:number,
   QuotedLbrHours:number,
   ActBurHours:number,
   ActLbrHours:number,
   EarnedBurHours:number,
   EarnedLbrHours:number,
   QuotedLbrCost:number,
   QuotedBurCost:number,
   EstLbrCost:number,
   EstBurCost:number,
   ActLbrCost:number,
   ActBurCost:number,
   EarnedLbrCost:number,
   EarnedBurCost:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProjectSumryRow{
   EstMtl:number,
   EstLbr:number,
   EstBur:number,
   EstSub:number,
   EstMtlBur:number,
   ActMtl:number,
   ActLbr:number,
   ActBur:number,
   ActSub:number,
   ActMtlBur:number,
   EarnedMtl:number,
   EarnedLbr:number,
   EarnedBur:number,
   EarnedSub:number,
   EarnedMtlBur:number,
   EstBurHrs:number,
   EstLbrHrs:number,
   ActBurHrs:number,
   ActLbrHrs:number,
   EarBurHrs:number,
   EarLbrHrs:number,
   QuoMtl:number,
   QuoLbr:number,
   QuoBur:number,
   QuoSub:number,
   QuoMtlBur:number,
   QuoBurHrs:number,
   QuoLbrHrs:number,
   QuotTot:number,
   EstTot:number,
   ActTot:number,
   EarnedTot:number,
      /**  Actual Other Direct Costs  */  
   ActODC:number,
      /**  Actual Other Direct Cost Burden  */  
   EarnedODC:number,
      /**  Estimated Other Direct Cost  */  
   EstODC:number,
      /**  Quoted Other Direct cost  */  
   QuoODC:number,
   QuoHrsTot:number,
   ActHrsTot:number,
   EarHrsTot:number,
   EstHrsTot:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
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
      @param curProjectID
   */  
export interface ProjectCostsHours_input{
      /**  Project ID  */  
   curProjectID:string,
}

export interface ProjectCostsHours_output{
   returnObj:Erp_Tablesets_ProjSummaryTableset[],
}

