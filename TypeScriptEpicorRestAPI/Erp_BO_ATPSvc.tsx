import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ATPSvc
// Description: Part Tracker , Part Advisor -> Available to Promise screen.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", {
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
   Summary: Invoke method ForecastButtonHandler
   Description: Call this method from Forecast button of ATP screen.
   OperationID: ForecastButtonHandler
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ForecastButtonHandler_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ForecastButtonHandler_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ForecastButtonHandler(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/ForecastButtonHandler", {
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
   Summary: Invoke method OnChangePlantWithDS
   Description: Update the ATP table when changing Plants in Kinetic.
   OperationID: OnChangePlantWithDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePlantWithDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlantWithDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePlantWithDS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/OnChangePlantWithDS", {
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
   Summary: Invoke method OnChangeField
   Description: When the user changes the value of any field except Plant and Part call this method.
   OperationID: OnChangeField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeField(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/OnChangeField", {
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
   Summary: Invoke method VerifyShortDescription
   Description: Validate short description
   OperationID: VerifyShortDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyShortDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyShortDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyShortDescription(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/VerifyShortDescription", {
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
   Summary: Invoke method OnChangePlant
   Description: When the user changes the Plant, call this method.
   OperationID: OnChangePlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/OnChangePlant", {
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
   Summary: Invoke method ProjectedReceipts
   Description: Call this method from Receipts button of ATP screen.
   OperationID: ProjectedReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProjectedReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProjectedReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProjectedReceipts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/ProjectedReceipts", {
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
   Summary: Invoke method ProjectedReceiptsWithDate
   Description: Call this method from Receipts button of ATP screen for Kinetic.
   OperationID: ProjectedReceiptsWithDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProjectedReceiptsWithDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProjectedReceiptsWithDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProjectedReceiptsWithDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/ProjectedReceiptsWithDate", {
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
   Summary: Invoke method SalesOrder
   Description: Call this method from Sales Order button of ATP screen.
   OperationID: SalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/SalesOrder", {
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
   Summary: Invoke method TransferOrder
   Description: Call this method from Transfer Order button of ATP screen.
   OperationID: TransferOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TransferOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransferOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransferOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/TransferOrder", {
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
   Summary: Invoke method getPlanningAttributeSet
   Description: Get the planning attribute set for an attribute set
   OperationID: getPlanningAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getPlanningAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getPlanningAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getPlanningAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/getPlanningAttributeSet", {
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
   Summary: Invoke method FindPlanningAttributeSet
   OperationID: FindPlanningAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPlanningAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPlanningAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPlanningAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/FindPlanningAttributeSet", {
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
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAttributeSetIDFromRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/UpdateAttributeSetIDFromRevisionNum", {
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
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/PartsAttributeClassHasRevisionAndIsMRPTracked", {
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
   Summary: Invoke method HasMRPPlanningAttribute
   Description: Return true if the Part has an MRP Planning Attribute, thus requiring an Attribute Set to be selected
   OperationID: HasMRPPlanningAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasMRPPlanningAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasMRPPlanningAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasMRPPlanningAttribute(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/HasMRPPlanningAttribute", {
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
export interface Erp_Tablesets_ATPForecastRow{
   Company:string,
   ForeDate:string,
   ForeQty:number,
   Name:string,
   ConsumedQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ATPForecastTableset{
   ATPForecast:Erp_Tablesets_ATPForecastRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ATPOrderRelTableset{
   OrderRel:Erp_Tablesets_OrderRelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ATPTFOrderRow{
   Company:string,
   NeedByDate:string,
   TFOrdNum:string,
   TFOrdLine:number,
   PartNum:string,
   Quantity:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ATPTFOrderTableset{
   ATPTFOrder:Erp_Tablesets_ATPTFOrderRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ATPTableset{
   AvailableToPromiseHead:Erp_Tablesets_AvailableToPromiseHeadRow[],
   AvailableToPromise:Erp_Tablesets_AvailableToPromiseRow[],
   CustomATP:Erp_Tablesets_CustomATPRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AvailableToPromiseHeadRow{
   Company:string,
   PartNum:string,
   Plant:string,
      /**  Available to method.  Valid values are "Q" and "D"  */  
   ATPMethod:string,
   SellingATPQty:number,
   ATPDate:string,
   OurATPQty:number,
   StartAtDate:string,
   OnHandQty:number,
      /**  Radio set with valid values as "S" and "O"  */  
   UMFactor:string,
   DaysBefore:number,
   DaysAfter:number,
      /**  Set to No if it needs to be disabled in the UI.  */  
   PlantEnabled:boolean,
      /**  Lead Time from the Part Plant record.  */  
   LeadTime:number,
      /**  Calculated at Today + LeadTime.  */  
   LeadDate:string,
      /**  ReceiveTime  */  
   ReceiveTime:number,
   SalesUOM:string,
   OurUOM:string,
   OurUM:string,
   SellUM:string,
   EnableAttrSetSearch:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AvailableToPromiseRow{
   Company:string,
   PartNum:string,
   Plant:string,
   DueDate:string,
   ForeQty:number,
   OrderQty:number,
   ProdQty:number,
   MpsQty:number,
   RcvQty:number,
      /**  Cumulative ATP Qty  */  
   ATPQty:number,
   ConsumedQty:number,
   TOrderQty:number,
      /**  Selling factor Forecast Qty  */  
   sfForeQty:number,
      /**  Selling Factor Order Qty  */  
   sfOrderQty:number,
      /**  Selling Factor Prod Qty  */  
   sfProdQty:number,
      /**  Selling Factor MPS Qty  */  
   sfMpsQty:number,
      /**  Selling Factor Recipt Qty  */  
   sfRcvQty:number,
      /**  Selling Factor ATP Qty  */  
   sfATPQty:number,
      /**  Selling Factor Consumed Qty  */  
   sfConsumedQty:number,
   sfTOrderQty:number,
      /**  DiscreteATPQty  */  
   DiscreteATPQty:number,
      /**  Selling Factor Discrete ATP Qty  */  
   sfDiscreteATPQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustomATPRow{
      /**  Cumulative ATP Qty  */  
   ATPQty:number,
   ForeQty:number,
   MpsQty:number,
   OrderQty:number,
   ProdQty:number,
      /**  Caption for the row. Will show a date formatted as a string.  */  
   RowCaption:string,
      /**  Radio set with valid values as "S" and "O". Taken from AvailableToPromiseHead.UMFactor.  */  
   SalesQtyOurQty:string,
      /**  Selling Factor ATP Qty  */  
   sfATPQty:number,
      /**  Selling factor Forecast Qty  */  
   sfForeQty:number,
      /**  Selling Factor MPS Qty  */  
   sfMpsQty:number,
      /**  Selling Factor Order Qty  */  
   sfOrderQty:number,
      /**  Selling Factor Prod Qty  */  
   sfProdQty:number,
   sfTOrderQty:number,
   TOrderQty:number,
   DueDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderRelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   ShipViaCode:string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   FirmRelease:boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   Make:boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   OurJobQty:number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   OurJobShippedQty:number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   VoidRelease:boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   PartNum:string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   RevisionNum:string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   TaxExempt:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   SellingReqQty:number,
      /**  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   SellingJobQty:number,
      /**  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  */  
   SellingJobShippedQty:number,
      /**  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   SellingStockQty:number,
      /**  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  */  
   SellingStockShippedQty:number,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  */  
   StagingWarehouseCode:string,
      /**  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  Indicates if this order release is linked to an inter-company PO release.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   ICPORelNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  A link to the demand schedule that created/updated this OrderRel.  */  
   ScheduleNumber:string,
      /**  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  */  
   MarkForNum:string,
      /**  Full name for the drop shipment.  */  
   DropShipName:string,
      /**  RAN Number.  Used for informational purposes.  Supplied by EDI.  */  
   RAN:string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   DemandReference:string,
      /**  Indicates if the demand schedule that created/updated this order release has been rejected.  */  
   DemandSchedRejected:boolean,
      /**  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  */  
   DatePickTicketPrinted:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  The location within the customer shipto address.  For future use.  */  
   Location:string,
      /**  The code of the transport routing/time. For future use.  */  
   TransportID:string,
      /**  Ship the good by this time.  */  
   ShipbyTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipment country  */  
   OTSCountryNum:number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   SubShipTo:string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   ShipRouting:string,
      /**  This field identifies Buy To Order releases.  */  
   BuyToOrder:boolean,
      /**  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  */  
   VendorNum:number,
      /**  Supplier Purchase Point. Used only for Buy To Order releases.  */  
   PurPoint:string,
      /**  This field identifies Drop Ship releases. Used only for Buy To Order releases.  */  
   DropShip:boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PONum:number,
      /**  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   POLine:number,
      /**  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PORelNum:number,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  True if Customer or ShipTo record was created using the OTS info.  */  
   OTSCustSaved:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   IUM:string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   SalesUM:string,
      /**  Status of Order Release  */  
   RelStatus:string,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  Previous Need By Date  */  
   PrevNeedByDate:string,
      /**  Previous Require Date  */  
   PrevReqDate:string,
      /**  Previous Ship To Num  */  
   PrevShipToNum:string,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
   OTMFName:string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   OTMFAddress1:string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   OTMFAddress2:string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   OTMFAddress3:string,
      /**  City portion of the One Time Mark For address.  */  
   OTMFCity:string,
      /**  The state or province portion of the One Time Mark For address.  */  
   OTMFState:string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   OTMFZIP:string,
      /**  One Time Mark For Contact Name  */  
   OTMFContact:string,
      /**  Fax number for the One Time Mark For.  */  
   OTMFFaxNum:string,
      /**  Phone number for the One Time Mark For  */  
   OTMFPhoneNum:string,
      /**  Country number for the One Time Mark For  */  
   OTMFCountryNum:number,
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  WIOrderLine  */  
   WIOrderLine:string,
      /**  WIOrder  */  
   WIOrder:string,
      /**  WebSKU  */  
   WebSKU:string,
      /**  ShipOvers  */  
   ShipOvers:boolean,
      /**  WIItemPrice  */  
   WIItemPrice:number,
      /**  WIItemShipCost  */  
   WIItemShipCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  PhaseID  */  
   PhaseID:string,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  WasRecInvoiced  */  
   WasRecInvoiced:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  This flag indicates if the sales order release is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  One Time ShipTo email address.  */  
   OTSEMailAddress:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Indicates if the release should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   AvailableQuantity:number,
      /**  BuyOverride  */  
   BuyOverride:boolean,
      /**  The message returned when checking a customer credit limit.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Is OTS allowed by the Sold to Customer?  */  
   CustAllowOTS:boolean,
      /**  True when Customer allows shipping to a Third-Party  */  
   CustomerAllowShipTo3:boolean,
   CustomerCustID:string,
   CustomerName:string,
   DisablePlantWhse:boolean,
   DocSelfAssessTax:number,
   DocTotalTax:number,
   DocWithholdTax:number,
      /**  DropShipOverride  */  
   DropShipOverride:boolean,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
'CP' = Cost Plus
The default is Customer Shipment.  */  
   DspInvMeth:string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   DspRevMethod:string,
   EnableBuyToOrder:boolean,
   EnableMake:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
      /**  ExistPOSugg, external field to show/hide an epishape  */  
   ExistPOSugg:boolean,
   HdrOTS:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Inventory UOM that the Order Release is allocated against. It is the similare column to the OrderDtl InvtyUOM and should always has the same value as in OrderDtl  */  
   InvtyUOM:string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  LinkToPONum, external field to show/hide an epishape  */  
   LinkToPONum:boolean,
   MakeOverride:boolean,
      /**  The formatted mark for address  */  
   MarkForAddrFormatted:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
      /**  The flag based on the user anwer if Ship To of the release is supposed be changed but Tax info is not changed because of the conflict in tax pricing  */  
   NoRelTaxRgnChange:boolean,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
   OnHandQuantity:number,
   OTSSaved:boolean,
      /**  OTS Tax Liability Code (Order Release)  */  
   OTSTaxRegionCode:string,
   PartExists:boolean,
      /**  If the phase has been recognized or invoiced.  */  
   PhaseWasRecInvoiced:boolean,
   ProjectID:string,
   ReleaseStatus:string,
      /**  the flag to indicate if all previously creaded manually added and manual tax relcords related to Order line release should be deleted if the user populates Tax Exempt field.  */  
   RemoveManAdTax:boolean,
   Rpt1SelfAssessTax:number,
   Rpt1TotalTax:number,
   Rpt1WithholdTax:number,
   Rpt2SelfAssessTax:number,
   Rpt2TotalTax:number,
   Rpt2WithholdTax:number,
   Rpt3SelfAssessTax:number,
   Rpt3TotalTax:number,
   Rpt3WithholdTax:number,
      /**  SalesOrderLinked  */  
   SalesOrderLinked:boolean,
      /**  Self-Assessed Tax  */  
   SelfAssessTax:number,
      /**  Selling Factor for display only  */  
   SellingFactor:number,
      /**  Selling Factor Direction for display oly  */  
   SellingFactorDirection:string,
      /**  The formatted ship to address  */  
   ShipToAddressFormatted:string,
   ShipToAddressList:string,
   ShipToContactEMailAddress:string,
   ShipToContactName:string,
   ShipToSelected:boolean,
   SNEnable:boolean,
   ThisRelInvtyQty:number,
   TotalJobStockShipped:number,
      /**  Invoice Tax  */  
   TotalTax:number,
   UpdateMarkForRecords:boolean,
   VoidOrder:boolean,
      /**  Withholding Tax  */  
   WithholdTax:number,
   AllowTaxCodeUpd:boolean,
      /**  Allow enable/disable for the button Attibutes in Order Release  */  
   EnableDynAttrButton:boolean,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on release.  */  
   AttributeMismatch:boolean,
      /**  The total allocated quantity for this release.  */  
   AllocatedQuantity:number,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this release is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowAllocationQueueActions:boolean,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   MarkForNumInactive:boolean,
   MFCustNumInactive:boolean,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OTMFCountryDescription:string,
   OTSCntryISOCode:string,
   OTSCntryEUMember:boolean,
   OTSCntryDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PlantName:string,
   PurPointAddress3:string,
   PurPointZip:string,
   PurPointName:string,
   PurPointCountry:string,
   PurPointAddress1:string,
   PurPointState:string,
   PurPointCity:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   ShipToNumInactive:boolean,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TaxRegionCodeDescription:string,
   TPShipToName:string,
   TPShipToBTName:string,
   TPShipToCustID:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProjectedReceiptsRow{
   Company:string,
   PartNum:string,
   Plant:string,
   DueDate:string,
   Type:string,
   Source:string,
   ReceivedQty:number,
   JobNum:string,
   AssemblySeq:number,
   PONum:number,
   POLine:number,
   PORelNum:number,
   ReqDueDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProjectedReceiptsTableset{
   ProjectedReceipts:Erp_Tablesets_ProjectedReceiptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param attributeSetID
   */  
export interface FindPlanningAttributeSet_input{
   partNum:string,
   attributeSetID:number,
}

export interface FindPlanningAttributeSet_output{
parameters : {
      /**  output parameters  */  
   attributeSetShortDesc:string,
   attributeSetDesc:string,
   newAttributeSetID:number,
}
}

   /** Required : 
      @param pcPartNum
      @param pcPlant
      @param pdtStartDate
      @param attributeSetID
   */  
export interface ForecastButtonHandler_input{
      /**  Part number.  */  
   pcPartNum:string,
      /**  Plant  */  
   pcPlant:string,
      /**  Start Date  */  
   pdtStartDate:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface ForecastButtonHandler_output{
   returnObj:Erp_Tablesets_ATPForecastTableset[],
}

   /** Required : 
      @param partNum
   */  
export interface HasMRPPlanningAttribute_input{
      /**  Part  */  
   partNum:string,
}

export interface HasMRPPlanningAttribute_output{
   returnObj:boolean,
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
      @param pcFieldName
      @param pcPartNum
      @param pcPlant
      @param ds
   */  
export interface OnChangeField_input{
      /**  Field name from where this method is called.  */  
   pcFieldName:string,
      /**  Part number.  */  
   pcPartNum:string,
      /**  Plant  */  
   pcPlant:string,
   ds:Erp_Tablesets_ATPTableset[],
}

export interface OnChangeField_output{
parameters : {
      /**  output parameters  */  
   pcRowIdent:string,
   ds:Erp_Tablesets_ATPTableset[],
}
}

   /** Required : 
      @param partNum
      @param plant
      @param attributeSetID
      @param ds
   */  
export interface OnChangePlantWithDS_input{
   partNum:string,
   plant:string,
   attributeSetID:number,
   ds:Erp_Tablesets_ATPTableset[],
}

export interface OnChangePlantWithDS_output{
parameters : {
      /**  output parameters  */  
   startAtDate:string,
   ds:Erp_Tablesets_ATPTableset[],
}
}

   /** Required : 
      @param pcPartNum
      @param pcPlant
      @param attributeSetID
   */  
export interface OnChangePlant_input{
      /**  Part number.  */  
   pcPartNum:string,
      /**  Plant  */  
   pcPlant:string,
      /**  AttributeSetID  */  
   attributeSetID:number,
}

export interface OnChangePlant_output{
   returnObj:Erp_Tablesets_ATPTableset[],
}

   /** Required : 
      @param attrClassID
   */  
export interface PartsAttributeClassHasRevisionAndIsMRPTracked_input{
      /**  current Attribute Class ID  */  
   attrClassID:string,
}

export interface PartsAttributeClassHasRevisionAndIsMRPTracked_output{
   returnObj:boolean,
}

   /** Required : 
      @param pcPartNum
      @param pcPlant
      @param pdtStartDate
   */  
export interface ProjectedReceiptsWithDate_input{
      /**  Part number.  */  
   pcPartNum:string,
      /**  Plant  */  
   pcPlant:string,
   pdtStartDate:string,
}

export interface ProjectedReceiptsWithDate_output{
   returnObj:Erp_Tablesets_ProjectedReceiptsTableset[],
}

   /** Required : 
      @param pcPartNum
      @param pcPlant
      @param attributeSetID
   */  
export interface ProjectedReceipts_input{
      /**  Part number.  */  
   pcPartNum:string,
      /**  Plant  */  
   pcPlant:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface ProjectedReceipts_output{
   returnObj:Erp_Tablesets_ProjectedReceiptsTableset[],
}

   /** Required : 
      @param pcPartNum
      @param pcPlant
      @param pdtStartDate
      @param attributeSetID
   */  
export interface SalesOrder_input{
      /**  Part number.  */  
   pcPartNum:string,
      /**  Plant  */  
   pcPlant:string,
      /**  Start Date  */  
   pdtStartDate:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface SalesOrder_output{
   returnObj:Erp_Tablesets_ATPOrderRelTableset[],
}

   /** Required : 
      @param pcPartNum
      @param pcPlant
      @param pdtStartDate
      @param attributeSetID
   */  
export interface TransferOrder_input{
      /**  Part number.  */  
   pcPartNum:string,
      /**  Plant  */  
   pcPlant:string,
      /**  Start Date  */  
   pdtStartDate:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface TransferOrder_output{
   returnObj:Erp_Tablesets_ATPTFOrderTableset[],
}

   /** Required : 
      @param partNum
      @param revisionNum
   */  
export interface UpdateAttributeSetIDFromRevisionNum_input{
      /**  current part number  */  
   partNum:string,
      /**  new revision selected  */  
   revisionNum:string,
}

export interface UpdateAttributeSetIDFromRevisionNum_output{
parameters : {
      /**  output parameters  */  
   attributeSetID:number,
}
}

   /** Required : 
      @param attrClassID
      @param shortAttrdesc
   */  
export interface VerifyShortDescription_input{
   attrClassID:string,
   shortAttrdesc:string,
}

export interface VerifyShortDescription_output{
parameters : {
      /**  output parameters  */  
   attributeSetID:number,
   longDescription:string,
}
}

   /** Required : 
      @param attributeSetID
   */  
export interface getPlanningAttributeSet_input{
      /**  Attribute Set ID  */  
   attributeSetID:number,
}

export interface getPlanningAttributeSet_output{
   returnObj:number,
}

