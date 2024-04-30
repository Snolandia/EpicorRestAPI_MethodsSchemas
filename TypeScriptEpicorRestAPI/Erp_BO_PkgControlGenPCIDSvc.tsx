import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PkgControlGenPCIDSvc
// Description: Class that handles the logic for the PCID generation. It is used in Adhoc Job Output, Partial, Ad Hoc and Overlay PCID screens.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/Init", {
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
   Summary: Invoke method GetTempRow
   Description: Purpose: Creates a PkgControlGenPCID record. Get info from the input data.
Parameters:
<param name="ipJobNum">JobNum</param><param name="ipCustID">CustID</param><param name="ipXPartNum">Cross part num</param><param name="ipPartNum">PartNum from part master part, if available</param><param name="ipKeyFieldName">The keyfield can be JobNum, CustID or XPartNum</param><param name="ipWhoCalled">Name of the form that called this method</param><param name="isMES">is this called from MES</param><param name="empIDorUserID">EmpID or UserID</param><param name="ipRawPCID">Raw PCID value</param><param name="custXPrtRowID">User selected CustXPrt.SysRowID </param><returns>Erp.BO.PkgControlGenPCIDTableset</returns>
Notes:
   OperationID: GetTempRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTempRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTempRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTempRow(requestBody:GetTempRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTempRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/GetTempRow", {
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
         resolve(data as GetTempRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPackageCode
   Description: Purpose: Get next package code according to the sequence set in Part Maintenance
Parameters:
<param name="ipCompany">Current Company</param><param name="ipPartNum">Part Number</param><param name="refPkgCode">Package code, can be send as empty to get the first package code in the sequence</param><param name="outPkgCodeDesc">Package code description</param><param name="custNum">Customer Number</param><param name="shipToNum">ShipTo Number</param>
Notes:
   OperationID: GetPackageCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPackageCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackageCode(requestBody:GetPackageCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPackageCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/GetPackageCode", {
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
         resolve(data as GetPackageCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SuppressPrintMessages
   Description: Returns if the employee has the 'Suppress Print Messages' flag on
   OperationID: SuppressPrintMessages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SuppressPrintMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuppressPrintMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SuppressPrintMessages(requestBody:SuppressPrintMessages_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SuppressPrintMessages_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/SuppressPrintMessages", {
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
         resolve(data as SuppressPrintMessages_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PerformMaterialMovement
   Description: PerformMaterialMovement
   OperationID: PerformMaterialMovement
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PerformMaterialMovement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMaterialMovement_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerformMaterialMovement(requestBody:PerformMaterialMovement_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PerformMaterialMovement_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/PerformMaterialMovement", {
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
         resolve(data as PerformMaterialMovement_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GeneratePCIDList
   Description: This method will generate the PCID
   OperationID: GeneratePCIDList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GeneratePCIDList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePCIDList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GeneratePCIDList(requestBody:GeneratePCIDList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GeneratePCIDList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/GeneratePCIDList", {
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
         resolve(data as GeneratePCIDList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GeneratePCID
   Description: This method will generate the PCID
   OperationID: GeneratePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GeneratePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GeneratePCID(requestBody:GeneratePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GeneratePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/GeneratePCID", {
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
         resolve(data as GeneratePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeInventoryTest
   Description: check negative inventory
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/NegativeInventoryTest", {
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
   Summary: Invoke method CheckPackageCodeAllocNegQty
   OperationID: CheckPackageCodeAllocNegQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackageCodeAllocNegQty(requestBody:CheckPackageCodeAllocNegQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPackageCodeAllocNegQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/CheckPackageCodeAllocNegQty", {
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
         resolve(data as CheckPackageCodeAllocNegQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsAutoPrintSetup
   Description: To verify if autoprint is setup
   OperationID: IsAutoPrintSetup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsAutoPrintSetup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutoPrintSetup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsAutoPrintSetup(requestBody:IsAutoPrintSetup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsAutoPrintSetup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/IsAutoPrintSetup", {
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
         resolve(data as IsAutoPrintSetup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSourcePCID
   OperationID: ValidateSourcePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSourcePCID(requestBody:ValidateSourcePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSourcePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateSourcePCID", {
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
         resolve(data as ValidateSourcePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSourcePCID
   Description: Logic to extract the source PCID
   OperationID: ChangeSourcePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSourcePCID(requestBody:ChangeSourcePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSourcePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ChangeSourcePCID", {
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
         resolve(data as ChangeSourcePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWarehouseList
   OperationID: GetWarehouseList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetWarehouseList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehouseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWarehouseList(requestBody:GetWarehouseList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWarehouseList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/GetWarehouseList", {
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
         resolve(data as GetWarehouseList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetPCIDLabelTypeInfo
   Description: Set PCID Label Type Info
   OperationID: SetPCIDLabelTypeInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetPCIDLabelTypeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetPCIDLabelTypeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetPCIDLabelTypeInfo(requestBody:SetPCIDLabelTypeInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetPCIDLabelTypeInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/SetPCIDLabelTypeInfo", {
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
         resolve(data as SetPCIDLabelTypeInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReturnValidItems
   Description: To get a list of history items to remove
   OperationID: ReturnValidItems
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReturnValidItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnValidItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReturnValidItems(requestBody:ReturnValidItems_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReturnValidItems_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ReturnValidItems", {
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
         resolve(data as ReturnValidItems_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CustomerChanged
   Description: Updates info when customer changes.
   OperationID: CustomerChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomerChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomerChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomerChanged(requestBody:CustomerChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomerChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/CustomerChanged", {
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
         resolve(data as CustomerChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PkgControlGenPCIDXPartChanged
   Description: Called when XPartNum changes.  This method will additionally update customer information if a customer is not already selected when called from
Overlay Import
   OperationID: PkgControlGenPCIDXPartChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PkgControlGenPCIDXPartChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PkgControlGenPCIDXPartChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgControlGenPCIDXPartChanged(requestBody:PkgControlGenPCIDXPartChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PkgControlGenPCIDXPartChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/PkgControlGenPCIDXPartChanged", {
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
         resolve(data as PkgControlGenPCIDXPartChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method XPartChanged
   Description: Updates info when customer part changes.
   OperationID: XPartChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/XPartChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/XPartChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_XPartChanged(requestBody:XPartChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<XPartChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/XPartChanged", {
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
         resolve(data as XPartChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ShipToChanged
   Description: Updates info when shipTo changes
   OperationID: ShipToChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ShipToChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShipToChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ShipToChanged(requestBody:ShipToChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ShipToChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ShipToChanged", {
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
         resolve(data as ShipToChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PkgCodeChanged
   Description: Updates info when pkgCode changes
   OperationID: PkgCodeChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PkgCodeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PkgCodeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PkgCodeChanged(requestBody:PkgCodeChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PkgCodeChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/PkgCodeChanged", {
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
         resolve(data as PkgCodeChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BinNumChanged
   Description: Updates info when BinNum changes
   OperationID: BinNumChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BinNumChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BinNumChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BinNumChanged(requestBody:BinNumChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BinNumChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/BinNumChanged", {
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
         resolve(data as BinNumChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method WarehouseCodeChanged
   Description: Updates info when Warehouse changes
   OperationID: WarehouseCodeChanged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/WarehouseCodeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarehouseCodeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarehouseCodeChanged(requestBody:WarehouseCodeChanged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<WarehouseCodeChanged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/WarehouseCodeChanged", {
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
         resolve(data as WarehouseCodeChanged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWhsePCID
   Description: Validates warehouse for PCID
   OperationID: ValidateWhsePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWhsePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhsePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWhsePCID(requestBody:ValidateWhsePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWhsePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateWhsePCID", {
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
         resolve(data as ValidateWhsePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWhseBinPCID
   Description: Validates BinNum for PCID
   OperationID: ValidateWhseBinPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWhseBinPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhseBinPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWhseBinPCID(requestBody:ValidateWhseBinPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWhseBinPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateWhseBinPCID", {
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
         resolve(data as ValidateWhseBinPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateNumberToGen
   Description: Validates number of PCIDs to generate
   OperationID: ValidateNumberToGen
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateNumberToGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNumberToGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateNumberToGen(requestBody:ValidateNumberToGen_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateNumberToGen_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateNumberToGen", {
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
         resolve(data as ValidateNumberToGen_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateShift
   Description: Validates shift
   OperationID: ValidateShift
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShift(requestBody:ValidateShift_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateShift_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateShift", {
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
         resolve(data as ValidateShift_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateXPart
   Description: Validates customer part
   OperationID: ValidateXPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateXPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateXPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateXPart(requestBody:ValidateXPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateXPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateXPart", {
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
         resolve(data as ValidateXPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePkgCode
   Description: Validates package code
   OperationID: ValidatePkgCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePkgCode(requestBody:ValidatePkgCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePkgCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidatePkgCode", {
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
         resolve(data as ValidatePkgCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCustomer
   Description: Validates customer
   OperationID: ValidateCustomer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCustomer(requestBody:ValidateCustomer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCustomer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateCustomer", {
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
         resolve(data as ValidateCustomer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateShipTo
   Description: Validates ShipTo
   OperationID: ValidateShipTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShipTo(requestBody:ValidateShipTo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateShipTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateShipTo", {
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
         resolve(data as ValidateShipTo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateJob
   Description: Validates job number
   OperationID: ValidateJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateJob(requestBody:ValidateJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/ValidateJob", {
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
         resolve(data as ValidateJob_output)
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
   */  
export interface BinNumChanged_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface BinNumChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param ds
      @param ipSourcePCID
   */  
export interface ChangeSourcePCID_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
   ipSourcePCID:string,
}

export interface ChangeSourcePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param ipCalledFrom
      @param ipPackageCode
      @param ipQty
   */  
export interface CheckPackageCodeAllocNegQty_input{
   ipCalledFrom:string,
   ipPackageCode:string,
   ipQty:number,
}

export interface CheckPackageCodeAllocNegQty_output{
parameters : {
      /**  output parameters  */  
   opWarning:string,
   opAction:string,
   opAllocWarning:string,
   opAllocAction:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CustomerChanged_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface CustomerChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

export interface Erp_Tablesets_PkgControlGenPCIDRow{
   Company:string,
   CurrentPkgCode:string,
   CustID:string,
   CustNum:number,
   JobNum:string,
   JobDate:string,
   Name:string,
   NumberToGen:number,
   OprSeq:number,
   OurSupplierCode:string,
   PartNum:string,
   Plant:string,
   PONum:string,
   PrinterID:string,
   PrinterList:string,
   QtyPer:number,
   RevisionNum:string,
   Shift:number,
   ShipToContainerPartID:string,
   ShipToName:string,
   ShipToNum:string,
   XPartNum:string,
   XRevisionNum:string,
   UOMCode:string,
   LabelType:string,
   PkgControlIDCode:string,
   PrintProgram:string,
   CustomerList:string,
   ShipToList:string,
   PCID:string,
   PromptUser:boolean,
   RowSeq:number,
      /**  Indicates if cust part can be enabled or not.  */  
   EnableCustPart:boolean,
      /**  Indicates if quantity per container can be enabled or not.  */  
   EnableQtyPer:boolean,
   SourcePCID:string,
      /**  Warehouse code affected by the generation of the PCID in Ad hoc PCID  */  
   WarehouseCode:string,
      /**  Warehouse Bin. Set in Ad hoc PCID  */  
   BinNum:string,
      /**  Warehouse bin description  */  
   BinDesc:string,
      /**  Quantity of labels to print  */  
   NumLabelsToPrint:number,
      /**  Indicates if the Number To Generate field should be enabled  */  
   EnableNumberToGen:boolean,
      /**  Screen that is using the BO  */  
   WhoCalled:string,
   ConvFactor:number,
      /**  Warehouse type. Some vaild options are STOCK, WIP and QUALITY  */  
   WarehouseType:string,
      /**  When user sets to True the system will write out to the StageHeader and StageItem tables instead of the PCID Inventory tables (PkgControlHeader / PkgControlItem).  */  
   AdhocStagedInventory:boolean,
   IsMES:boolean,
   EmpID:string,
      /**  Report style taken from the label type record  */  
   ReportStyle:number,
   WhseDesc:string,
   ScanPCID:string,
      /**  Raw barcode scanned PCID  */  
   RawBarcodeScan:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Ship To List using standard delimiters  */  
   ShipToStdList:string,
   WarehouseList:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlGenPCIDTableset{
   PkgControlGenPCID:Erp_Tablesets_PkgControlGenPCIDRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param whoCalled
      @param ds
   */  
export interface GeneratePCIDList_input{
      /**  Form that is calling this method  */  
   whoCalled:string,
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface GeneratePCIDList_output{
      /**  The generated PCID  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   pcidRange:string,
   returnMessage:string,
}
}

   /** Required : 
      @param whoCalled
      @param ds
   */  
export interface GeneratePCID_input{
      /**  Form that is calling this method  */  
   whoCalled:string,
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface GeneratePCID_output{
      /**  The generated PCID  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   rangeMessage:string,
}
}

   /** Required : 
      @param ipCompany
      @param ipPartNum
      @param refPkgCode
      @param custNum
      @param shipToNum
   */  
export interface GetPackageCode_input{
   ipCompany:string,
   ipPartNum:string,
   refPkgCode:string,
   custNum:number,
   shipToNum:string,
}

export interface GetPackageCode_output{
parameters : {
      /**  output parameters  */  
   refPkgCode:string,
   outPkgCodeDesc:string,
}
}

   /** Required : 
      @param ipJobNum
      @param ipCustID
      @param ipXPartNum
      @param ipPartNum
      @param ipKeyFieldName
      @param ipWhoCalled
      @param isMES
      @param empIDorUserID
      @param ipRawPCID
      @param custXPrtRowID
   */  
export interface GetTempRow_input{
   ipJobNum:string,
   ipCustID:string,
   ipXPartNum:string,
   ipPartNum:string,
   ipKeyFieldName:string,
   ipWhoCalled:string,
   isMES:boolean,
   empIDorUserID:string,
   ipRawPCID:string,
   custXPrtRowID:string,
}

export interface GetTempRow_output{
   returnObj:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

   /** Required : 
      @param ipPartNum
   */  
export interface GetWarehouseList_input{
   ipPartNum:string,
}

export interface GetWarehouseList_output{
parameters : {
      /**  output parameters  */  
   WarehouseList:string,
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

   /** Required : 
      @param ipWriteToStaged
   */  
export interface IsAutoPrintSetup_input{
      /**  write to staged table  */  
   ipWriteToStaged:boolean,
}

export interface IsAutoPrintSetup_output{
   returnObj:boolean,
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
export interface NegativeInventoryTest_input{
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

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param ipPCID
      @param ds
   */  
export interface PerformMaterialMovement_input{
   ipPCID:string,
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface PerformMaterialMovement_output{
parameters : {
      /**  output parameters  */  
   legalNumberMessage:string,
   partTranPKs:string,
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PkgCodeChanged_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface PkgCodeChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param whoCalled
      @param ds
   */  
export interface PkgControlGenPCIDXPartChanged_input{
   whoCalled:string,
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface PkgControlGenPCIDXPartChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param historyList
      @param returnList
   */  
export interface ReturnValidItems_input{
   historyList:string,
   returnList:string,
}

export interface ReturnValidItems_output{
parameters : {
      /**  output parameters  */  
   returnList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SetPCIDLabelTypeInfo_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface SetPCIDLabelTypeInfo_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ShipToChanged_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface ShipToChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param empID
   */  
export interface SuppressPrintMessages_input{
      /**  Employee ID  */  
   empID:string,
}

export interface SuppressPrintMessages_output{
      /**  True if messages should be hidden  */  
   returnObj:boolean,
}

   /** Required : 
      @param proposedCustID
      @param partNum
      @param pkgCode
      @param calledFrom
   */  
export interface ValidateCustomer_input{
   proposedCustID:string,
   partNum:string,
   pkgCode:string,
   calledFrom:string,
}

export interface ValidateCustomer_output{
}

   /** Required : 
      @param jobNum
      @param whoCalled
   */  
export interface ValidateJob_input{
   jobNum:string,
   whoCalled:string,
}

export interface ValidateJob_output{
}

   /** Required : 
      @param proposedNumberToGen
   */  
export interface ValidateNumberToGen_input{
      /**  proposedNumberToGen  */  
   proposedNumberToGen:string,
}

export interface ValidateNumberToGen_output{
}

   /** Required : 
      @param proposedPkgCode
   */  
export interface ValidatePkgCode_input{
      /**  proposedPkgCode  */  
   proposedPkgCode:string,
}

export interface ValidatePkgCode_output{
}

   /** Required : 
      @param proposedShift
   */  
export interface ValidateShift_input{
      /**  proposedShift  */  
   proposedShift:string,
}

export interface ValidateShift_output{
}

   /** Required : 
      @param custNum
      @param proposedShipTo
      @param partNum
      @param pkgCode
      @param calledFrom
   */  
export interface ValidateShipTo_input{
   custNum:number,
   proposedShipTo:string,
   partNum:string,
   pkgCode:string,
   calledFrom:string,
}

export interface ValidateShipTo_output{
}

   /** Required : 
      @param ipSourcePCID
   */  
export interface ValidateSourcePCID_input{
   ipSourcePCID:string,
}

export interface ValidateSourcePCID_output{
}

   /** Required : 
      @param ToWhse
      @param ToBinNum
   */  
export interface ValidateWhseBinPCID_input{
      /**  Warehouse  */  
   ToWhse:string,
      /**  Bin Num to validate  */  
   ToBinNum:string,
}

export interface ValidateWhseBinPCID_output{
   returnObj:boolean,
}

   /** Required : 
      @param toWhse
      @param partNum
      @param warehouseType
   */  
export interface ValidateWhsePCID_input{
      /**  Warehouse to validate.  */  
   toWhse:string,
      /**  PartNum  */  
   partNum:string,
      /**  warehouseType  */  
   warehouseType:string,
}

export interface ValidateWhsePCID_output{
   returnObj:boolean,
}

   /** Required : 
      @param proposedCustID
      @param proposedXPart
      @param pkgCode
      @param shipToNum
      @param calledFrom
   */  
export interface ValidateXPart_input{
   proposedCustID:string,
   proposedXPart:string,
   pkgCode:string,
   shipToNum:string,
   calledFrom:string,
}

export interface ValidateXPart_output{
parameters : {
      /**  output parameters  */  
   multipleMatches:boolean,
   newProposedXPart:string,
}
}

   /** Required : 
      @param ds
   */  
export interface WarehouseCodeChanged_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface WarehouseCodeChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface XPartChanged_input{
   ds:Erp_Tablesets_PkgControlGenPCIDTableset[],
}

export interface XPartChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlGenPCIDTableset,
}
}

