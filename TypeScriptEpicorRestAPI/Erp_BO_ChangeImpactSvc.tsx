import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ChangeImpactSvc
// Description: This object is used to view the effects on each department
           that result from changes made to the schedule. This include the actual
           number of hours and days, what-if hours and days and change hours and
           days overdue. This is a non-standard bl object with no standard methods,
           it can't be updated nor deleted. This is just for information purposes.
           bo/ChangeImpact/ChangeImpact.p
           Change Impact Informer Business Object
           Fernanda Garcia
           04/28/2005
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/$metadata", {
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
   Summary: Invoke method GetData
   Description: Loads the start up data for Change Impact Informer
If a change is made to this method the same change should be applied to
the GetSpecificBinSearch method.
   OperationID: GetData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetData(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/GetData", {
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
   Summary: Invoke method OnChangeParameters
   Description: This method will recalculate the Early/Late/OnTime jobs when the JobReq,
EarlyGracePeriod and LateGracePeriod change.
   OperationID: OnChangeParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeParameters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/OnChangeParameters", {
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
export interface Erp_Tablesets_ChangeImpactTableset{
   ChgImpHed:Erp_Tablesets_ChgImpHedRow[],
   ChgImpDtl:Erp_Tablesets_ChgImpDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ChgImpDtlRow{
      /**  Work Center JCDepartment Code.  */  
   DeptCode:string,
      /**  Resource Group ID  */  
   ResourceGrpID:string,
      /**  Company Identifier  */  
   Company:string,
      /**  Hours Over  */  
   HoursOver:number,
      /**  Days Over  */  
   DaysOver:number,
      /**  What If Hours Over  */  
   WIHoursOver:number,
      /**  What if Days Over  */  
   WIDaysOver:number,
      /**  Change Hours Over  */  
   ChgHoursOver:number,
      /**  Change Days Over  */  
   ChgDaysOver:number,
   ResourceGrpIDDescription:string,
   SysRowID:string,
   DeptCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ChgImpHedRow{
      /**  The date that is the basis for early and late calculations  */  
   JobReq:string,
      /**  Number of days before the JobReq Date that a job is considered early.  */  
   EarlyGracePeriod:number,
      /**  Number of day after the JobReq date that a job can be considered early  */  
   LateGracePeriod:number,
      /**  Actual Jobs Early  */  
   ActualJobsEarly:number,
      /**  Actual Jobs Late  */  
   ActualJobsLate:number,
      /**  Actual Jobs Ontime  */  
   ActualJobsOntime:number,
      /**  What IF Jobs Early  */  
   WIJobsEarly:number,
      /**  What If Jobs Late  */  
   WIJobsLate:number,
      /**  What if Jobs On Time  */  
   WIJobsOnTime:number,
      /**  Change Jobs Early  */  
   ChgJobsEarly:number,
      /**  Change Jobs Late  */  
   ChgJobsLate:number,
      /**  Change Jobs OnTime  */  
   ChgJobsOnTime:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface GetData_output{
   returnObj:Erp_Tablesets_ChangeImpactTableset[],
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
export interface OnChangeParameters_input{
   ds:Erp_Tablesets_ChangeImpactTableset[],
}

export interface OnChangeParameters_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ChangeImpactTableset[],
}
}

