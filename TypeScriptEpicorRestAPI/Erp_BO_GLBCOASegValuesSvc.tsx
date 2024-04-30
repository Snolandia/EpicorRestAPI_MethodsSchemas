import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLBCOASegValuesSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/$metadata", {
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
   Description: Get GLBCOASegValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegValues
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegValuesRow
   */  
export function get_GLBCOASegValues(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLBCOASegValues(requestBody:Erp_Tablesets_GLBCOASegValuesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues", {
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
   Summary: Calls GetByID to retrieve the GLBCOASegValue item
   Description: Calls GetByID to retrieve the GLBCOASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   */  
export function get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
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
         resolve(data as Erp_Tablesets_GLBCOASegValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLBCOASegValue for the service
   Description: Calls UpdateExt to update GLBCOASegValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, requestBody:Erp_Tablesets_GLBCOASegValuesRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
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
   Summary: Call UpdateExt to delete GLBCOASegValue item
   Description: Call UpdateExt to delete GLBCOASegValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
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
   Description: Get GLBCOASegOpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBCOASegOpts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegOptRow
   */  
export function get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_GLBCOASegOpts(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/GLBCOASegOpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLBCOASegOpt item
   Description: Calls GetByID to retrieve the GLBCOASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegOpt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   */  
export function get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
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
         resolve(data as Erp_Tablesets_GLBCOASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegOptRow
   */  
export function get_GLBCOASegOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLBCOASegOptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLBCOASegOpts(requestBody:Erp_Tablesets_GLBCOASegOptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts", {
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
   Summary: Calls GetByID to retrieve the GLBCOASegOpt item
   Description: Calls GetByID to retrieve the GLBCOASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   */  
export function get_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegOptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
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
         resolve(data as Erp_Tablesets_GLBCOASegOptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLBCOASegOpt for the service
   Description: Calls UpdateExt to update GLBCOASegOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, requestBody:Erp_Tablesets_GLBCOASegOptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
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
   Summary: Call UpdateExt to delete GLBCOASegOpt item
   Description: Call UpdateExt to delete GLBCOASegOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param SubSegmentNbr Desc: SubSegmentNbr   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, SubSegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegValuesListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseGLBCOASegValues:string, whereClauseGLBCOASegOpt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLBCOASegValues!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBCOASegValues=" + whereClauseGLBCOASegValues
   }
   if(typeof whereClauseGLBCOASegOpt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBCOASegOpt=" + whereClauseGLBCOASegOpt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(extCompanyID:string, coACode:string, segmentNbr:string, segmentCode:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof extCompanyID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "extCompanyID=" + extCompanyID
   }
   if(typeof coACode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "coACode=" + coACode
   }
   if(typeof segmentNbr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "segmentNbr=" + segmentNbr
   }
   if(typeof segmentCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "segmentCode=" + segmentCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGLBCOASegValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBCOASegValues(requestBody:GetNewGLBCOASegValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLBCOASegValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GetNewGLBCOASegValues", {
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
         resolve(data as GetNewGLBCOASegValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLBCOASegOpt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegOpt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBCOASegOpt(requestBody:GetNewGLBCOASegOpt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLBCOASegOpt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GetNewGLBCOASegOpt", {
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
         resolve(data as GetNewGLBCOASegOpt_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegOptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOASegOptRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOASegValuesListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOASegValuesRow,
}

export interface Erp_Tablesets_GLBCOASegOptRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  System generated sequence number  */  
   "SubSegmentNbr":number,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   "ValOption":string,
      /**  Indicates the default segment value to be used for this natural account.  */  
   "DefaultSegment":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLBCOASegValuesListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Name of Segment Value  */  
   "SegmentName":string,
      /**  Segment description.  */  
   "SegmentDesc":string,
      /**  Short name of the segment value.  */  
   "SegmentAbbrev":string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   "ActiveFlag":boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   "EffectiveFrom":string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   "EffectiveTo":string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   "Category":string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   "NormalBalance":string,
      /**  Rate type used for debit balances.  */  
   "DebitRateType":string,
      /**  Rate type used for credit balances  */  
   "CreditRateType":string,
      /**  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  */  
   "CurrencyCode":string,
   "CurrAcct":boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  */  
   "RefEntityType":string,
   "Summarization":number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   "MatchingEnabled":boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLBCOASegValuesRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Segment value used to construct the GL Account.  */  
   "SegmentCode":string,
      /**  Name of Segment Value  */  
   "SegmentName":string,
      /**  Segment description.  */  
   "SegmentDesc":string,
      /**  Short name of the segment value.  */  
   "SegmentAbbrev":string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   "ActiveFlag":boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   "EffectiveFrom":string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   "EffectiveTo":string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   "Category":string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   "NormalBalance":string,
      /**  Rate type used for debit balances.  */  
   "DebitRateType":string,
      /**  Rate type used for credit balances  */  
   "CreditRateType":string,
      /**  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  */  
   "CurrencyCode":string,
   "CurrAcct":boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  */  
   "RefEntityType":string,
   "Summarization":number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   "MatchingEnabled":boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  StatUOMCode  */  
   "StatUOMCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ReverseCategory  */  
   "ReverseCategory":string,
      /**  ExtAnalysisCode  */  
   "ExtAnalysisCode":string,
      /**  CurrencyAcctType  */  
   "CurrencyAcctType":string,
      /**  RevalueOpt  */  
   "RevalueOpt":number,
      /**  GLGainAcctContext  */  
   "GLGainAcctContext":string,
      /**  GLLossAcctContext  */  
   "GLLossAcctContext":string,
      /**  GainAccount  */  
   "GainAccount":string,
      /**  LossAccount  */  
   "LossAccount":string,
      /**  AccrualAccount  */  
   "AccrualAccount":string,
      /**  GainSegVal1  */  
   "GainSegVal1":string,
      /**  GainSegVal2  */  
   "GainSegVal2":string,
      /**  GainSegVal3  */  
   "GainSegVal3":string,
      /**  GainSegVal4  */  
   "GainSegVal4":string,
      /**  GainSegVal5  */  
   "GainSegVal5":string,
      /**  GainSegVal6  */  
   "GainSegVal6":string,
      /**  GainSegVal7  */  
   "GainSegVal7":string,
      /**  GainSegVal8  */  
   "GainSegVal8":string,
      /**  GainSegVal9  */  
   "GainSegVal9":string,
      /**  GainSegVal10  */  
   "GainSegVal10":string,
      /**  GainSegVal11  */  
   "GainSegVal11":string,
      /**  GainSegVal12  */  
   "GainSegVal12":string,
      /**  GainSegVal13  */  
   "GainSegVal13":string,
      /**  GainSegVal14  */  
   "GainSegVal14":string,
      /**  GainSegVal15  */  
   "GainSegVal15":string,
      /**  GainSegVal16  */  
   "GainSegVal16":string,
      /**  GainSegVal17  */  
   "GainSegVal17":string,
      /**  GainSegVal18  */  
   "GainSegVal18":string,
      /**  GainSegVal19  */  
   "GainSegVal19":string,
      /**  GainSegVal20  */  
   "GainSegVal20":string,
      /**  LossSegVal1  */  
   "LossSegVal1":string,
      /**  LossSegVal2  */  
   "LossSegVal2":string,
      /**  LossSegVal3  */  
   "LossSegVal3":string,
      /**  LossSegVal4  */  
   "LossSegVal4":string,
      /**  LossSegVal5  */  
   "LossSegVal5":string,
      /**  LossSegVal6  */  
   "LossSegVal6":string,
      /**  LossSegVal7  */  
   "LossSegVal7":string,
      /**  LossSegVal8  */  
   "LossSegVal8":string,
      /**  LossSegVal9  */  
   "LossSegVal9":string,
      /**  LossSegVal10  */  
   "LossSegVal10":string,
      /**  LossSegVal11  */  
   "LossSegVal11":string,
      /**  LossSegVal12  */  
   "LossSegVal12":string,
      /**  LossSegVal13  */  
   "LossSegVal13":string,
      /**  LossSegVal14  */  
   "LossSegVal14":string,
      /**  LossSegVal15  */  
   "LossSegVal15":string,
      /**  LossSegVal16  */  
   "LossSegVal16":string,
      /**  LossSegVal17  */  
   "LossSegVal17":string,
      /**  LossSegVal18  */  
   "LossSegVal18":string,
      /**  LossSegVal19  */  
   "LossSegVal19":string,
      /**  LossSegVal20  */  
   "LossSegVal20":string,
      /**  AccrualSegVal1  */  
   "AccrualSegVal1":string,
      /**  AccrualSegVal2  */  
   "AccrualSegVal2":string,
      /**  AccrualSegVal3  */  
   "AccrualSegVal3":string,
      /**  AccrualSegVal4  */  
   "AccrualSegVal4":string,
      /**  AccrualSegVal5  */  
   "AccrualSegVal5":string,
      /**  AccrualSegVal6  */  
   "AccrualSegVal6":string,
      /**  AccrualSegVal7  */  
   "AccrualSegVal7":string,
      /**  AccrualSegVal8  */  
   "AccrualSegVal8":string,
      /**  AccrualSegVal9  */  
   "AccrualSegVal9":string,
      /**  AccrualSegVal10  */  
   "AccrualSegVal10":string,
      /**  AccrualSegVal11  */  
   "AccrualSegVal11":string,
      /**  AccrualSegVal12  */  
   "AccrualSegVal12":string,
      /**  AccrualSegVal13  */  
   "AccrualSegVal13":string,
      /**  AccrualSegVal14  */  
   "AccrualSegVal14":string,
      /**  AccrualSegVal15  */  
   "AccrualSegVal15":string,
      /**  AccrualSegVal16  */  
   "AccrualSegVal16":string,
      /**  AccrualSegVal17  */  
   "AccrualSegVal17":string,
      /**  AccrualSegVal18  */  
   "AccrualSegVal18":string,
      /**  AccrualSegVal19  */  
   "AccrualSegVal19":string,
      /**  AccrualSegVal20  */  
   "AccrualSegVal20":string,
      /**  COSegDtlNbr  */  
   "COSegDtlNbr":number,
      /**  COPrintBalanceInvDtl  */  
   "COPrintBalanceInvDtl":boolean,
      /**  BENAEID  */  
   "BENAEID":string,
      /**  Mapped  */  
   "Mapped":boolean,
      /**  ReportCategory  */  
   "ReportCategory":string,
      /**  ReverseReportCategory  */  
   "ReverseReportCategory":string,
      /**  LinkedPlant  */  
   "LinkedPlant":string,
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
      @param extCompanyID
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface DeleteByID_input{
   extCompanyID:string,
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLBCOASegOptRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  System generated sequence number  */  
   SubSegmentNbr:number,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   ValOption:string,
      /**  Indicates the default segment value to be used for this natural account.  */  
   DefaultSegment:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBCOASegValuesListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Name of Segment Value  */  
   SegmentName:string,
      /**  Segment description.  */  
   SegmentDesc:string,
      /**  Short name of the segment value.  */  
   SegmentAbbrev:string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   ActiveFlag:boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   EffectiveFrom:string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   EffectiveTo:string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   Category:string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   NormalBalance:string,
      /**  Rate type used for debit balances.  */  
   DebitRateType:string,
      /**  Rate type used for credit balances  */  
   CreditRateType:string,
      /**  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  */  
   CurrencyCode:string,
   CurrAcct:boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  */  
   RefEntityType:string,
   Summarization:number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   MatchingEnabled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBCOASegValuesListTableset{
   GLBCOASegValuesList:Erp_Tablesets_GLBCOASegValuesListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLBCOASegValuesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Segment value used to construct the GL Account.  */  
   SegmentCode:string,
      /**  Name of Segment Value  */  
   SegmentName:string,
      /**  Segment description.  */  
   SegmentDesc:string,
      /**  Short name of the segment value.  */  
   SegmentAbbrev:string,
      /**  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  */  
   ActiveFlag:boolean,
      /**  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  */  
   EffectiveFrom:string,
      /**  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  */  
   EffectiveTo:string,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   Category:string,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   NormalBalance:string,
      /**  Rate type used for debit balances.  */  
   DebitRateType:string,
      /**  Rate type used for credit balances  */  
   CreditRateType:string,
      /**  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  */  
   CurrencyCode:string,
   CurrAcct:boolean,
      /**  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  */  
   RefEntityType:string,
   Summarization:number,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched.  */  
   MatchingEnabled:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  StatUOMCode  */  
   StatUOMCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ReverseCategory  */  
   ReverseCategory:string,
      /**  ExtAnalysisCode  */  
   ExtAnalysisCode:string,
      /**  CurrencyAcctType  */  
   CurrencyAcctType:string,
      /**  RevalueOpt  */  
   RevalueOpt:number,
      /**  GLGainAcctContext  */  
   GLGainAcctContext:string,
      /**  GLLossAcctContext  */  
   GLLossAcctContext:string,
      /**  GainAccount  */  
   GainAccount:string,
      /**  LossAccount  */  
   LossAccount:string,
      /**  AccrualAccount  */  
   AccrualAccount:string,
      /**  GainSegVal1  */  
   GainSegVal1:string,
      /**  GainSegVal2  */  
   GainSegVal2:string,
      /**  GainSegVal3  */  
   GainSegVal3:string,
      /**  GainSegVal4  */  
   GainSegVal4:string,
      /**  GainSegVal5  */  
   GainSegVal5:string,
      /**  GainSegVal6  */  
   GainSegVal6:string,
      /**  GainSegVal7  */  
   GainSegVal7:string,
      /**  GainSegVal8  */  
   GainSegVal8:string,
      /**  GainSegVal9  */  
   GainSegVal9:string,
      /**  GainSegVal10  */  
   GainSegVal10:string,
      /**  GainSegVal11  */  
   GainSegVal11:string,
      /**  GainSegVal12  */  
   GainSegVal12:string,
      /**  GainSegVal13  */  
   GainSegVal13:string,
      /**  GainSegVal14  */  
   GainSegVal14:string,
      /**  GainSegVal15  */  
   GainSegVal15:string,
      /**  GainSegVal16  */  
   GainSegVal16:string,
      /**  GainSegVal17  */  
   GainSegVal17:string,
      /**  GainSegVal18  */  
   GainSegVal18:string,
      /**  GainSegVal19  */  
   GainSegVal19:string,
      /**  GainSegVal20  */  
   GainSegVal20:string,
      /**  LossSegVal1  */  
   LossSegVal1:string,
      /**  LossSegVal2  */  
   LossSegVal2:string,
      /**  LossSegVal3  */  
   LossSegVal3:string,
      /**  LossSegVal4  */  
   LossSegVal4:string,
      /**  LossSegVal5  */  
   LossSegVal5:string,
      /**  LossSegVal6  */  
   LossSegVal6:string,
      /**  LossSegVal7  */  
   LossSegVal7:string,
      /**  LossSegVal8  */  
   LossSegVal8:string,
      /**  LossSegVal9  */  
   LossSegVal9:string,
      /**  LossSegVal10  */  
   LossSegVal10:string,
      /**  LossSegVal11  */  
   LossSegVal11:string,
      /**  LossSegVal12  */  
   LossSegVal12:string,
      /**  LossSegVal13  */  
   LossSegVal13:string,
      /**  LossSegVal14  */  
   LossSegVal14:string,
      /**  LossSegVal15  */  
   LossSegVal15:string,
      /**  LossSegVal16  */  
   LossSegVal16:string,
      /**  LossSegVal17  */  
   LossSegVal17:string,
      /**  LossSegVal18  */  
   LossSegVal18:string,
      /**  LossSegVal19  */  
   LossSegVal19:string,
      /**  LossSegVal20  */  
   LossSegVal20:string,
      /**  AccrualSegVal1  */  
   AccrualSegVal1:string,
      /**  AccrualSegVal2  */  
   AccrualSegVal2:string,
      /**  AccrualSegVal3  */  
   AccrualSegVal3:string,
      /**  AccrualSegVal4  */  
   AccrualSegVal4:string,
      /**  AccrualSegVal5  */  
   AccrualSegVal5:string,
      /**  AccrualSegVal6  */  
   AccrualSegVal6:string,
      /**  AccrualSegVal7  */  
   AccrualSegVal7:string,
      /**  AccrualSegVal8  */  
   AccrualSegVal8:string,
      /**  AccrualSegVal9  */  
   AccrualSegVal9:string,
      /**  AccrualSegVal10  */  
   AccrualSegVal10:string,
      /**  AccrualSegVal11  */  
   AccrualSegVal11:string,
      /**  AccrualSegVal12  */  
   AccrualSegVal12:string,
      /**  AccrualSegVal13  */  
   AccrualSegVal13:string,
      /**  AccrualSegVal14  */  
   AccrualSegVal14:string,
      /**  AccrualSegVal15  */  
   AccrualSegVal15:string,
      /**  AccrualSegVal16  */  
   AccrualSegVal16:string,
      /**  AccrualSegVal17  */  
   AccrualSegVal17:string,
      /**  AccrualSegVal18  */  
   AccrualSegVal18:string,
      /**  AccrualSegVal19  */  
   AccrualSegVal19:string,
      /**  AccrualSegVal20  */  
   AccrualSegVal20:string,
      /**  COSegDtlNbr  */  
   COSegDtlNbr:number,
      /**  COPrintBalanceInvDtl  */  
   COPrintBalanceInvDtl:boolean,
      /**  BENAEID  */  
   BENAEID:string,
      /**  Mapped  */  
   Mapped:boolean,
      /**  ReportCategory  */  
   ReportCategory:string,
      /**  ReverseReportCategory  */  
   ReverseReportCategory:string,
      /**  LinkedPlant  */  
   LinkedPlant:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBCOASegValuesTableset{
   GLBCOASegValues:Erp_Tablesets_GLBCOASegValuesRow[],
   GLBCOASegOpt:Erp_Tablesets_GLBCOASegOptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGLBCOASegValuesTableset{
   GLBCOASegValues:Erp_Tablesets_GLBCOASegValuesRow[],
   GLBCOASegOpt:Erp_Tablesets_GLBCOASegOptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param extCompanyID
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface GetByID_input{
   extCompanyID:string,
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLBCOASegValuesTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLBCOASegValuesTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLBCOASegValuesTableset[],
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
   returnObj:Erp_Tablesets_GLBCOASegValuesListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param coACode
      @param segmentNbr
      @param segmentCode
   */  
export interface GetNewGLBCOASegOpt_input{
   ds:Erp_Tablesets_GLBCOASegValuesTableset[],
   extCompanyID:string,
   coACode:string,
   segmentNbr:number,
   segmentCode:string,
}

export interface GetNewGLBCOASegOpt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOASegValuesTableset,
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param coACode
      @param segmentNbr
   */  
export interface GetNewGLBCOASegValues_input{
   ds:Erp_Tablesets_GLBCOASegValuesTableset[],
   extCompanyID:string,
   coACode:string,
   segmentNbr:number,
}

export interface GetNewGLBCOASegValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOASegValuesTableset,
}
}

   /** Required : 
      @param whereClauseGLBCOASegValues
      @param whereClauseGLBCOASegOpt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLBCOASegValues:string,
   whereClauseGLBCOASegOpt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLBCOASegValuesTableset[],
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

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGLBCOASegValuesTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLBCOASegValuesTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLBCOASegValuesTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOASegValuesTableset,
}
}

