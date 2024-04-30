import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.IoTDeviceSvc
// Description: IoT Device allowing configuration and communication with IoT Hub
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get IoTDevices items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IoTDevices
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceRow
   */  
export function get_IoTDevices(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IoTDevices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.IoTDeviceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IoTDevices(requestBody:Ice_Tablesets_IoTDeviceRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the IoTDevice item
   Description: Calls GetByID to retrieve the IoTDevice item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IoTDevice
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.IoTDeviceRow
   */  
export function get_IoTDevices_Company_DeviceID(Company:string, DeviceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_IoTDeviceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices(" + Company + "," + DeviceID + ")", {
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
         resolve(data as Ice_Tablesets_IoTDeviceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update IoTDevice for the service
   Description: Calls UpdateExt to update IoTDevice. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IoTDevice
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_IoTDevices_Company_DeviceID(Company:string, DeviceID:string, requestBody:Ice_Tablesets_IoTDeviceRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices(" + Company + "," + DeviceID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete IoTDevice item
   Description: Call UpdateExt to delete IoTDevice item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IoTDevice
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_IoTDevices_Company_DeviceID(Company:string, DeviceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices(" + Company + "," + DeviceID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get IoTDeviceRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IoTDeviceRules
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceRuleRow
   */  
export function get_IoTDeviceRules(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IoTDeviceRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IoTDeviceRules(requestBody:Ice_Tablesets_IoTDeviceRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the IoTDeviceRule item
   Description: Calls GetByID to retrieve the IoTDeviceRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IoTDeviceRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param RuleID Desc: RuleID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
   */  
export function get_IoTDeviceRules_Company_DeviceID_RuleID(Company:string, DeviceID:string, RuleID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_IoTDeviceRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules(" + Company + "," + DeviceID + "," + RuleID + ")", {
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
         resolve(data as Ice_Tablesets_IoTDeviceRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update IoTDeviceRule for the service
   Description: Calls UpdateExt to update IoTDeviceRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IoTDeviceRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param RuleID Desc: RuleID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_IoTDeviceRules_Company_DeviceID_RuleID(Company:string, DeviceID:string, RuleID:string, requestBody:Ice_Tablesets_IoTDeviceRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules(" + Company + "," + DeviceID + "," + RuleID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete IoTDeviceRule item
   Description: Call UpdateExt to delete IoTDeviceRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IoTDeviceRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param RuleID Desc: RuleID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_IoTDeviceRules_Company_DeviceID_RuleID(Company:string, DeviceID:string, RuleID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules(" + Company + "," + DeviceID + "," + RuleID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get IoTDeviceStatus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IoTDeviceStatus
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceStatusRow
   */  
export function get_IoTDeviceStatus(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IoTDeviceStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IoTDeviceStatus(requestBody:Ice_Tablesets_IoTDeviceStatusRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the IoTDeviceStatu item
   Description: Calls GetByID to retrieve the IoTDeviceStatu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IoTDeviceStatu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
   */  
export function get_IoTDeviceStatus_Company_DeviceID(Company:string, DeviceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_IoTDeviceStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus(" + Company + "," + DeviceID + ")", {
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
         resolve(data as Ice_Tablesets_IoTDeviceStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update IoTDeviceStatu for the service
   Description: Calls UpdateExt to update IoTDeviceStatu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IoTDeviceStatu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_IoTDeviceStatus_Company_DeviceID(Company:string, DeviceID:string, requestBody:Ice_Tablesets_IoTDeviceStatusRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus(" + Company + "," + DeviceID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete IoTDeviceStatu item
   Description: Call UpdateExt to delete IoTDeviceStatu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IoTDeviceStatu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DeviceID Desc: DeviceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_IoTDeviceStatus_Company_DeviceID(Company:string, DeviceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus(" + Company + "," + DeviceID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseIoTDevice:string, whereClauseIoTDeviceRule:string, whereClauseIoTDeviceStatus:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseIoTDevice!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseIoTDevice=" + whereClauseIoTDevice
   }
   if(typeof whereClauseIoTDeviceRule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseIoTDeviceRule=" + whereClauseIoTDeviceRule
   }
   if(typeof whereClauseIoTDeviceStatus!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseIoTDeviceStatus=" + whereClauseIoTDeviceStatus
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(deviceID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof deviceID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "deviceID=" + deviceID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailableRelatedTo
   Description: Gets a list of available related to which have searches available.
   OperationID: GetAvailableRelatedTo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableRelatedTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableRelatedTo(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailableRelatedTo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetAvailableRelatedTo", {
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
         resolve(data as GetAvailableRelatedTo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDeviceRules
   Description: Deprecated: the method is used for the classic UI only.
Get applicable rules for the Device and whether they are currently active
This includes any assigned by associated group. Inactive rules are not included.
   OperationID: GetDeviceRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDeviceRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeviceRules(requestBody:GetDeviceRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDeviceRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetDeviceRules", {
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
         resolve(data as GetDeviceRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDeviceStatus
   Description: Deprecated: the method is used for the classic UI only.
Get the status of a device from IoT Hub
   OperationID: GetDeviceStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDeviceStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeviceStatus(requestBody:GetDeviceStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDeviceStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetDeviceStatus", {
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
         resolve(data as GetDeviceStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDeviceTwin
   Description: Get all the Device Twin Properties from IoT Hub
   OperationID: GetDeviceTwin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDeviceTwin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceTwin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeviceTwin(requestBody:GetDeviceTwin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDeviceTwin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetDeviceTwin", {
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
         resolve(data as GetDeviceTwin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateDeviceTwin
   Description: Update the Device Twin desired properties for a device
   OperationID: UpdateDeviceTwin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateDeviceTwin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDeviceTwin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDeviceTwin(requestBody:UpdateDeviceTwin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateDeviceTwin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/UpdateDeviceTwin", {
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
         resolve(data as UpdateDeviceTwin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SendDeviceMessage
   Description: Sends a Cloud to Device message via the IoT Hub
   OperationID: SendDeviceMessage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SendDeviceMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendDeviceMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SendDeviceMessage(requestBody:SendDeviceMessage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SendDeviceMessage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/SendDeviceMessage", {
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
         resolve(data as SendDeviceMessage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SendDeviceData
   Description: Sends a Cloud to Device message via the IoT Hub
   OperationID: SendDeviceData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SendDeviceData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendDeviceData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SendDeviceData(requestBody:SendDeviceData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SendDeviceData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/SendDeviceData", {
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
         resolve(data as SendDeviceData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RetrieveMissingDevicesFromIoTHuB
   Description: Get a dataset of devices that exist in IoT Hub but have not been configured within ERP
   OperationID: RetrieveMissingDevicesFromIoTHuB
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveMissingDevicesFromIoTHuB_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveMissingDevicesFromIoTHuB(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RetrieveMissingDevicesFromIoTHuB_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/RetrieveMissingDevicesFromIoTHuB", {
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
         resolve(data as RetrieveMissingDevicesFromIoTHuB_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMissingDevicesFromIoTHub
   Description: Deprecated: the method is used for the classic UI only.
Get a list of devices that exist in IoT Hub but have not been configured within ERP
   OperationID: GetMissingDevicesFromIoTHub
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMissingDevicesFromIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMissingDevicesFromIoTHub(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMissingDevicesFromIoTHub_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetMissingDevicesFromIoTHub", {
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
         resolve(data as GetMissingDevicesFromIoTHub_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateDevicesToERPFromIoTHub
   Description: Add one or more devices that exist in the IoT Hub but have not yet been created within ERP
   OperationID: UpdateDevicesToERPFromIoTHub
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateDevicesToERPFromIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDevicesToERPFromIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateDevicesToERPFromIoTHub(requestBody:UpdateDevicesToERPFromIoTHub_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateDevicesToERPFromIoTHub_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/UpdateDevicesToERPFromIoTHub", {
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
         resolve(data as UpdateDevicesToERPFromIoTHub_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddMissingDevicesFromIoTHub
   Description: Deprecated: the method is used for the classic UI only.
Add one or more devices that exist in the IoT Hub but have not yet been created within ERP
   OperationID: AddMissingDevicesFromIoTHub
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddMissingDevicesFromIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMissingDevicesFromIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddMissingDevicesFromIoTHub(requestBody:AddMissingDevicesFromIoTHub_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddMissingDevicesFromIoTHub_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/AddMissingDevicesFromIoTHub", {
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
         resolve(data as AddMissingDevicesFromIoTHub_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UploadDevicesToIoTHub
   Description: Add one or more devices that exist in ERP but have not yet been created within IoT Hub
   OperationID: UploadDevicesToIoTHub
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UploadDevicesToIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadDevicesToIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadDevicesToIoTHub(requestBody:UploadDevicesToIoTHub_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UploadDevicesToIoTHub_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/UploadDevicesToIoTHub", {
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
         resolve(data as UploadDevicesToIoTHub_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddDevicesToIoTHub
   Description: Deprecated: the method is used for the classic UI only.
Add one or more devices that exist in ERP but have not yet been created within IoT Hub
   OperationID: AddDevicesToIoTHub
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddDevicesToIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddDevicesToIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddDevicesToIoTHub(requestBody:AddDevicesToIoTHub_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddDevicesToIoTHub_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/AddDevicesToIoTHub", {
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
         resolve(data as AddDevicesToIoTHub_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateDeviceGroupID
   Description: Verifies if a device group ID is valid
   OperationID: ValidateDeviceGroupID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateDeviceGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDeviceGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateDeviceGroupID(requestBody:ValidateDeviceGroupID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateDeviceGroupID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/ValidateDeviceGroupID", {
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
         resolve(data as ValidateDeviceGroupID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UploadImage
   Description: Upload an image for the Device to be used on the widget
   OperationID: UploadImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UploadImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadImage(requestBody:UploadImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UploadImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/UploadImage", {
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
         resolve(data as UploadImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveImage
   Description: Remove an image for the Device
   OperationID: RemoveImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveImage(requestBody:RemoveImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/RemoveImage", {
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
         resolve(data as RemoveImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DownloadImage
   Description: Download an image assigned to a Device. If there is no image assigned nothing is returned
   OperationID: DownloadImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DownloadImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadImage(requestBody:DownloadImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DownloadImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/DownloadImage", {
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
         resolve(data as DownloadImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSysRowID
   OperationID: ChangeSysRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSysRowID(requestBody:ChangeSysRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/ChangeSysRowID", {
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
         resolve(data as ChangeSysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RetrieveDeviceRules
   Description: Get applicable rules for the Device and whether they are currently active
This includes any assigned by associated group. Inactive rules are not included.
   OperationID: RetrieveDeviceRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RetrieveDeviceRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveDeviceRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveDeviceRules(requestBody:RetrieveDeviceRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RetrieveDeviceRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/RetrieveDeviceRules", {
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
         resolve(data as RetrieveDeviceRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RetrieveDeviceStatus
   Description: Get the status of a device from IoT Hub
   OperationID: RetrieveDeviceStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RetrieveDeviceStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveDeviceStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveDeviceStatus(requestBody:RetrieveDeviceStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RetrieveDeviceStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/RetrieveDeviceStatus", {
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
         resolve(data as RetrieveDeviceStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDeviceTwinDatasetForTree
   Description: Get all the Device Twin Properties from IoT Hub
   OperationID: GetDeviceTwinDatasetForTree
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDeviceTwinDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceTwinDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDeviceTwinDatasetForTree(requestBody:GetDeviceTwinDatasetForTree_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDeviceTwinDatasetForTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetDeviceTwinDatasetForTree", {
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
         resolve(data as GetDeviceTwinDatasetForTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelatedToKeyDescription
   Description: Get Related To Description
   OperationID: GetRelatedToKeyDescription
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelatedToKeyDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedToKeyDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelatedToKeyDescription(requestBody:GetRelatedToKeyDescription_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelatedToKeyDescription_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetRelatedToKeyDescription", {
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
         resolve(data as GetRelatedToKeyDescription_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultSearch
   Description: Get default search for specified table
   OperationID: GetDefaultSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultSearch(requestBody:GetDefaultSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetDefaultSearch", {
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
         resolve(data as GetDefaultSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewIoTDevice
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIoTDevice
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewIoTDevice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIoTDevice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewIoTDevice(requestBody:GetNewIoTDevice_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewIoTDevice_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetNewIoTDevice", {
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
         resolve(data as GetNewIoTDevice_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/Update", {
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
         resolve(data as Update_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_IoTDeviceListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRow{
   "odatametadata":string,
   "value":Ice_Tablesets_IoTDeviceRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRuleRow{
   "odatametadata":string,
   "value":Ice_Tablesets_IoTDeviceRuleRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceStatusRow{
   "odatametadata":string,
   "value":Ice_Tablesets_IoTDeviceStatusRow,
}

export interface Ice_Tablesets_IoTDeviceListRow{
      /**  Company  */  
   "Company":string,
      /**  DeviceID  */  
   "DeviceID":string,
      /**  Description  */  
   "Description":string,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_IoTDeviceRow{
      /**  Company  */  
   "Company":string,
      /**  DeviceID  */  
   "DeviceID":string,
      /**  Description  */  
   "Description":string,
      /**  Inactive  */  
   "Inactive":boolean,
      /**  GroupID  */  
   "GroupID":string,
      /**  RelatedToSchemaName  */  
   "RelatedToSchemaName":string,
      /**  RelatedToTableName  */  
   "RelatedToTableName":string,
      /**  RelatedToSysRowID  */  
   "RelatedToSysRowID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "RelatedToDescription":string,
   "BitFlag":number,
   "IoTDeviceGroupLinkDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_IoTDeviceRuleRow{
   "Active":boolean,
   "Company":string,
   "Description":string,
   "DeviceID":string,
   "RuleID":string,
   "Stateful":boolean,
   "StoreEventData":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_IoTDeviceStatusRow{
   "Company":string,
   "DeviceID":string,
   "DeviceOnline":boolean,
   "DeviceStatus":string,
   "HubRegistered":boolean,
   "IoTEdge":boolean,
   "AuthenticationType":string,
   "LastActivity":string,
   "LastStatusUpdate":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param deviceIDs
   */  
export interface AddDevicesToIoTHub_input{
   deviceIDs:string,
}

export interface AddDevicesToIoTHub_output{
}

   /** Required : 
      @param deviceIDs
   */  
export interface AddMissingDevicesFromIoTHub_input{
      /**  Collection of Device IDs  */  
   deviceIDs:string,
}

export interface AddMissingDevicesFromIoTHub_output{
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param sysRowID
      @param ds
   */  
export interface ChangeSysRowID_input{
   sysRowID:string,
   ds:Ice_Tablesets_IoTDeviceTableset[],
}

export interface ChangeSysRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_IoTDeviceTableset,
}
}

   /** Required : 
      @param deviceID
   */  
export interface DeleteByID_input{
   deviceID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param deviceID
   */  
export interface DownloadImage_input{
      /**  Device ID  */  
   deviceID:string,
}

export interface DownloadImage_output{
      /**  Image data  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   fileName:string,
   mimeType:string,
}
}

export interface GetAvailableRelatedTo_output{
   returnObj:Ice_Tablesets_IoTDeviceRelatedToTableset[],
}

   /** Required : 
      @param deviceID
   */  
export interface GetByID_input{
   deviceID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_IoTDeviceTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_IoTDeviceTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_IoTDeviceTableset[],
}

   /** Required : 
      @param systemCode
      @param tableName
   */  
export interface GetDefaultSearch_input{
      /**  System code of the table  */  
   systemCode:string,
      /**  Name of the table  */  
   tableName:string,
}

export interface GetDefaultSearch_output{
parameters : {
      /**  output parameters  */  
   folderName:string,
   subfolderName:string,
}
}

   /** Required : 
      @param ts
      @param deviceID
   */  
export interface GetDeviceRules_input{
   ts:Ice_Tablesets_IoTDeviceTableset[],
      /**  Device ID  */  
   deviceID:string,
}

export interface GetDeviceRules_output{
parameters : {
      /**  output parameters  */  
   ts:Ice_Tablesets_IoTDeviceTableset,
}
}

   /** Required : 
      @param ts
      @param deviceID
   */  
export interface GetDeviceStatus_input{
   ts:Ice_Tablesets_IoTDeviceTableset[],
      /**  Device ID  */  
   deviceID:string,
}

export interface GetDeviceStatus_output{
parameters : {
      /**  output parameters  */  
   ts:Ice_Tablesets_IoTDeviceTableset,
}
}

   /** Required : 
      @param deviceID
      @param errorOnNotFound
   */  
export interface GetDeviceTwinDatasetForTree_input{
      /**  Device ID within Company  */  
   deviceID:string,
      /**  Flag whether to error if the twin is not found  */  
   errorOnNotFound:boolean,
}

export interface GetDeviceTwinDatasetForTree_output{
   returnObj:Ice_Tablesets_IoTDeviceTwinTableset[],
}

   /** Required : 
      @param deviceID
      @param errorOnNotFound
   */  
export interface GetDeviceTwin_input{
      /**  Device ID within Company  */  
   deviceID:string,
      /**  Flag whether to error if the twin is not found  */  
   errorOnNotFound:boolean,
}

export interface GetDeviceTwin_output{
      /**  Device JSON Twin  */  
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Ice_Tablesets_IoTDeviceListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetMissingDevicesFromIoTHub_output{
      /**  Collection of Device IDs  */  
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetNewIoTDevice_input{
   ds:Ice_Tablesets_IoTDeviceTableset[],
}

export interface GetNewIoTDevice_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_IoTDeviceTableset,
}
}

   /** Required : 
      @param schemaName
      @param tableName
      @param sysRowID
   */  
export interface GetRelatedToKeyDescription_input{
      /**  Related To Schema Name  */  
   schemaName:string,
      /**  Related To Table Name  */  
   tableName:string,
      /**  Related To SysRowID  */  
   sysRowID:string,
}

export interface GetRelatedToKeyDescription_output{
      /**  RelatedToDescription string  */  
   returnObj:string,
}

   /** Required : 
      @param whereClauseIoTDevice
      @param whereClauseIoTDeviceRule
      @param whereClauseIoTDeviceStatus
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseIoTDevice:string,
   whereClauseIoTDeviceRule:string,
   whereClauseIoTDeviceStatus:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_IoTDeviceTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Ice_Tablesets_IoTDeviceListRow{
      /**  Company  */  
   Company:string,
      /**  DeviceID  */  
   DeviceID:string,
      /**  Description  */  
   Description:string,
      /**  Inactive  */  
   Inactive:boolean,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IoTDeviceListTableset{
   IoTDeviceList:Ice_Tablesets_IoTDeviceListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_IoTDeviceRelatedToRow{
   SystemCode:string,
   ClassName:string,
   DataTableID:string,
   DBTableName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IoTDeviceRelatedToTableset{
   IoTDeviceRelatedTo:Ice_Tablesets_IoTDeviceRelatedToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_IoTDeviceRow{
      /**  Company  */  
   Company:string,
      /**  DeviceID  */  
   DeviceID:string,
      /**  Description  */  
   Description:string,
      /**  Inactive  */  
   Inactive:boolean,
      /**  GroupID  */  
   GroupID:string,
      /**  RelatedToSchemaName  */  
   RelatedToSchemaName:string,
      /**  RelatedToTableName  */  
   RelatedToTableName:string,
      /**  RelatedToSysRowID  */  
   RelatedToSysRowID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   RelatedToDescription:string,
   BitFlag:number,
   IoTDeviceGroupLinkDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IoTDeviceRuleRow{
   Active:boolean,
   Company:string,
   Description:string,
   DeviceID:string,
   RuleID:string,
   Stateful:boolean,
   StoreEventData:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IoTDeviceSelectionRow{
   DeviceID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IoTDeviceSelectionTableset{
   IoTDeviceSelection:Ice_Tablesets_IoTDeviceSelectionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_IoTDeviceStatusRow{
   Company:string,
   DeviceID:string,
   DeviceOnline:boolean,
   DeviceStatus:string,
   HubRegistered:boolean,
   IoTEdge:boolean,
   AuthenticationType:string,
   LastActivity:string,
   LastStatusUpdate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IoTDeviceTableset{
   IoTDevice:Ice_Tablesets_IoTDeviceRow[],
   IoTDeviceRule:Ice_Tablesets_IoTDeviceRuleRow[],
   IoTDeviceStatus:Ice_Tablesets_IoTDeviceStatusRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_IoTDeviceTwinDataRow{
   Id:number,
   ParentId:number,
   Key:string,
   Value:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_IoTDeviceTwinTableset{
   IoTDeviceTwinData:Ice_Tablesets_IoTDeviceTwinDataRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtIoTDeviceTableset{
   IoTDevice:Ice_Tablesets_IoTDeviceRow[],
   IoTDeviceRule:Ice_Tablesets_IoTDeviceRuleRow[],
   IoTDeviceStatus:Ice_Tablesets_IoTDeviceStatusRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param deviceID
   */  
export interface RemoveImage_input{
      /**  Device ID  */  
   deviceID:string,
}

export interface RemoveImage_output{
}

   /** Required : 
      @param deviceID
   */  
export interface RetrieveDeviceRules_input{
      /**  Device ID  */  
   deviceID:string,
}

export interface RetrieveDeviceRules_output{
   returnObj:Ice_Tablesets_IoTDeviceTableset[],
}

   /** Required : 
      @param deviceID
   */  
export interface RetrieveDeviceStatus_input{
      /**  Device ID  */  
   deviceID:string,
}

export interface RetrieveDeviceStatus_output{
   returnObj:Ice_Tablesets_IoTDeviceTableset[],
}

export interface RetrieveMissingDevicesFromIoTHuB_output{
   returnObj:Ice_Tablesets_IoTDeviceSelectionTableset[],
}

   /** Required : 
      @param deviceID
      @param byteArray
   */  
export interface SendDeviceData_input{
      /**  Device ID  */  
   deviceID:string,
      /**  Byte data  */  
   byteArray:string,
}

export interface SendDeviceData_output{
}

   /** Required : 
      @param deviceID
      @param message
   */  
export interface SendDeviceMessage_input{
      /**  Device ID  */  
   deviceID:string,
      /**  Message encoded as UTF8  */  
   message:string,
}

export interface SendDeviceMessage_output{
}

   /** Required : 
      @param deviceID
      @param jsonTwinPatch
   */  
export interface UpdateDeviceTwin_input{
      /**  Device ID within Company  */  
   deviceID:string,
      /**  JSON Twin patch data  */  
   jsonTwinPatch:string,
}

export interface UpdateDeviceTwin_output{
}

   /** Required : 
      @param deviceIDs
   */  
export interface UpdateDevicesToERPFromIoTHub_input{
      /**  String of Device IDs delimeted by '~'  */  
   deviceIDs:string,
}

export interface UpdateDevicesToERPFromIoTHub_output{
      /**  message  */  
   returnObj:string,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtIoTDeviceTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtIoTDeviceTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_IoTDeviceTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_IoTDeviceTableset,
}
}

   /** Required : 
      @param deviceIDs
   */  
export interface UploadDevicesToIoTHub_input{
      /**  String of Device IDs delimeted by '~'  */  
   deviceIDs:string,
}

export interface UploadDevicesToIoTHub_output{
}

   /** Required : 
      @param deviceID
      @param data
      @param fileName
   */  
export interface UploadImage_input{
      /**  Device ID  */  
   deviceID:string,
      /**  Image data  */  
   data:string,
      /**  Filename of image  */  
   fileName:string,
}

export interface UploadImage_output{
}

   /** Required : 
      @param deviceGroupID
   */  
export interface ValidateDeviceGroupID_input{
      /**  GroupID to validate  */  
   deviceGroupID:string,
}

export interface ValidateDeviceGroupID_output{
}

