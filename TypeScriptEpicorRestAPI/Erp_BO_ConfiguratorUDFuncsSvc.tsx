import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ConfiguratorUDFuncsSvc
// Description: This Business Object allows the modification of Configurator User Defined Functions
            This Object is intent to replace the calls to Customer own code in .i and .p files with User Defined Functions in C#
           
            Business Object for the Configurator User Defined Functions Entry
            Alejandro Martinez
            08/26/2013
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/$metadata", {
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
   Description: Get ConfiguratorUDFuncs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfiguratorUDFuncs
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefRow
   */  
export function get_ConfiguratorUDFuncs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfiguratorUDFuncs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PcFunctionDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfiguratorUDFuncs(requestBody:Erp_Tablesets_PcFunctionDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs", {
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
   Summary: Calls GetByID to retrieve the ConfiguratorUDFunc item
   Description: Calls GetByID to retrieve the ConfiguratorUDFunc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfiguratorUDFunc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcFunctionDefRow
   */  
export function get_ConfiguratorUDFuncs_Company_ConfigID_FunctionName(Company:string, ConfigID:string, FunctionName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcFunctionDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")", {
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
         resolve(data as Erp_Tablesets_PcFunctionDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConfiguratorUDFunc for the service
   Description: Calls UpdateExt to update ConfiguratorUDFunc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfiguratorUDFunc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConfiguratorUDFuncs_Company_ConfigID_FunctionName(Company:string, ConfigID:string, FunctionName:string, requestBody:Erp_Tablesets_PcFunctionDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")", {
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
   Summary: Call UpdateExt to delete ConfiguratorUDFunc item
   Description: Call UpdateExt to delete ConfiguratorUDFunc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfiguratorUDFunc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConfiguratorUDFuncs_Company_ConfigID_FunctionName(Company:string, ConfigID:string, FunctionName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get PcFunctionDefAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcFunctionDefAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefAttchRow
   */  
export function get_ConfiguratorUDFuncs_Company_ConfigID_FunctionName_PcFunctionDefAttches(Company:string, ConfigID:string, FunctionName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")/PcFunctionDefAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcFunctionDefAttch item
   Description: Calls GetByID to retrieve the PcFunctionDefAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcFunctionDefAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   */  
export function get_ConfiguratorUDFuncs_Company_ConfigID_FunctionName_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company:string, ConfigID:string, FunctionName:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcFunctionDefAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PcFunctionDefAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcFunctionDefAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcFunctionDefAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefAttchRow
   */  
export function get_PcFunctionDefAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcFunctionDefAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcFunctionDefAttches(requestBody:Erp_Tablesets_PcFunctionDefAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches", {
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
   Summary: Calls GetByID to retrieve the PcFunctionDefAttch item
   Description: Calls GetByID to retrieve the PcFunctionDefAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcFunctionDefAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   */  
export function get_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company:string, ConfigID:string, FunctionName:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcFunctionDefAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PcFunctionDefAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcFunctionDefAttch for the service
   Description: Calls UpdateExt to update PcFunctionDefAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcFunctionDefAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company:string, ConfigID:string, FunctionName:string, DrawingSeq:string, requestBody:Erp_Tablesets_PcFunctionDefAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PcFunctionDefAttch item
   Description: Call UpdateExt to delete PcFunctionDefAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcFunctionDefAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company:string, ConfigID:string, FunctionName:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")", {
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
   Description: Get PcFunctionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcFunctionParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionParamRow
   */  
export function get_PcFunctionParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcFunctionParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcFunctionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PcFunctionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcFunctionParams(requestBody:Erp_Tablesets_PcFunctionParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams", {
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
   Summary: Calls GetByID to retrieve the PcFunctionParam item
   Description: Calls GetByID to retrieve the PcFunctionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcFunctionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PcFunctionParamRow
   */  
export function get_PcFunctionParams_Company_ConfigID_FunctionName_ParameterName(Company:string, ConfigID:string, FunctionName:string, ParameterName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcFunctionParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams(" + Company + "," + ConfigID + "," + FunctionName + "," + ParameterName + ")", {
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
         resolve(data as Erp_Tablesets_PcFunctionParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcFunctionParam for the service
   Description: Calls UpdateExt to update PcFunctionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcFunctionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcFunctionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcFunctionParams_Company_ConfigID_FunctionName_ParameterName(Company:string, ConfigID:string, FunctionName:string, ParameterName:string, requestBody:Erp_Tablesets_PcFunctionParamRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams(" + Company + "," + ConfigID + "," + FunctionName + "," + ParameterName + ")", {
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
   Summary: Call UpdateExt to delete PcFunctionParam item
   Description: Call UpdateExt to delete PcFunctionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcFunctionParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param FunctionName Desc: FunctionName   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcFunctionParams_Company_ConfigID_FunctionName_ParameterName(Company:string, ConfigID:string, FunctionName:string, ParameterName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams(" + Company + "," + ConfigID + "," + FunctionName + "," + ParameterName + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefListRow)
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
export function get_GetRows(whereClausePcFunctionDef:string, whereClausePcFunctionDefAttch:string, whereClausePcFunctionParam:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePcFunctionDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcFunctionDef=" + whereClausePcFunctionDef
   }
   if(typeof whereClausePcFunctionDefAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcFunctionDefAttch=" + whereClausePcFunctionDefAttch
   }
   if(typeof whereClausePcFunctionParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcFunctionParam=" + whereClausePcFunctionParam
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(configID:string, functionName:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof configID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "configID=" + configID
   }
   if(typeof functionName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "functionName=" + functionName
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetList" + params, {
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
   Summary: Invoke method ValidateConfigID
   Description: Validates if the configuration ID Exist in the Catalog.
   OperationID: ValidateConfigID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateConfigID(requestBody:ValidateConfigID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateConfigID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ValidateConfigID", {
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
         resolve(data as ValidateConfigID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateConfigForCopyMethod
   Description: Verify the method being copied is valid for the target configuration
   OperationID: ValidateConfigForCopyMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateConfigForCopyMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateConfigForCopyMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateConfigForCopyMethod(requestBody:ValidateConfigForCopyMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateConfigForCopyMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ValidateConfigForCopyMethod", {
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
         resolve(data as ValidateConfigForCopyMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveOnePosition
   Description: This Method moves Up and Down Parameter for User Defined Functions one possitio
in the grid and returns the whole updated DataTable
   OperationID: MoveOnePosition
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveOnePosition(requestBody:MoveOnePosition_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveOnePosition_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/MoveOnePosition", {
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
         resolve(data as MoveOnePosition_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DoGetNewParamSequence
   Description: This Method Returns the corresponding new Parameter Sequence for the new Parameter.
   OperationID: DoGetNewParamSequence
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DoGetNewParamSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoGetNewParamSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DoGetNewParamSequence(requestBody:DoGetNewParamSequence_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DoGetNewParamSequence_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/DoGetNewParamSequence", {
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
         resolve(data as DoGetNewParamSequence_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFunctionTypeChanges
   Description: Executes the IsTheMethodInUse logic and checks EWC types to inform user typescript code will be reset to string.empty when changing from client to server.
   OperationID: ValidateFunctionTypeChanges
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFunctionTypeChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFunctionTypeChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFunctionTypeChanges(requestBody:ValidateFunctionTypeChanges_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFunctionTypeChanges_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ValidateFunctionTypeChanges", {
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
         resolve(data as ValidateFunctionTypeChanges_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePcFunctionParamBeforeDelete
   Description: Determine if the method is in use before deleting the parameter so the appropriate warning can be presented to the user
   OperationID: ValidatePcFunctionParamBeforeDelete
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePcFunctionParamBeforeDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcFunctionParamBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePcFunctionParamBeforeDelete(requestBody:ValidatePcFunctionParamBeforeDelete_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePcFunctionParamBeforeDelete_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ValidatePcFunctionParamBeforeDelete", {
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
         resolve(data as ValidatePcFunctionParamBeforeDelete_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsTheMethodInUse
   Description: Use this method to determine if a method is in use prior to renaming it
   OperationID: IsTheMethodInUse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsTheMethodInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTheMethodInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsTheMethodInUse(requestBody:IsTheMethodInUse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsTheMethodInUse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/IsTheMethodInUse", {
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
         resolve(data as IsTheMethodInUse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RenameMethod
   Description: This Method Renames the User Defined Method name.
   OperationID: RenameMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RenameMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RenameMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RenameMethod(requestBody:RenameMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RenameMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/RenameMethod", {
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
         resolve(data as RenameMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyMethod
   Description: This Method Copies a user defined method to a different Configurator.
   OperationID: CopyMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyMethod(requestBody:CopyMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/CopyMethod", {
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
         resolve(data as CopyMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateName
   Description: This method Validates if the specified string contains spaces in there and throws an exception in that case.
   OperationID: ValidateName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateName(requestBody:ValidateName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ValidateName", {
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
         resolve(data as ValidateName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMethod
   Description: This method Validates if the specified method already exist in the target configurator.
   OperationID: ValidateMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMethod(requestBody:ValidateMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ValidateMethod", {
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
         resolve(data as ValidateMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateEWCReturnType
   Description: This method Validates if the return type is valid for the type of configurator and the type of function defined
   OperationID: ValidateEWCReturnType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateEWCReturnType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEWCReturnType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateEWCReturnType(requestBody:ValidateEWCReturnType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateEWCReturnType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ValidateEWCReturnType", {
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
         resolve(data as ValidateEWCReturnType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParametersForCodeEditor
   Description: Returns a list of all the parameters within the Method specified.
   OperationID: GetParametersForCodeEditor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetParametersForCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParametersForCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParametersForCodeEditor(requestBody:GetParametersForCodeEditor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetParametersForCodeEditor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetParametersForCodeEditor", {
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
         resolve(data as GetParametersForCodeEditor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveNewCode
   Description: This method Saves the expression code returned from Code Editor.
   OperationID: SaveNewCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveNewCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveNewCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveNewCode(requestBody:SaveNewCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveNewCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/SaveNewCode", {
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
         resolve(data as SaveNewCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveNewScriptCode
   Description: This method Saves the Script expression code returned from Code Editor for client UDMethods.
   OperationID: SaveNewScriptCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveNewScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveNewScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveNewScriptCode(requestBody:SaveNewScriptCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveNewScriptCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/SaveNewScriptCode", {
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
         resolve(data as SaveNewScriptCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFunctionType
   Description: Set SendValues when function type changes
   OperationID: OnChangeFunctionType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFunctionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFunctionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFunctionType(requestBody:OnChangeFunctionType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFunctionType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/OnChangeFunctionType", {
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
         resolve(data as OnChangeFunctionType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MethodUsesInputs
   Description: Set SendValues when function type changes
   OperationID: MethodUsesInputs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MethodUsesInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MethodUsesInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MethodUsesInputs(requestBody:MethodUsesInputs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MethodUsesInputs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/MethodUsesInputs", {
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
         resolve(data as MethodUsesInputs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetUDMethodsForCodeEditor
   Description: retrieves data needed by the Code Editor
   OperationID: GetUDMethodsForCodeEditor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetUDMethodsForCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUDMethodsForCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUDMethodsForCodeEditor(requestBody:GetUDMethodsForCodeEditor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetUDMethodsForCodeEditor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetUDMethodsForCodeEditor", {
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
         resolve(data as GetUDMethodsForCodeEditor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcFunctionDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcFunctionDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPcFunctionDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcFunctionDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcFunctionDef(requestBody:GetNewPcFunctionDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPcFunctionDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetNewPcFunctionDef", {
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
         resolve(data as GetNewPcFunctionDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcFunctionDefAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcFunctionDefAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPcFunctionDefAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcFunctionDefAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcFunctionDefAttch(requestBody:GetNewPcFunctionDefAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPcFunctionDefAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetNewPcFunctionDefAttch", {
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
         resolve(data as GetNewPcFunctionDefAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcFunctionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcFunctionParam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPcFunctionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcFunctionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcFunctionParam(requestBody:GetNewPcFunctionParam_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPcFunctionParam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetNewPcFunctionParam", {
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
         resolve(data as GetNewPcFunctionParam_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcFunctionDefAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcFunctionDefListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcFunctionDefRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcFunctionParamRow,
}

export interface Erp_Tablesets_PcFunctionDefAttchRow{
   "Company":string,
   "ConfigID":string,
   "FunctionName":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcFunctionDefListRow{
      /**  Company  */  
   "Company":string,
      /**  FunctionName  */  
   "FunctionName":string,
      /**  Description  */  
   "Description":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  FunctionType  */  
   "FunctionType":string,
      /**  ReturnType  */  
   "ReturnType":string,
      /**  SysRowID  */  
   "SysRowID":string,
   "ParamsExist":boolean,
   "ExtConfig":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcFunctionDefRow{
      /**  Company  */  
   "Company":string,
      /**  FunctionName  */  
   "FunctionName":string,
      /**  Description  */  
   "Description":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  FunctionType  */  
   "FunctionType":string,
      /**  Expression  */  
   "Expression":string,
      /**  ReturnType  */  
   "ReturnType":string,
      /**  OldFunctionName  */  
   "OldFunctionName":string,
      /**  IsSync  */  
   "IsSync":boolean,
      /**  GlobalFunc  */  
   "GlobalFunc":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  BagID  */  
   "BagID":string,
      /**  NoInputs  */  
   "NoInputs":boolean,
      /**  ScriptExpression  */  
   "ScriptExpression":string,
   "DispFunctionName":string,
   "DispFunctionType":string,
   "DispReturnType":string,
      /**  Script expressions are only permitted for PCEMF configurator client expressions.  */  
   "BtnEditScript":boolean,
   "BitFlag":number,
   "PcStatusConfigType":string,
   "PcStatusApproved":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcFunctionParamRow{
      /**  Company  */  
   "Company":string,
      /**  FunctionName  */  
   "FunctionName":string,
      /**  ParameterName  */  
   "ParameterName":string,
      /**  DefaultValue  */  
   "DefaultValue":string,
      /**  Modifier  */  
   "Modifier":string,
      /**  ParamType  */  
   "ParamType":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  ParamSeq  */  
   "ParamSeq":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
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
      @param sourceConfigID
      @param sourceMethodName
      @param targetConfigID
      @param targetMethodName
      @param ds
   */  
export interface CopyMethod_input{
      /**  This the source Configuration ID  */  
   sourceConfigID:string,
      /**  This is the source method Name  */  
   sourceMethodName:string,
      /**  This os the new Method  */  
   targetConfigID:string,
      /**  This is the Original method Name  */  
   targetMethodName:string,
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

export interface CopyMethod_output{
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

   /** Required : 
      @param configID
      @param functionName
   */  
export interface DeleteByID_input{
   configID:string,
   functionName:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param configID
      @param functionName
   */  
export interface DoGetNewParamSequence_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Function or Method Name  */  
   functionName:string,
}

export interface DoGetNewParamSequence_output{
      /**  The new Sequence  */  
   returnObj:number,
}

export interface Erp_Tablesets_CodeEditorPCFuncParamRow{
   ParameterName:string,
   ParameterType:string,
   Modifier:string,
   DefaultValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCInputsRow{
   InputName:string,
   InputType:string,
   DataType:string,
   PcDynLstCount:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfigUDCodEditorRow{
   Company:string,
   ConfigID:string,
   FunctionName:string,
   MethodDeclaration:string,
   MethodToolTip:string,
   DataType:string,
      /**  The tokenized text used for the expression builder.  */  
   TokenizedText:string,
   MethodType:string,
   CodeEditorText:string,
   ExcludeFromExpressionBuilder:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfigUDCodeEditorTableset{
   ConfigUDCodEditor:Erp_Tablesets_ConfigUDCodEditorRow[],
   CodeEditorPCFuncParam:Erp_Tablesets_CodeEditorPCFuncParamRow[],
   CodeEditorPCInputs:Erp_Tablesets_CodeEditorPCInputsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfiguratorUDFuncsListTableset{
   PcFunctionDefList:Erp_Tablesets_PcFunctionDefListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfiguratorUDFuncsTableset{
   PcFunctionDef:Erp_Tablesets_PcFunctionDefRow[],
   PcFunctionDefAttch:Erp_Tablesets_PcFunctionDefAttchRow[],
   PcFunctionParam:Erp_Tablesets_PcFunctionParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcFunctionDefAttchRow{
   Company:string,
   ConfigID:string,
   FunctionName:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcFunctionDefListRow{
      /**  Company  */  
   Company:string,
      /**  FunctionName  */  
   FunctionName:string,
      /**  Description  */  
   Description:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  FunctionType  */  
   FunctionType:string,
      /**  ReturnType  */  
   ReturnType:string,
      /**  SysRowID  */  
   SysRowID:string,
   ParamsExist:boolean,
   ExtConfig:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcFunctionDefRow{
      /**  Company  */  
   Company:string,
      /**  FunctionName  */  
   FunctionName:string,
      /**  Description  */  
   Description:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  FunctionType  */  
   FunctionType:string,
      /**  Expression  */  
   Expression:string,
      /**  ReturnType  */  
   ReturnType:string,
      /**  OldFunctionName  */  
   OldFunctionName:string,
      /**  IsSync  */  
   IsSync:boolean,
      /**  GlobalFunc  */  
   GlobalFunc:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  BagID  */  
   BagID:string,
      /**  NoInputs  */  
   NoInputs:boolean,
      /**  ScriptExpression  */  
   ScriptExpression:string,
   DispFunctionName:string,
   DispFunctionType:string,
   DispReturnType:string,
      /**  Script expressions are only permitted for PCEMF configurator client expressions.  */  
   BtnEditScript:boolean,
   BitFlag:number,
   PcStatusConfigType:string,
   PcStatusApproved:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcFunctionParamRow{
      /**  Company  */  
   Company:string,
      /**  FunctionName  */  
   FunctionName:string,
      /**  ParameterName  */  
   ParameterName:string,
      /**  DefaultValue  */  
   DefaultValue:string,
      /**  Modifier  */  
   Modifier:string,
      /**  ParamType  */  
   ParamType:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ParamSeq  */  
   ParamSeq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtConfiguratorUDFuncsTableset{
   PcFunctionDef:Erp_Tablesets_PcFunctionDefRow[],
   PcFunctionDefAttch:Erp_Tablesets_PcFunctionDefAttchRow[],
   PcFunctionParam:Erp_Tablesets_PcFunctionParamRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param configID
      @param functionName
   */  
export interface GetByID_input{
   configID:string,
   functionName:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name  */  
   tableName:string,
      /**  The field name.  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
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
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param configID
      @param functionName
   */  
export interface GetNewPcFunctionDefAttch_input{
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
   configID:string,
   functionName:string,
}

export interface GetNewPcFunctionDefAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset,
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcFunctionDef_input{
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
   configID:string,
}

export interface GetNewPcFunctionDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset,
}
}

   /** Required : 
      @param ds
      @param configID
      @param functionName
   */  
export interface GetNewPcFunctionParam_input{
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
   configID:string,
   functionName:string,
}

export interface GetNewPcFunctionParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset,
}
}

   /** Required : 
      @param configID
      @param functionName
   */  
export interface GetParametersForCodeEditor_input{
      /**  Configudation ID  */  
   configID:string,
      /**  Method Name  */  
   functionName:string,
}

export interface GetParametersForCodeEditor_output{
   returnObj:Erp_Tablesets_ConfigUDCodeEditorTableset[],
}

   /** Required : 
      @param whereClausePcFunctionDef
      @param whereClausePcFunctionDefAttch
      @param whereClausePcFunctionParam
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePcFunctionDef:string,
   whereClausePcFunctionDefAttch:string,
   whereClausePcFunctionParam:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ConfigID
      @param FunctionType
      @param fromUDMethods
   */  
export interface GetUDMethodsForCodeEditor_input{
   ConfigID:string,
   FunctionType:string,
   fromUDMethods:boolean,
}

export interface GetUDMethodsForCodeEditor_output{
   returnObj:Erp_Tablesets_ConfigUDCodeEditorTableset[],
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

   /** Required : 
      @param configID
      @param currentMethodName
   */  
export interface IsTheMethodInUse_input{
   configID:string,
   currentMethodName:string,
}

export interface IsTheMethodInUse_output{
parameters : {
      /**  output parameters  */  
   inUseMessage:string,
}
}

   /** Required : 
      @param configID
      @param methodName
   */  
export interface MethodUsesInputs_input{
      /**  The configurator's id.  */  
   configID:string,
      /**  The method's name  */  
   methodName:string,
}

export interface MethodUsesInputs_output{
   returnObj:boolean,
}

   /** Required : 
      @param configID
      @param functionName
      @param parameterName
      @param paramSeq
      @param moveDir
   */  
export interface MoveOnePosition_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Function or Method Name  */  
   functionName:string,
      /**  Parameter Name  */  
   parameterName:string,
      /**  Current Sequence of the Parameter being moved  */  
   paramSeq:number,
      /**  Direction to move the Parameter "Up" or "Down"  */  
   moveDir:string,
}

export interface MoveOnePosition_output{
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

   /** Required : 
      @param inputName
      @param ds
   */  
export interface OnChangeFunctionType_input{
      /**  The control name.  */  
   inputName:string,
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

export interface OnChangeFunctionType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset,
}
}

   /** Required : 
      @param configID
      @param oldMethodName
      @param newMethodName
      @param ds
   */  
export interface RenameMethod_input{
      /**  This os the new Method  */  
   configID:string,
      /**  This is the Original method Name  */  
   oldMethodName:string,
      /**  This os the new Method  */  
   newMethodName:string,
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

export interface RenameMethod_output{
   returnObj:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

   /** Required : 
      @param configID
      @param functionName
      @param newCode
   */  
export interface SaveNewCode_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Function Name  */  
   functionName:string,
      /**  New Expression Code to be saved  */  
   newCode:string,
}

export interface SaveNewCode_output{
      /**  true/False depending if the  */  
   returnObj:boolean,
}

   /** Required : 
      @param configID
      @param functionName
      @param newCode
   */  
export interface SaveNewScriptCode_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Function Name  */  
   functionName:string,
      /**  New Expression Code to be saved  */  
   newCode:string,
}

export interface SaveNewScriptCode_output{
      /**  true/False depending if the  */  
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConfiguratorUDFuncsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConfiguratorUDFuncsTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorUDFuncsTableset,
}
}

   /** Required : 
      @param sourceConfigID
      @param sourceMethod
      @param targetConfigID
   */  
export interface ValidateConfigForCopyMethod_input{
   sourceConfigID:string,
   sourceMethod:string,
   targetConfigID:string,
}

export interface ValidateConfigForCopyMethod_output{
}

   /** Required : 
      @param proposedConfigID
   */  
export interface ValidateConfigID_input{
   proposedConfigID:string,
}

export interface ValidateConfigID_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   configApproved:boolean,
   configType:string,
}
}

   /** Required : 
      @param functionType
      @param returnType
   */  
export interface ValidateEWCReturnType_input{
      /**  This is the function type: client or server  */  
   functionType:string,
      /**  This is the return type used for the function  */  
   returnType:string,
}

export interface ValidateEWCReturnType_output{
   returnObj:boolean,
}

   /** Required : 
      @param configID
      @param currentMethodName
      @param proposedFunctionType
   */  
export interface ValidateFunctionTypeChanges_input{
      /**  Configuration ID  */  
   configID:string,
      /**  method being validated  */  
   currentMethodName:string,
      /**  proposed function type - server or client  */  
   proposedFunctionType:string,
}

export interface ValidateFunctionTypeChanges_output{
parameters : {
      /**  output parameters  */  
   inUseMessage:string,
   EWCWarningMessage:string,
}
}

   /** Required : 
      @param configID
      @param methodName
   */  
export interface ValidateMethod_input{
      /**  This is target or destination Configurator where the method will be copied.  */  
   configID:string,
      /**  The name of the target method.  */  
   methodName:string,
}

export interface ValidateMethod_output{
   returnObj:boolean,
}

   /** Required : 
      @param name
      @param from
   */  
export interface ValidateName_input{
      /**  String provided for a MethodName or ParameterName.  */  
   name:string,
      /**  Indicates if the name belongs to a method or parameter.  */  
   from:string,
}

export interface ValidateName_output{
   returnObj:boolean,
}

   /** Required : 
      @param configID
      @param functionName
   */  
export interface ValidatePcFunctionParamBeforeDelete_input{
   configID:string,
   functionName:string,
}

export interface ValidatePcFunctionParamBeforeDelete_output{
parameters : {
      /**  output parameters  */  
   inUseMessage:string,
}
}

