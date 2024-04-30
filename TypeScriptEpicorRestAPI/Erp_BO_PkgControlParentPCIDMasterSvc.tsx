import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PkgControlParentPCIDMasterSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", {
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
   Summary: Invoke method Init
   OperationID: Init
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Init_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Init(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Init_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/Init", {
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
         resolve(data as Init_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPCIDMaster
   Description: This returns a blank master record to the UI
   OperationID: GetNewPCIDMaster
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCIDMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCIDMaster(requestBody:GetNewPCIDMaster_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCIDMaster_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/GetNewPCIDMaster", {
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
         resolve(data as GetNewPCIDMaster_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPCIDPrinted
   Description: to check if pcid has been printed and throw a error.
   OperationID: CheckPCIDPrinted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPCIDPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPCIDPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPCIDPrinted(requestBody:CheckPCIDPrinted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPCIDPrinted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/CheckPCIDPrinted", {
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
         resolve(data as CheckPCIDPrinted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportStyleNum
   OperationID: GetReportStyleNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReportStyleNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyleNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportStyleNum(requestBody:GetReportStyleNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportStyleNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/GetReportStyleNum", {
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
         resolve(data as GetReportStyleNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessParentPCID
   Description: This method updates the parent pcid record when the ui is closed.
   OperationID: ProcessParentPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessParentPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessParentPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessParentPCID(requestBody:ProcessParentPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessParentPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/ProcessParentPCID", {
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
         resolve(data as ProcessParentPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessChildPCID
   Description: this method creates the parent/child links if a child is scanned in the UI.
   OperationID: ProcessChildPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessChildPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessChildPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessChildPCID(requestBody:ProcessChildPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessChildPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/ProcessChildPCID", {
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
         resolve(data as ProcessChildPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessPCIDPrinted
   Description: This method updates the parent pcid record after a mixed label has been printed
   OperationID: ProcessPCIDPrinted
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessPCIDPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPCIDPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessPCIDPrinted(requestBody:ProcessPCIDPrinted_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessPCIDPrinted_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/ProcessPCIDPrinted", {
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
         resolve(data as ProcessPCIDPrinted_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreProcess
   Description: this method checks the parent/child records for errors before processing.
   OperationID: PreProcess
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreProcess(requestBody:PreProcess_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreProcess_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/PreProcess", {
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
         resolve(data as PreProcess_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateEDIMasterMixed
   Description: To validate the EDI Data before print and during confirm
   OperationID: ValidateEDIMasterMixed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateEDIMasterMixed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEDIMasterMixed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateEDIMasterMixed(requestBody:ValidateEDIMasterMixed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateEDIMasterMixed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/ValidateEDIMasterMixed", {
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
         resolve(data as ValidateEDIMasterMixed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreProcessConfirm
   OperationID: PreProcessConfirm
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreProcessConfirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessConfirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreProcessConfirm(requestBody:PreProcessConfirm_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreProcessConfirm_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/PreProcessConfirm", {
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
         resolve(data as PreProcessConfirm_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConfirmParent
   Description: This method should be called when a child pcid has already been entered and
if the parent needs to be confirmed
   OperationID: ConfirmParent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConfirmParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfirmParent(requestBody:ConfirmParent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConfirmParent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/ConfirmParent", {
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
         resolve(data as ConfirmParent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConfirmChild
   Description: This method should be called if the parent PCID is already entered
and the user wants to confirm the child.
   OperationID: ConfirmChild
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConfirmChild_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmChild_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfirmChild(requestBody:ConfirmChild_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConfirmChild_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/ConfirmChild", {
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
         resolve(data as ConfirmChild_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MasterPCIDNeedsToBeLoaded
   Description: Method to throw a error message
   OperationID: MasterPCIDNeedsToBeLoaded
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterPCIDNeedsToBeLoaded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterPCIDNeedsToBeLoaded(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MasterPCIDNeedsToBeLoaded_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/MasterPCIDNeedsToBeLoaded", {
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
         resolve(data as MasterPCIDNeedsToBeLoaded_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ContactSupervisor
   OperationID: ContactSupervisor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContactSupervisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ContactSupervisor(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ContactSupervisor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/ContactSupervisor", {
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
         resolve(data as ContactSupervisor_output)
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
      @param ipPCID
   */  
export interface CheckPCIDPrinted_input{
   ipPCID:string,
}

export interface CheckPCIDPrinted_output{
}

   /** Required : 
      @param ds
      @param ipPCID
   */  
export interface ConfirmChild_input{
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
      /**  child pcid that needs to be confirmed  */  
   ipPCID:string,
}

export interface ConfirmChild_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset,
}
}

   /** Required : 
      @param ds
      @param ipPCID
   */  
export interface ConfirmParent_input{
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
   ipPCID:string,
}

export interface ConfirmParent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset,
}
}

export interface ContactSupervisor_output{
}

export interface Erp_Tablesets_PkgControlParentPCIDMasterRow{
   PCID:string,
   Status:string,
   Label:string,
   Part:string,
   Quantity:number,
   UOM:string,
   NumberOfPCIDs:number,
   PrevPCID:string,
   ChildPCID:string,
   PkgMasterMixedPrint:boolean,
   ControlIDCode:string,
   MasterMixedMaster:string,
   Seq:number,
   MessageUI:string,
   RemoveChild:boolean,
   EnablePrint:boolean,
   ConfirmPCID:string,
      /**  Enable parent PCID field.  */  
   EnableParent:boolean,
   EnableChild:boolean,
   EnableConfirmPCID:boolean,
   ParentPCID:string,
      /**  Last Time and Date when the PCID was updated  */  
   UpdatedDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlParentPCIDMasterTableset{
   PkgControlParentPCIDMaster:Erp_Tablesets_PkgControlParentPCIDMasterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipType
   */  
export interface GetNewPCIDMaster_input{
   ipType:string,
}

export interface GetNewPCIDMaster_output{
   returnObj:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
}

   /** Required : 
      @param MasterMixed
      @param ipPCID
   */  
export interface GetReportStyleNum_input{
      /**  master or mixedmaster  */  
   MasterMixed:string,
      /**  input pcid  */  
   ipPCID:string,
}

export interface GetReportStyleNum_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   NumLabelsToPrint:number,
   promptForReportStyle:boolean,
   printerID:string,
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

export interface Init_output{
}

export interface MasterPCIDNeedsToBeLoaded_output{
}

   /** Required : 
      @param ds
      @param ipPCID
   */  
export interface PreProcessConfirm_input{
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
   ipPCID:string,
}

export interface PreProcessConfirm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset,
}
}

   /** Required : 
      @param ds
      @param ipChildPCID
   */  
export interface PreProcess_input{
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
   ipChildPCID:string,
}

export interface PreProcess_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset,
   opMessageUI:string,
   opSupervisorPwdRequired:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessChildPCID_input{
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
}

export interface ProcessChildPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessPCIDPrinted_input{
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
}

export interface ProcessPCIDPrinted_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessParentPCID_input{
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset[],
}

export interface ProcessParentPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlParentPCIDMasterTableset,
}
}

   /** Required : 
      @param ipParentPCID
   */  
export interface ValidateEDIMasterMixed_input{
   ipParentPCID:string,
}

export interface ValidateEDIMasterMixed_output{
   returnObj:boolean,
}

