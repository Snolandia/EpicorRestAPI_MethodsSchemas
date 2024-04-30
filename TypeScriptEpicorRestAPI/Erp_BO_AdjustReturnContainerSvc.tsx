import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.AdjustReturnContainerSvc
// Description: Allows user to adjust in or out returnable containers
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/$metadata", {
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
   Summary: Invoke method ChangeBinNum
   Description: Called when bin num is changed
   OperationID: ChangeBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBinNum(requestBody:ChangeBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/ChangeBinNum", {
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
         resolve(data as ChangeBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeQuantity
   Description: Called when quantity is changed - retrieves, validates and sets reason codes based on negative or positive qty
   OperationID: ChangeQuantity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQuantity(requestBody:ChangeQuantity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeQuantity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/ChangeQuantity", {
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
         resolve(data as ChangeQuantity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeWarehouse
   Description: Called when quantity is changed - retrieves, validates and sets reason codes based on negative or positive qty
   OperationID: ChangeWarehouse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeWarehouse(requestBody:ChangeWarehouse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeWarehouse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/ChangeWarehouse", {
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
         resolve(data as ChangeWarehouse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackageControlEnabled
   Description: Checks whether Package Control is enabled.
   OperationID: CheckPackageControlEnabled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageControlEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackageControlEnabled(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPackageControlEnabled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/CheckPackageControlEnabled", {
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
         resolve(data as CheckPackageControlEnabled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAdjustReturnContainer
   Description: Gets the default values for the AdjustReturnContainer data table based on the part
number entered.
   OperationID: GetAdjustReturnContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAdjustReturnContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAdjustReturnContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAdjustReturnContainer(requestBody:GetAdjustReturnContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAdjustReturnContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/GetAdjustReturnContainer", {
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
         resolve(data as GetAdjustReturnContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAdjustReturnContainerBrw
   Description: Populates adjust return container inventory on-hand qty dataset when warehouse is selected
   OperationID: GetAdjustReturnContainerBrw
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAdjustReturnContainerBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAdjustReturnContainerBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAdjustReturnContainerBrw(requestBody:GetAdjustReturnContainerBrw_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAdjustReturnContainerBrw_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/GetAdjustReturnContainerBrw", {
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
         resolve(data as GetAdjustReturnContainerBrw_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMatchingCount
   Description: Gets the number of matches for the given criteria and populates buffer if only one match found.
Can pass one of either PartNum, ShipToPartNum, PkgCode, or both PartNum and PkgCode
   OperationID: GetMatchingCount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMatchingCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchingCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMatchingCount(requestBody:GetMatchingCount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMatchingCount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/GetMatchingCount", {
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
         resolve(data as GetMatchingCount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeInventoryAllocationsTest
   OperationID: NegativeInventoryAllocationsTest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NegativeInventoryAllocationsTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryAllocationsTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryAllocationsTest(requestBody:NegativeInventoryAllocationsTest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NegativeInventoryAllocationsTest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/NegativeInventoryAllocationsTest", {
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
         resolve(data as NegativeInventoryAllocationsTest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreSetAdjustReturnContainer
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreSetAdjustReturnContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreSetAdjustReturnContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetAdjustReturnContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreSetAdjustReturnContainer(requestBody:PreSetAdjustReturnContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreSetAdjustReturnContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/PreSetAdjustReturnContainer", {
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
         resolve(data as PreSetAdjustReturnContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetAdjustReturnContainer
   OperationID: SetAdjustReturnContainer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetAdjustReturnContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAdjustReturnContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetAdjustReturnContainer(requestBody:SetAdjustReturnContainer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetAdjustReturnContainer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/SetAdjustReturnContainer", {
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
         resolve(data as SetAdjustReturnContainer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AdjustReturnContainerSvc/GetAvailTranDocTypes", {
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
         resolve(data as GetAvailTranDocTypes_output)
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
      @param binNum
      @param ds
   */  
export interface ChangeBinNum_input{
      /**  Proposed value  */  
   binNum:string,
   ds:Erp_Tablesets_AdjustReturnContainerTableset[],
}

export interface ChangeBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AdjustReturnContainerTableset,
}
}

   /** Required : 
      @param qty
      @param ds
   */  
export interface ChangeQuantity_input{
      /**  Proposed qty  */  
   qty:number,
   ds:Erp_Tablesets_AdjustReturnContainerTableset[],
}

export interface ChangeQuantity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AdjustReturnContainerTableset,
}
}

   /** Required : 
      @param warehouseCode
      @param ds
   */  
export interface ChangeWarehouse_input{
      /**  Proposed value  */  
   warehouseCode:string,
   ds:Erp_Tablesets_AdjustReturnContainerTableset[],
}

export interface ChangeWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AdjustReturnContainerTableset,
}
}

export interface CheckPackageControlEnabled_output{
      /**  True if enabled/false if not  */  
   returnObj:boolean,
}

export interface Erp_Tablesets_AdjustReturnContainerBrwRow{
      /**  Company  */  
   Company:string,
      /**  Bin number  */  
   BinNum:string,
      /**  On hand quantity  */  
   OnHandQty:number,
      /**  Non nettable flag  */  
   NonNettable:boolean,
      /**  Lot number  */  
   LotNum:string,
      /**  WareHouse Bin description.  */  
   WhseBinDesc:string,
   StkUOMCode:string,
   StkUOMDesc:string,
      /**  The PartBin.OnHandQty expressed in Part Base UOM  */  
   BaseOnHandQty:number,
      /**  Unit of Measure to qualifiy BaseOnHandQty. This is the Part Base UOM.  */  
   BaseOnHandUOM:string,
   WarehouseCode:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AdjustReturnContainerBrwTableset{
   AdjustReturnContainerBrw:Erp_Tablesets_AdjustReturnContainerBrwRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AdjustReturnContainerConflictRow{
   PartNum:string,
   PartDescription:string,
   PkgCode:string,
   PkgCodeDesc:string,
   ShipToPartNum:string,
   ShipToPartNumDesc:string,
   CustID:string,
   CustName:string,
   ShipToNum:string,
   ShipToName:string,
   ShipToSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AdjustReturnContainerRow{
   Company:string,
   WarehouseCode:string,
   OnHandQty:number,
   BinNum:string,
   AdjustQuantity:number,
   ReasonCode:string,
   Reference:string,
   UnitOfMeasure:string,
   TransDate:string,
   ReasonType:string,
   AllowNegQty:boolean,
   StkUOMCode:string,
   OnHandUOM:string,
   PartDescription:string,
   WarehouseDescription:string,
   ReasonCodeDescription:string,
   WhseBinDescription:string,
   Plant:string,
   PartNum:string,
   PkgCode:string,
   PkgCodeDesc:string,
   LegalNumberMessage:string,
   ShipToPartNum:string,
   ShipToPartNumDesc:string,
   ShipToSeq:number,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AdjustReturnContainerTableset{
   AdjustReturnContainer:Erp_Tablesets_AdjustReturnContainerRow[],
   AdjustReturnContainerConflict:Erp_Tablesets_AdjustReturnContainerConflictRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param partNum
      @param warehouseCode
   */  
export interface GetAdjustReturnContainerBrw_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Warehouse code used to get bin information.  */  
   warehouseCode:string,
}

export interface GetAdjustReturnContainerBrw_output{
   returnObj:Erp_Tablesets_AdjustReturnContainerBrwTableset[],
}

   /** Required : 
      @param partNum
      @param pkgCode
      @param shipToSeq
   */  
export interface GetAdjustReturnContainer_input{
      /**  Part number  */  
   partNum:string,
      /**  Pkg Code  */  
   pkgCode:string,
      /**  ShipToSeq from PackingShipTo (optional)  */  
   shipToSeq:number,
}

export interface GetAdjustReturnContainer_output{
   returnObj:Erp_Tablesets_AdjustReturnContainerTableset[],
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param partNum
      @param shipToPartNum
      @param pkgCode
   */  
export interface GetMatchingCount_input{
      /**  Part number to search against Part  */  
   partNum:string,
      /**  Part number to search against ShipToPacking  */  
   shipToPartNum:string,
      /**  PkgCode search against Packing and PackingPlant  */  
   pkgCode:string,
}

export interface GetMatchingCount_output{
   returnObj:Erp_Tablesets_AdjustReturnContainerTableset[],
parameters : {
      /**  output parameters  */  
   matches:number,
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
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcDimCode
      @param pdDimConvFactor
      @param ipSellingQuantity
   */  
export interface NegativeInventoryAllocationsTest_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcDimCode:string,
   pdDimConvFactor:number,
   ipSellingQuantity:number,
}

export interface NegativeInventoryAllocationsTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
   opAllocAction:string,
   opAllocWarning:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreSetAdjustReturnContainer_input{
   ds:Erp_Tablesets_AdjustReturnContainerTableset[],
}

export interface PreSetAdjustReturnContainer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AdjustReturnContainerTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface SetAdjustReturnContainer_input{
   ds:Erp_Tablesets_AdjustReturnContainerTableset[],
}

export interface SetAdjustReturnContainer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AdjustReturnContainerTableset,
}
}

