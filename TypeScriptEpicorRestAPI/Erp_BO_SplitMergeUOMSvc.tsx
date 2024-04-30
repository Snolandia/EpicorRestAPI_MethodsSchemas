import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SplitMergeUOMSvc
// Description: SplitMergeUOM Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/$metadata", {
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
   Summary: Invoke method CalculateRemainQty
   Description: Calculates The Remaining Qty
   OperationID: CalculateRemainQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateRemainQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateRemainQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateRemainQty(requestBody:CalculateRemainQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateRemainQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/CalculateRemainQty", {
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
         resolve(data as CalculateRemainQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:GetPartXRefInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartXRefInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/GetPartXRefInfo", {
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
         resolve(data as GetPartXRefInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSplitMergeHeadData
   Description: Gets the default values for the ttSMHdr data table based on the part
number entered.
   OperationID: GetSplitMergeHeadData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSplitMergeHeadData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSplitMergeHeadData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSplitMergeHeadData(requestBody:GetSplitMergeHeadData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSplitMergeHeadData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/GetSplitMergeHeadData", {
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
         resolve(data as GetSplitMergeHeadData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBinNum
   Description: Used to verify if the selected Bin is valid for the selected warehouse
   OperationID: OnChangeBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBinNum(requestBody:OnChangeBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/OnChangeBinNum", {
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
         resolve(data as OnChangeBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLotNum
   Description: Used to default the Lot Number when the BinNum has been changed
   OperationID: OnChangeLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLotNum(requestBody:OnChangeLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/OnChangeLotNum", {
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
         resolve(data as OnChangeLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeProcType
   Description: Used to create the Split or Merge Records
   OperationID: OnChangeProcType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeProcType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProcType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeProcType(requestBody:OnChangeProcType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeProcType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/OnChangeProcType", {
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
         resolve(data as OnChangeProcType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQuantity
   Description: Used to verify that quantity to split or merge
   OperationID: OnChangeQuantity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuantity(requestBody:OnChangeQuantity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQuantity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/OnChangeQuantity", {
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
         resolve(data as OnChangeQuantity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUOM
   Description: Used to return a list of valid UOM to process the split or merge
   OperationID: OnChangeUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUOM(requestBody:OnChangeUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/OnChangeUOM", {
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
         resolve(data as OnChangeUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWarehouse
   Description: Used to verify that selected warehouse is valid for the
part and current plant and to default the Bin and Lot Number when the Warehouse has been changed
   OperationID: OnChangeWarehouse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWarehouse(requestBody:OnChangeWarehouse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeWarehouse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/OnChangeWarehouse", {
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
         resolve(data as OnChangeWarehouse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessType
   Description: Runs the Split or Merge Process
   OperationID: ProcessType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessType(requestBody:ProcessType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/ProcessType", {
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
         resolve(data as ProcessType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeInventoryTest
   Description: Negative inventory test
   OperationID: NegativeInventoryTest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryTest(requestBody:NegativeInventoryTest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NegativeInventoryTest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/NegativeInventoryTest", {
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
         resolve(data as NegativeInventoryTest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshOnHandQty
   Description: Update OnHandQty after splitting/merging the Quantity
   OperationID: RefreshOnHandQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshOnHandQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshOnHandQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshOnHandQty(requestBody:RefreshOnHandQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshOnHandQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SplitMergeUOMSvc/RefreshOnHandQty", {
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
         resolve(data as RefreshOnHandQty_output)
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
      @param partNum
      @param ds
   */  
export interface CalculateRemainQty_input{
      /**  Part number to split or merge.  */  
   partNum:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface CalculateRemainQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

export interface Erp_Tablesets_SMDtlRow{
   Company:string,
   PartNum:string,
   WarehouseCode:string,
   BinNum:string,
   LotNum:string,
   OnHandQty:number,
   Quantity:number,
   UOM:string,
   UOMDescription:string,
   ConvFactor:number,
   ConvFactorUOM:string,
      /**  Quantity already allocated  */  
   AllocatedQty:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SMHdrRow{
   Company:string,
   PartNum:string,
   WarehouseCode:string,
   BinNum:string,
   LotNum:string,
      /**  S=Split; M=Merge  */  
   ProcessType:string,
   OnHandQty:number,
   Quantity:number,
   UOM:string,
   TransDate:string,
   BinDescription:string,
   LotDescription:string,
   PartDescription:string,
   UOMDescription:string,
   WarehouseDesc:string,
   EnableLot:boolean,
   OnHandUOM:string,
   OnHandUOMDesc:string,
   RemainQty:number,
   RemainUOM:string,
   TransQty:number,
   TransUOM:string,
      /**  Quantity already allocated for the Part to be split/merged  */  
   AllocatedQty:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SplitMergeUOMTableset{
   SMHdr:Erp_Tablesets_SMHdrRow[],
   SMDtl:Erp_Tablesets_SMDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param SysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param partNum
      @param ds
   */  
export interface GetSplitMergeHeadData_input{
      /**  Part number to split or merge.  */  
   partNum:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface GetSplitMergeHeadData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
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
      @param partNum
      @param ds
   */  
export interface NegativeInventoryTest_input{
   partNum:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   negQtyAction:string,
   negInvMessage:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param partNum
      @param binNum
      @param ds
   */  
export interface OnChangeBinNum_input{
      /**  Part number to split or merge.  */  
   partNum:string,
      /**  Bin Number.  */  
   binNum:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface OnChangeBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param partNum
      @param lotNum
      @param ds
   */  
export interface OnChangeLotNum_input{
      /**  Part number to split or merge.  */  
   partNum:string,
      /**  Lot Number.  */  
   lotNum:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface OnChangeLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param partNum
      @param processType
      @param ds
   */  
export interface OnChangeProcType_input{
      /**  Part number to split or merge.  */  
   partNum:string,
      /**  Process Type.  */  
   processType:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface OnChangeProcType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param partNum
      @param dQuantity
      @param ds
   */  
export interface OnChangeQuantity_input{
      /**  Part number to split or merge.  */  
   partNum:string,
      /**  Quantity.  */  
   dQuantity:number,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface OnChangeQuantity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param partNum
      @param uOMCode
      @param ds
   */  
export interface OnChangeUOM_input{
      /**  Part number to split or merge.  */  
   partNum:string,
      /**  Unit of Messure.  */  
   uOMCode:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface OnChangeUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param partNum
      @param whseCode
      @param ds
   */  
export interface OnChangeWarehouse_input{
      /**  Part number to split or merge.  */  
   partNum:string,
      /**  Warehouse Code.  */  
   whseCode:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface OnChangeWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param partNum
      @param ds
   */  
export interface ProcessType_input{
      /**  Part number to split or merge.  */  
   partNum:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface ProcessType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

   /** Required : 
      @param type
      @param ds
   */  
export interface RefreshOnHandQty_input{
      /**  The process type. S = splitting, M = merging  */  
   type:string,
   ds:Erp_Tablesets_SplitMergeUOMTableset[],
}

export interface RefreshOnHandQty_output{
   returnObj:Erp_Tablesets_SplitMergeUOMTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SplitMergeUOMTableset,
}
}

