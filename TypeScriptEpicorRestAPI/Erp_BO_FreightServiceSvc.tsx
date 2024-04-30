import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.FreightServiceSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/$metadata", {
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
   Summary: Invoke method BuildCustFreightRequest
   Description: Build the customer freight request
   OperationID: BuildCustFreightRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildCustFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCustFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildCustFreightRequest(requestBody:BuildCustFreightRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildCustFreightRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/BuildCustFreightRequest", {
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
         resolve(data as BuildCustFreightRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateTimeOut
   Description: UpdateTimeOut in http calls
   OperationID: UpdateTimeOut
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateTimeOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateTimeOut(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateTimeOut_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/UpdateTimeOut", {
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
         resolve(data as UpdateTimeOut_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LogManifestMsg
   Description: Create Manifest Log File
   OperationID: LogManifestMsg
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LogManifestMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LogManifestMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LogManifestMsg(requestBody:LogManifestMsg_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LogManifestMsg_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/LogManifestMsg", {
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
         resolve(data as LogManifestMsg_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildGenUnfreightManifest
   Description: UnFreigth Manifest
   OperationID: BuildGenUnfreightManifest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildGenUnfreightManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildGenUnfreightManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildGenUnfreightManifest(requestBody:BuildGenUnfreightManifest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildGenUnfreightManifest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/BuildGenUnfreightManifest", {
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
         resolve(data as BuildGenUnfreightManifest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildMasterPackFreightRequest
   Description: Build the freight request based upon the masterpack
   OperationID: BuildMasterPackFreightRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildMasterPackFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildMasterPackFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildMasterPackFreightRequest(requestBody:BuildMasterPackFreightRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildMasterPackFreightRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/BuildMasterPackFreightRequest", {
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
         resolve(data as BuildMasterPackFreightRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildMiscFreightRequest
   Description: build the miscellaneous shipment freight request
   OperationID: BuildMiscFreightRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildMiscFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildMiscFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildMiscFreightRequest(requestBody:BuildMiscFreightRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildMiscFreightRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/BuildMiscFreightRequest", {
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
         resolve(data as BuildMiscFreightRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildSubFreightRequest
   Description: build the subcontract freight request
   OperationID: BuildSubFreightRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildSubFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildSubFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildSubFreightRequest(requestBody:BuildSubFreightRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildSubFreightRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/BuildSubFreightRequest", {
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
         resolve(data as BuildSubFreightRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildTransFreightRequest
   Description: build the transfer freight request
   OperationID: BuildTransFreightRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildTransFreightRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildTransFreightRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildTransFreightRequest(requestBody:BuildTransFreightRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildTransFreightRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/BuildTransFreightRequest", {
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
         resolve(data as BuildTransFreightRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateFreightedShipment
   Description: Update the freighted shipment
   OperationID: UpdateFreightedShipment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateFreightedShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFreightedShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateFreightedShipment(requestBody:UpdateFreightedShipment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateFreightedShipment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/UpdateFreightedShipment", {
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
         resolve(data as UpdateFreightedShipment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateUnFreightedShipment
   Description: Unfreight a shipment
   OperationID: UpdateUnFreightedShipment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateUnFreightedShipment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateUnFreightedShipment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateUnFreightedShipment(requestBody:UpdateUnFreightedShipment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateUnFreightedShipment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/UpdateUnFreightedShipment", {
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
         resolve(data as UpdateUnFreightedShipment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FreightCarton
   Description: Call for Manifest Freight Carton
   OperationID: FreightCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FreightCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FreightCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FreightCarton(requestBody:FreightCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FreightCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/FreightCarton", {
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
         resolve(data as FreightCarton_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnfreightCarton
   Description: Call for Manifest Unfreight Carton
   OperationID: UnfreightCarton
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnfreightCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnfreightCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnfreightCarton(requestBody:UnfreightCarton_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnfreightCarton_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FreightServiceSvc/UnfreightCarton", {
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
         resolve(data as UnfreightCarton_output)
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
      @param packID
   */  
export interface BuildCustFreightRequest_input{
      /**  Pack Number  */  
   packID:number,
}

export interface BuildCustFreightRequest_output{
   returnObj:Erp_Tablesets_FreightInfoRequestTableset[],
}

   /** Required : 
      @param userID
      @param packID
      @param packType
      @param cartonRequest
      @param WorkStationID
   */  
export interface BuildGenUnfreightManifest_input{
      /**  userID  */  
   userID:string,
      /**  packID  */  
   packID:number,
      /**  packType  */  
   packType:string,
      /**  cartonRequest  */  
   cartonRequest:any,      //schema had no properties on an object.
      /**  WorkStationID  */  
   WorkStationID:string,
}

export interface BuildGenUnfreightManifest_output{
   returnObj:boolean,
}

   /** Required : 
      @param packID
   */  
export interface BuildMasterPackFreightRequest_input{
      /**  Pack Number  */  
   packID:number,
}

export interface BuildMasterPackFreightRequest_output{
   returnObj:Erp_Tablesets_FreightInfoRequestTableset[],
}

   /** Required : 
      @param packID
   */  
export interface BuildMiscFreightRequest_input{
      /**  Pack Number  */  
   packID:number,
}

export interface BuildMiscFreightRequest_output{
   returnObj:Erp_Tablesets_FreightInfoRequestTableset[],
}

   /** Required : 
      @param packID
   */  
export interface BuildSubFreightRequest_input{
      /**  Pack Number  */  
   packID:number,
}

export interface BuildSubFreightRequest_output{
   returnObj:Erp_Tablesets_FreightInfoRequestTableset[],
}

   /** Required : 
      @param packID
   */  
export interface BuildTransFreightRequest_input{
      /**  Pack Number  */  
   packID:number,
}

export interface BuildTransFreightRequest_output{
   returnObj:Erp_Tablesets_FreightInfoRequestTableset[],
}

export interface Erp_Tablesets_COORow{
   Company:string,
   MasterpackPackID:number,
   PackID:number,
   OrderNum:string,
   OrderLineNum:number,
   OrderRelNum:number,
   OrigCountry:number,
   CountryDescription:string,
   PartNum:string,
   QtyPerc:number,
   ValuePerc:number,
   Primary:boolean,
   RelatedToFile:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FreightCartonResponseRow{
   CallTagNumber:string,
   DimWeight:number,
   DimWeightUOM:string,
   DiscountFreightAmount:number,
   DiscountFreightAmountUOM:string,
   ErrorFlag:boolean,
   ErrorMessage:string,
   EstimatedFreightAmount:number,
   EstimatedFreightAmountUOM:string,
   EstimatedFreightFlag:boolean,
   FreightZone:string,
   OtherAmount:number,
   OtherAmountUOM:string,
   OversizeFlag:boolean,
   PickupNumber:string,
   PublishedFreightAmount:number,
   PublishedFreightAmountUOM:string,
   ShipDate:string,
   TemplateCode:string,
   TransactionNumber:string,
   WayBillNbr:string,
   FreightedShipVia:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FreightCartonResponseTrackingRow{
   TrackingNumber:string,
   PackID:number,
      /**  Discounted freight amount calculated by the shipper  */  
   DiscountFreightAmt:number,
      /**  Published freight amount determined by the shipper.  */  
   PublishedFreightAmt:number,
      /**  Concatenation of the pack num and sequential case number.  */  
   CaseNum:string,
      /**  Shipment type  */  
   ShipmentType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FreightInfoRequestTableset{
   MasterPackInfo:Erp_Tablesets_MasterPackInfoRow[],
   PackInfo:Erp_Tablesets_PackInfoRow[],
   OrderInfo:Erp_Tablesets_OrderInfoRow[],
   OrderLine:Erp_Tablesets_OrderLineRow[],
   COO:Erp_Tablesets_COORow[],
   KitComponent:Erp_Tablesets_KitComponentRow[],
   PhantomPack:Erp_Tablesets_PhantomPackRow[],
   UPSQV:Erp_Tablesets_UPSQVRow[],
   MasterUPSQV:Erp_Tablesets_MasterUPSQVRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FreightInfoResponseTableset{
   FreightCartonResponse:Erp_Tablesets_FreightCartonResponseRow[],
   FreightCartonResponseTracking:Erp_Tablesets_FreightCartonResponseTrackingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_KitComponentRow{
   Company:string,
   MasterpackPackID:number,
   PackID:number,
   OrderNum:string,
   OrderLine:number,
   KitPartNum:string,
   AESExp:string,
   ECNNumber:string,
   ExpLicNumber:string,
   ExpLicType:string,
   HazClass:string,
   HazGvrnmtID:string,
   HazItem:boolean,
   HazPackInstr:string,
   HazSub:string,
   HazTechName:string,
   HTS:string,
   NAFTAOrigCountry:string,
   NAFTAPref:string,
   NAFTAProd:string,
   OrigCountry:string,
   SchedBcode:string,
   UseHTSDesc:boolean,
   PartDescription:string,
   QtyShip:number,
   QtyShipUOM:string,
   BaseCurrSymbol:string,
   CurrSymbol:string,
   UnitPrice:number,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   Date20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   KitParentLine:number,
   OrderRelNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MasterPackInfoRow{
   AddFreightToAmountFlag:boolean,
   AODFlag:boolean,
   AutoPODFlag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   ContentValue:number,
   DeclaredValue:number,
   DeclaredValueCurrencyUOM:string,
   DeclaredValueFlag:boolean,
   DocumentsOnlyFlag:boolean,
   EmailNotificationAddresses:string,
   EmailNotificationFlag:boolean,
   FFCity:string,
   FFCompName:string,
   FFContact:string,
   FFCountry:string,
   FFID:string,
   FFPhoneNum:string,
   FFAddress1:string,
   FFAddress2:string,
   FFState:string,
   FFZip:string,
   FreightCarrier:string,
   FreightType:string,
   GroundCollectionTypeCode:string,
   HandlingCharge:number,
   HandlingChargeCurrencyUOM:string,
   HandlingChargeFlag:boolean,
   HazardousShipment:boolean,
   Height:number,
   HeightUOM:string,
   HomeDeliveryDate:string,
   HomeDeliveryFlag:boolean,
   HomeDeliveryInstr:string,
   HomeDeliveryPhone:string,
   IntrntlShip:boolean,
   Length:number,
   LengthUOM:string,
   LetterOfInstr:boolean,
   MoneyOrderAmount:number,
   MoneyOrderAmountCurrUOM:string,
   MoneyOrderRequiredFlag:boolean,
   PackID:number,
   PayAccount:string,
   PayBTCity:string,
   PayBTCountry:string,
   PayBTAddress1:string,
   PayBTAddress2:string,
   PayBTState:string,
   PayFlag:string,
   PriorityAlertFlag:boolean,
   Reference1:string,
   Reference2:string,
   Reference3:string,
   Reference4:string,
   Reference5:string,
   ReferenceNotes:string,
   ReleaseAuthNumber:string,
   ReleaseOnFileFlag:boolean,
   ResidentialDeliveryFlag:boolean,
   SaturdayDeliveryFlag:boolean,
   SaturdayPickupFlag:boolean,
   SequenceNum:number,
   ServiceSaturdayDeliveryFlag:boolean,
   ServiceSaturdayPickupFlag:boolean,
   ShipDate:string,
   ShipExportDeclartn:boolean,
   ShipToAddress:string,
   ShipToAddress2:string,
   ShipToAttention:string,
   ShipToCity:string,
   ShipToCountry:string,
   ShipToFax:string,
   ShipToID:string,
   ShipToName:string,
   ShipToPhone:string,
   ShipToPostalCode:string,
   ShipToRegion:string,
   ShipToTerritory:string,
   SignatureRequiredFlag:boolean,
   SoldToAddress:string,
   SoldToAddress2:string,
   SoldToAttention:string,
   SoldToCity:string,
   SoldToCountry:string,
   SoldToFax:string,
   SoldToID:string,
   SoldToName:string,
   SoldToPhone:string,
   SoldToPostalCode:string,
   SoldToRegion:string,
   SoldToTerritory:string,
   StationID:string,
   TemplateCode:string,
   VerbalConfirmationFlag:boolean,
   Weight:number,
   WeightUOM:string,
   Width:number,
   WidthUOM:string,
   PackIDList:string,
   UserEntryID:string,
      /**  Pay Zip Code  */  
   PayBTZip:string,
      /**  Company  */  
   Company:string,
      /**  Misc, Customer, SubContract or Transfer  */  
   ShipmentType:string,
   ShipToAddress3:string,
      /**  Sold To Address 3  */  
   SoldToAddress3:string,
   IndividualPackIds:boolean,
   ServSignature:boolean,
      /**  Determines the level of delivery confirmation.   1 - No Signature Required 2 - Adult Signature Required 3 - Confirmation Required 4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
   FFAddress3:string,
   NonStdPkg:boolean,
   PayBTAddress3:string,
   PayBTPhone:string,
   AddlHdlgFlag:boolean,
      /**  Package code  */  
   PkgCode:string,
      /**  Identifies the type of manifest the third party shipping applications are to process.  SPack is a standard pack, MPack is a master pack, PPack is a Phantom Pack and MPIND is an individual master pack.  */  
   ManifestType:string,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   SoldToUseBlindShipping:boolean,
   CustomerNotes:string,
   ShipperNotes:string,
   PkgSizeUOM:string,
   LabelComment:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MasterUPSQVRow{
   UPSQuantumView:boolean,
   UPSQVShipFromName:string,
   UPSQVMemo:string,
   UPSQVEmailAddrs:string,
   UPSQVShipNotList:boolean,
   UPSQVExceptNotList:boolean,
   UPSQVDelNotList:boolean,
   Company:string,
   PackID:number,
   UPSQVSeq:number,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Character11:string,
   Character12:string,
   Character13:string,
   Character14:string,
   Character15:string,
   Character16:string,
   Character17:string,
   Character18:string,
   Character19:string,
   Character20:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderInfoRow{
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   CustPONumber:string,
   DropShip:boolean,
   FFCity:string,
   FFCompName:string,
   FFContact:string,
   FFCountry:string,
   FFID:string,
   FFPhoneNum:string,
   FFAddress1:string,
   FFAddress2:string,
   FFState:string,
   FFZip:string,
   IntrntlShip:boolean,
   JobNumber:string,
   LetterOfInstr:boolean,
   OrderNum:string,
   PayAccount:string,
   PayBTCity:string,
   PayBTCountry:string,
   PayBTAddress1:string,
   PayBTAddress2:string,
   PayBTState:string,
   PayBTZip:string,
   PayFlag:string,
   ShipExprtDeclartn:boolean,
   TotalOrderValue:number,
   TotalOrderValueCurrencyUOM:string,
   OrderType:string,
   PartList:string,
      /**  Customer  */  
   CustID:string,
      /**  Pay Bill To Name  */  
   PayBTName:string,
      /**  Billing address3  */  
   PayBTAddress3:string,
      /**  Freight Forward Address 3  */  
   FFAddress3:string,
      /**  Billing phone number  */  
   PayBTPhone:string,
   Company:string,
   MasterpackPackID:number,
   PackID:number,
   PackslipComments:string,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   CheckBox19:boolean,
   DeliveryInstr:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderLineRow{
   Company:string,
   MasterpackPackID:number,
   PackID:number,
   OrderNum:string,
   OrderRelNum:number,
   UnitPrice:number,
   QTYShipUOM:string,
   Kit:boolean,
   KitPrintCompPack:boolean,
   KitPrintCompCust:boolean,
   AESExp:string,
   ECNNumber:string,
   ExpLicType:string,
   ExpLicNumber:string,
   HazClass:string,
   HazGvrnmtID:string,
   HazItem:boolean,
   HazPackInstr:string,
   HazSub:string,
   HazTechName:string,
   HTS:string,
   NAFTAOrigCountry:string,
   NAFTAPref:string,
   NAFTAProd:string,
   OrigCountry:string,
   SchedBcode:string,
   UseHTSDesc:boolean,
   PartNum:string,
   PartDescription:string,
   QtyShip:number,
   OrderLineNum:number,
   BaseCurrSymbol:string,
   CurrSymbol:string,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   PartCharacter01:string,
   PartCharacter02:string,
   PartCharacter03:string,
   PartCharacter04:string,
   PartCharacter05:string,
   PartCharacter06:string,
   PartCharacter07:string,
   PartCharacter08:string,
   PartCharacter09:string,
   PartCharacter10:string,
   PartCheckBox01:boolean,
   PartCheckBox02:boolean,
   PartCheckBox03:boolean,
   PartCheckBox04:boolean,
   PartCheckBox05:boolean,
   PartCheckBox06:boolean,
   PartCheckBox07:boolean,
   PartCheckBox08:boolean,
   PartCheckBox09:boolean,
   PartCheckBox10:boolean,
   PartCheckBox11:boolean,
   PartCheckBox12:boolean,
   PartCheckBox13:boolean,
   PartCheckBox14:boolean,
   PartCheckBox15:boolean,
   PartCheckBox16:boolean,
   PartCheckBox17:boolean,
   PartCheckBox18:boolean,
   PartCheckBox19:boolean,
   PartCheckBox20:boolean,
   PartDate01:string,
   PartDate02:string,
   PartDate03:string,
   PartDate04:string,
   PartDate05:string,
   PartDate06:string,
   PartDate07:string,
   PartDate08:string,
   PartDate09:string,
   PartDate10:string,
   PartDate11:string,
   PartDate12:string,
   PartDate13:string,
   PartDate14:string,
   PartDate15:string,
   PartDate16:string,
   PartDate17:string,
   PartDate18:string,
   PartDate19:string,
   PartDate20:string,
   PartNumber01:number,
   PartNumber02:number,
   PartNumber03:number,
   PartNumber04:number,
   PartNumber05:number,
   PartNumber06:number,
   PartNumber07:number,
   PartNumber08:number,
   PartNumber09:number,
   PartNumber10:number,
   PartNumber11:number,
   PartNumber12:number,
   PartNumber13:number,
   PartNumber14:number,
   PartNumber15:number,
   PartNumber16:number,
   PartNumber17:number,
   PartNumber18:number,
   PartNumber19:number,
   PartNumber20:number,
   PartShortChar01:string,
   PartShortChar02:string,
   PartShortChar03:string,
   PartShortChar04:string,
   PartShortChar05:string,
   PartShortChar06:string,
   PartShortChar07:string,
   PartShortChar08:string,
   PartShortChar09:string,
   PartShortChar10:string,
      /**  Bill of Landing Class. Additional data for the part required for LTL and International shipments.  */  
   BOLClass:string,
      /**  Fair Market Value. Additional data for the part required for LTL and International shipments.  */  
   FairMarketValue:number,
      /**  The Part's Unit Net Weight.  */  
   NetWeight:number,
      /**   Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  */  
   NetWeightUOM:string,
      /**  The Part's Unit Gross Weight.  */  
   GrossWeight:number,
      /**   The Part's Unit Gross Weight. 
Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight". Use UOMClass.DefUOMCode of the "weight" UOMClass as a default when creating new part records.  */  
   GrossWeightUOM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PackInfoRow{
   AddFreightToAmountFlag:boolean,
   AODFlag:boolean,
   AutoPODflag:boolean,
   CertOfOrigin:boolean,
   CommercialInvoice:boolean,
   ContentValue:number,
   ContentValueCurrencyUOM:string,
   ConZip:string,
   DeclaredValue:number,
   DeclaredValueCurrencyUOM:string,
   DeclaredValueFlag:boolean,
   DocumentsOnlyFlag:boolean,
   EmailNotificationAddresses:string,
   EmailNotificationFlag:boolean,
   FFCity:string,
   FFCompName:string,
   FFContact:string,
   FFCountry:string,
   FFID:string,
   FFPhoneNum:string,
   FFAddress1:string,
      /**  `  */  
   FFAddress2:string,
   FFState:string,
   FFZip:string,
   FreightCarrier:string,
   FreightType:string,
   GroundCollectionTypeCode:string,
   HandlingCharge:number,
   HandlingChargeCurrencyUOM:string,
   HandlingChargeFlag:boolean,
   HazardousShipment:boolean,
   HeightUOM:string,
   HomeDeliveryDate:string,
   HomeDeliveryFlag:boolean,
   HomeDeliveryInstr:string,
   HomeDeliveryPhone:string,
   IntrntlShip:boolean,
   Length:number,
   LengthUOM:string,
   LetterOfInstr:boolean,
   MoneyOrderAmount:number,
   MoneyOrderAmountCurrUOM:string,
   MoneyOrderRequiredFlag:boolean,
   PackID:number,
   PayAccount:string,
   PayBTCity:string,
   PayBTCountry:string,
   PayBTAddress1:string,
   PayBTAddress2:string,
   PayBTState:string,
   PayFlag:string,
   PriorityAlertFlag:boolean,
   Reference1:string,
   Reference2:string,
   Reference3:string,
   Reference4:string,
   Reference5:string,
   ReferenceNotes:string,
   ReleaseAuthNumber:string,
   ReleaseOnFileFlag:boolean,
   ResidentialDeliveryFlag:boolean,
   SaturdayDeliveryFlag:boolean,
   SaturdayPickupFlag:boolean,
   SequenceNum:number,
   ServiceSaturdayDeliveryFlag:boolean,
   ServiceSaturdayPickupFlag:boolean,
   ShipDate:string,
   ShipExprtDeclartn:boolean,
   ShipToAddress:string,
   ShipToAddress2:string,
   ShipToAttention:string,
   ShipToCity:string,
   ShipToCountry:string,
   ShipToFax:string,
   ShipToID:string,
   ShipToName:string,
   ShipToPhone:string,
   ShipToPostalCode:string,
   ShipToRegion:string,
   ShipToTerritory:string,
   SignatureRequiredFlag:boolean,
   SoldToAddress:string,
   SoldToAddress2:string,
   SoldToAttention:string,
   SoldToCity:string,
   SoldToCountry:string,
   SoldToFax:string,
   SoldToID:string,
   SoldToName:string,
   SoldToPhone:string,
   SoldToPostalCode:string,
   SoldToRegion:string,
   SoldToTerritory:string,
   StationID:string,
   TemplateCode:string,
   VerbalConfirmationFlag:boolean,
   Weight:number,
   WeightUOM:string,
   Width:number,
   WidthUOM:string,
   OrderList:string,
   UserEntryID:string,
   PayBTZip:string,
      /**  Height  */  
   Height:number,
      /**  Company  */  
   Company:string,
      /**  Transfer, Customer, Subcontract or Misc  */  
   ShipmentType:string,
      /**  Sold To Address 3  */  
   SoldToAddress3:string,
      /**  Ship To Address 3  */  
   ShipToAddress3:string,
   DeliveryConf:number,
      /**  Additional Handling flag.  */  
   AddlHdlgFlag:boolean,
      /**  Freight Forward Address line 3  */  
   FFAddress3:string,
      /**  Billing phone number  */  
   PayBTPhone:string,
      /**  Bililng address line 3  */  
   PayBTAddress3:string,
      /**  logical indicating if the packaing is standard  */  
   NonStdPkg:boolean,
      /**  packaging  */  
   PkgCode:string,
      /**  Vantage generated case number sent to third party shipping packages.  Concatenation of the PackNum and a sequential counter.  */  
   CaseNum:string,
   MasterpackPackID:number,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   SoldToUseBlindShipping:boolean,
   IncotermCode:string,
   IncotermLocation:string,
   CustomerNotes:string,
   PkgSizeUOM:string,
   LabelComment:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PhantomPackRow{
   Company:string,
   MasterpackPackID:number,
   PackID:number,
   CaseNumber:string,
   Weight:number,
   WeightUOM:string,
   Length:number,
   LengthUOM:string,
   Width:number,
   WidthUOM:string,
   Height:number,
   HeightUOM:string,
   CODAmount:number,
   DeclaredValue:boolean,
   DeclaredAmount:number,
   CheckMOReq:boolean,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UPSQVRow{
   UPSQuantumView:boolean,
   UPSQVShipFromName:string,
   UPSQVMemo:string,
   UPSQVEmailAddrs:string,
   UPSQVShipNotList:boolean,
   UPSQVExceptNotList:boolean,
   UPSQVDelNotList:boolean,
   Company:string,
   MasterpackPackID:number,
   PackID:number,
   UPSQVSeq:number,
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Character11:string,
   Character12:string,
   Character13:string,
   Character14:string,
   Character15:string,
   Character16:string,
   Character17:string,
   Character18:string,
   Character19:string,
   Character20:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Date06:string,
   Date07:string,
   Date08:string,
   Date09:string,
   Date10:string,
   Date11:string,
   Date12:string,
   Date13:string,
   Date14:string,
   Date15:string,
   Date16:string,
   Date17:string,
   Date18:string,
   Date19:string,
   Date20:string,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UnfreightCartonResponseRow{
   PackID:number,
   ErrorFlag:boolean,
   ErrorMessage:string,
   UnfreightDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UnfreightInfoResponseTableset{
   UnfreightCartonResponse:Erp_Tablesets_UnfreightCartonResponseRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param freightURL
      @param rdt
      @param WorkStationID
      @param httpTimeOut
   */  
export interface FreightCarton_input{
   freightURL:string,
   rdt:any,      //schema had no properties on an object.
   WorkStationID:string,
   httpTimeOut:number,
}

export interface FreightCarton_output{
   returnObj:any,      //schema had no properties on an object.
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
      @param tds
      @param rds
      @param packNum
      @param shipmentType
   */  
export interface LogManifestMsg_input{
   tds:Erp_Tablesets_FreightInfoRequestTableset[],
   rds:Erp_Tablesets_FreightInfoResponseTableset[],
      /**  packNum  */  
   packNum:number,
      /**  shipmentType  */  
   shipmentType:string,
}

export interface LogManifestMsg_output{
}

   /** Required : 
      @param freightURL
      @param urds
      @param WorkStationID
      @param httpTimeOut
   */  
export interface UnfreightCarton_input{
   freightURL:string,
   urds:any,      //schema had no properties on an object.
   WorkStationID:string,
   httpTimeOut:number,
}

export interface UnfreightCarton_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param ipPackID
      @param ipShipmentType
      @param ds
   */  
export interface UpdateFreightedShipment_input{
      /**  package code  */  
   ipPackID:number,
      /**  shipment type  */  
   ipShipmentType:string,
   ds:Erp_Tablesets_FreightInfoResponseTableset[],
}

export interface UpdateFreightedShipment_output{
}

export interface UpdateTimeOut_output{
parameters : {
      /**  output parameters  */  
   httpTimeOut:number,
}
}

   /** Required : 
      @param ipPackID
      @param ipShipmentType
      @param ds
   */  
export interface UpdateUnFreightedShipment_input{
      /**  package code  */  
   ipPackID:number,
      /**  shipment type  */  
   ipShipmentType:string,
   ds:Erp_Tablesets_UnfreightInfoResponseTableset[],
}

export interface UpdateUnFreightedShipment_output{
}

