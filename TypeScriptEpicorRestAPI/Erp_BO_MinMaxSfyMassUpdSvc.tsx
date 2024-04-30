import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MinMaxSfyMassUpdSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata", {
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
   Summary: Invoke method GetHistoryWindow
   Description: This method is used to get the History Window ONLY. It will not calculate any other value.
This is used mostly for BLTester to compare results.
   OperationID: GetHistoryWindow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHistoryWindow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHistoryWindow(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetHistoryWindow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/GetHistoryWindow", {
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
         resolve(data as GetHistoryWindow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSingleHistoryWindow
   OperationID: GetSingleHistoryWindow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSingleHistoryWindow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSingleHistoryWindow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSingleHistoryWindow(requestBody:GetSingleHistoryWindow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSingleHistoryWindow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/GetSingleHistoryWindow", {
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
         resolve(data as GetSingleHistoryWindow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMinMaxSafetyRecords
   OperationID: GetMinMaxSafetyRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMinMaxSafetyRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMinMaxSafetyRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMinMaxSafetyRecords(requestBody:GetMinMaxSafetyRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMinMaxSafetyRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/GetMinMaxSafetyRecords", {
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
         resolve(data as GetMinMaxSafetyRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateSelected
   OperationID: CalculateSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateSelected(requestBody:CalculateSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/CalculateSelected", {
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
         resolve(data as CalculateSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassUpdate
   OperationID: MassUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MassUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassUpdate(requestBody:MassUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MassUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/MassUpdate", {
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
         resolve(data as MassUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMinMaxSafetyValues
   OperationID: ValidateMinMaxSafetyValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMinMaxSafetyValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMinMaxSafetyValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMinMaxSafetyValues(requestBody:ValidateMinMaxSafetyValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMinMaxSafetyValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/ValidateMinMaxSafetyValues", {
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
         resolve(data as ValidateMinMaxSafetyValues_output)
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
      @param ds
      @param cutOffDate
   */  
export interface CalculateSelected_input{
   ds:Erp_Tablesets_MinMaxSfyMassUpdTableset[],
   cutOffDate:string,
}

export interface CalculateSelected_output{
   returnObj:Erp_Tablesets_MinMaxSfyMassUpdTableset[],
}

export interface Erp_Tablesets_MinMaxSfyMassUpdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.  */  
   ClassID:string,
      /**  Calculated Field of MMSInclude. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  */  
   CalcMMSInclude:boolean,
      /**  Calculated Field of MMSSales. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  */  
   CalcMMSSales:boolean,
      /**  Calculated Field of MMSIssue. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  */  
   CalcMMSIssue:boolean,
      /**  Calculated Field of MMSHistory. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  */  
   CalcMMSHistory:number,
      /**  Sum of all TranQty from PartTran STK-CUS records for a specific Company/Site/Part  */  
   SaleQty:number,
      /**  Sum of all TranQty from PartTran STK-MTL records for a specific Company/Site/Part  */  
   IssueQty:number,
      /**   if CalcMMSSales and CalcMMSIssue then SaleQty + IssueQty
if CalcMMSSales  then SaleQty
if CalcMMSIssue then IssueQty  */  
   TotalUsage:number,
      /**  External field used to select a row for Update or Mass Update  */  
   Select:boolean,
      /**  Full description of the part class.  */  
   ClassDesc:string,
      /**  Describes the Part.  */  
   Description:string,
      /**  Same as PartPlant.ReOrderLevel  */  
   ReOrderLevel:boolean,
      /**  Calculated Field of LeadTime. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  */  
   CalcLeadTime:number,
      /**  Indicates the desired minimum on-hand quantity. Same as PartPlant.MinimumQty. Used for Mass Update.  */  
   MinimumQty:number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand. Same as PartPlant.MaximumQty  */  
   MaximumQty:number,
      /**  Safety quantity is a "purchasing cushion" limit. Same as PartPlant.SafetyQty  */  
   SafetyQty:number,
      /**  It will be calculated as DailyUsage * CalcLeadTime  */  
   ProposedMin:number,
      /**  It will be calculated as (ProposedMin * CalcMMSMaxFactor) + ProposedSafety  */  
   ProposedMax:number,
      /**  It will be calculated as if(CalcMMSSafetyFactor > 0) then ProposedMin * CalcMMSSafetyFactor / 100 else 0  */  
   ProposedSafety:number,
      /**  It will be calculated as SafetyQty * PartCost  */  
   CurrSafetyValue:number,
      /**  It will be calculated as ProposedSafety * PartCost  */  
   NewSafetyValue:number,
      /**  it will be calculated as NewSafetyValue - CurrSafetyValue  */  
   SafetyCostChange:number,
      /**  It will be calculated as MinimumQty * PartCost  */  
   CurrMinValue:number,
      /**  It will be calculated as MaximumQty * PartCost  */  
   CurrMaxValue:number,
      /**  It will be calculated as ProposedMin * PartCost  */  
   NewMinValue:number,
      /**  It will be calculated as ProposedMax * PartCost  */  
   NewMaxValue:number,
      /**  It will be calculated as NewMinValue - CurrMinValue  */  
   MinCostChange:number,
      /**  It will be calculated as NewMaxValue - CurrMaxValue  */  
   MaxCostChange:number,
      /**  Calculated Field of MMSSafetyFactor. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  */  
   CalcMMSSafetyFactor:number,
      /**  Calculated Field of MMSMaxFactor. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  */  
   CalcMMSMaxFactor:number,
      /**  It will be calculated as if(CalcLeadTime = 0 and TotalUsage <= 0) then 0 else TotalUsage / CalcMMSHistory  */  
   DailyUsage:number,
   CostMethod:string,
   CostID:string,
   PartCost:number,
      /**  Contains the value from PartPlant.LeadTime. Used for Mass Update option.  */  
   PartLeadTime:number,
      /**  A readonly column that contains PartPlant.MinimumQty value. Used for reference ONLY when user is working with Mass Update option.  */  
   CurrMinimumQty:number,
      /**  A readonly column that contains PartPlant.MaximumQty value. Used for reference ONLY when user is working with Mass Update option.  */  
   CurrMaximumQty:number,
      /**  A readonly column that contains PartPlant.SafetyQty value. Used for reference ONLY when user is working with Mass Update option.  */  
   CurrSafetyQty:number,
      /**  Value from PartPlant.SavedCalculatedUsageQty.  */  
   CalculatedUsageQty:number,
      /**  Value from PartPlant.SavedOnDateTime  */  
   LastUpdate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MinMaxSfyMassUpdTableset{
   MinMaxSfyMassUpd:Erp_Tablesets_MinMaxSfyMassUpdRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetHistoryWindow_output{
   returnObj:Erp_Tablesets_MinMaxSfyMassUpdTableset[],
}

   /** Required : 
      @param classFilter
      @param partFilter
   */  
export interface GetMinMaxSafetyRecords_input{
   classFilter:string,
   partFilter:string,
}

export interface GetMinMaxSafetyRecords_output{
   returnObj:Erp_Tablesets_MinMaxSfyMassUpdTableset[],
}

   /** Required : 
      @param partNum
      @param historyWindow
      @param cutOffDate
   */  
export interface GetSingleHistoryWindow_input{
   partNum:string,
   historyWindow:number,
   cutOffDate:string,
}

export interface GetSingleHistoryWindow_output{
   returnObj:Erp_Tablesets_MinMaxSfyMassUpdTableset[],
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
export interface MassUpdate_input{
   ds:Erp_Tablesets_MinMaxSfyMassUpdTableset[],
}

export interface MassUpdate_output{
}

   /** Required : 
      @param minQty
      @param maxQty
      @param sfyQty
      @param reOrder
   */  
export interface ValidateMinMaxSafetyValues_input{
   minQty:number,
   maxQty:number,
   sfyQty:number,
   reOrder:boolean,
}

export interface ValidateMinMaxSafetyValues_output{
}

