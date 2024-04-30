import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLBCOASvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/$metadata", {
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
   Description: Get GLBCOAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOAs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOARow
   */  
export function get_GLBCOAs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOAs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLBCOARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLBCOAs(requestBody:Erp_Tablesets_GLBCOARow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs", {
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
   Summary: Calls GetByID to retrieve the GLBCOA item
   Description: Calls GetByID to retrieve the GLBCOA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOARow
   */  
export function get_GLBCOAs_Company_ExtCompanyID_COACode(Company:string, ExtCompanyID:string, COACode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOARow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")", {
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
         resolve(data as Erp_Tablesets_GLBCOARow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLBCOA for the service
   Description: Calls UpdateExt to update GLBCOA. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLBCOAs_Company_ExtCompanyID_COACode(Company:string, ExtCompanyID:string, COACode:string, requestBody:Erp_Tablesets_GLBCOARow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")", {
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
   Summary: Call UpdateExt to delete GLBCOA item
   Description: Call UpdateExt to delete GLBCOA item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOA
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLBCOAs_Company_ExtCompanyID_COACode(Company:string, ExtCompanyID:string, COACode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")", {
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
   Description: Get GLBCOASegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBCOASegments1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentRow
   */  
export function get_GLBCOAs_Company_ExtCompanyID_COACode_GLBCOASegments(Company:string, ExtCompanyID:string, COACode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")/GLBCOASegments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLBCOASegment item
   Description: Calls GetByID to retrieve the GLBCOASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegment1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   */  
export function get_GLBCOAs_Company_ExtCompanyID_COACode_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOAs(" + Company + "," + ExtCompanyID + "," + COACode + ")/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", {
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
         resolve(data as Erp_Tablesets_GLBCOASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegments
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegmentRow
   */  
export function get_GLBCOASegments(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLBCOASegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLBCOASegments(requestBody:Erp_Tablesets_GLBCOASegmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments", {
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
   Summary: Calls GetByID to retrieve the GLBCOASegment item
   Description: Calls GetByID to retrieve the GLBCOASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   */  
export function get_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", {
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
         resolve(data as Erp_Tablesets_GLBCOASegmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLBCOASegment for the service
   Description: Calls UpdateExt to update GLBCOASegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, requestBody:Erp_Tablesets_GLBCOASegmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", {
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
   Summary: Call UpdateExt to delete GLBCOASegment item
   Description: Call UpdateExt to delete GLBCOASegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegment
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")", {
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
   Description: Get GLBCOASegValues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBCOASegValues1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param select Desc: Odata select comma delimited list of fields
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
export function get_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr_GLBCOASegValues(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")/GLBCOASegValues", {
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
   Summary: Calls GetByID to retrieve the GLBCOASegValue item
   Description: Calls GetByID to retrieve the GLBCOASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegValue1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ExtCompanyID Desc: ExtCompanyID   Required: True   Allow empty value : True
      @param COACode Desc: COACode   Required: True   Allow empty value : True
      @param SegmentNbr Desc: SegmentNbr   Required: True
      @param SegmentCode Desc: SegmentCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   */  
export function get_GLBCOASegments_Company_ExtCompanyID_COACode_SegmentNbr_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegments(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + ")/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegValues
      @param select Desc: Odata select comma delimited list of fields
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
export function get_GLBCOASegValues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues", {
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
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   */  
export function get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company:string, ExtCompanyID:string, COACode:string, SegmentNbr:string, SegmentCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLBCOASegValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOAListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOAListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOAListRow)
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
export function get_GetRows(whereClauseGLBCOA:string, whereClauseGLBCOASegment:string, whereClauseGLBCOASegValues:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLBCOA!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBCOA=" + whereClauseGLBCOA
   }
   if(typeof whereClauseGLBCOASegment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBCOASegment=" + whereClauseGLBCOASegment
   }
   if(typeof whereClauseGLBCOASegValues!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLBCOASegValues=" + whereClauseGLBCOASegValues
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetRows" + params, {
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
export function get_GetByID(extCompanyID:string, coACode:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetList" + params, {
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
   Summary: Invoke method GetNewGLBCOA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBCOA(requestBody:GetNewGLBCOA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLBCOA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetNewGLBCOA", {
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
         resolve(data as GetNewGLBCOA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLBCOASegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLBCOASegment(requestBody:GetNewGLBCOASegment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLBCOASegment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetNewGLBCOASegment", {
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
         resolve(data as GetNewGLBCOASegment_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetNewGLBCOASegValues", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOAListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOAListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOARow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOARow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOASegValuesRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegmentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLBCOASegmentRow,
}

export interface Erp_Tablesets_GLBCOAListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "Description":string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  */  
   "SeparatorChar":string,
      /**  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  */  
   "MultiCompany":boolean,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgDate":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgTime":number,
   "CtrlSegList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLBCOARow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "Description":string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  */  
   "SeparatorChar":string,
      /**  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  */  
   "MultiCompany":boolean,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   "PerBalFmt":string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   "TBBalFmt":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgDate":string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   "FmtChgTime":number,
   "CtrlSegList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  GlobalCOA  */  
   "GlobalCOA":boolean,
      /**  GlobalLock  */  
   "GlobalLock":boolean,
      /**  RebuildGLAccts  */  
   "RebuildGLAccts":boolean,
      /**  Peru CSF: SUNAT Chart of Accounts Code  */  
   "PESunatCOA":string,
   "BitFlag":number,
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

export interface Erp_Tablesets_GLBCOASegmentRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company ID of the external company this COA was imported from.  */  
   "ExtCompanyID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  System generated number from 1 through 20.  */  
   "SegmentNbr":number,
      /**  Name of Segment  */  
   "SegmentName":string,
      /**  Short name of segment.  */  
   "Abbreviation":string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   "MaxLength":number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   "MinLength":number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   "Dynamic":boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   "UseRefEntity":boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   "RefEntity":string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   "AllowAlpha":boolean,
      /**  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  */  
   "EntryControl":string,
      /**  Indicates if journal entries are automatically balanced.  */  
   "SegSelfBal":boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   "Level":number,
      /**  Indicates if this segment is included in the standard trial balance account.  */  
   "SummaryBal":boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   "DetailBal":boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  */  
   "KeepOpenBal":boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   "DisplayOrder":number,
      /**  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  */  
   "MultiCompany":boolean,
      /**  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   "AutoCreateSegVals":boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   "SelfBalAcct":string,
      /**  Balance Seg Value 1  */  
   "BalSegValue1":string,
      /**  Balance Seg Value 2  */  
   "BalSegValue2":string,
      /**  Balance Seg Value 3  */  
   "BalSegValue3":string,
      /**  Balance Seg Value 4  */  
   "BalSegValue4":string,
      /**  Balance Seg Value 5  */  
   "BalSegValue5":string,
      /**  Balance Seg Value 6  */  
   "BalSegValue6":string,
      /**  Balance Seg Value 7  */  
   "BalSegValue7":string,
      /**  Balance Seg Value 8  */  
   "BalSegValue8":string,
      /**  Balance Seg Value 9  */  
   "BalSegValue9":string,
      /**  Balance Seg Value 10  */  
   "BalSegValue10":string,
      /**  Balance Seg Value 11  */  
   "BalSegValue11":string,
      /**  Balance Seg Value 12  */  
   "BalSegValue12":string,
      /**  Balance Seg Value 13  */  
   "BalSegValue13":string,
      /**  Balance Seg Value 14  */  
   "BalSegValue14":string,
      /**  Balance Seg Value 15  */  
   "BalSegValue15":string,
      /**  Balance Seg Value 16  */  
   "BalSegValue16":string,
      /**  Balance Seg Value 17  */  
   "BalSegValue17":string,
      /**  Balance Seg Value 18  */  
   "BalSegValue18":string,
      /**  Balance Seg Value 19  */  
   "BalSegValue19":string,
      /**  Balance Seg Value 20  */  
   "BalSegValue20":string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   "SelfOffAcct":string,
      /**  Offset Segment Value 1  */  
   "OffSegValue1":string,
      /**  Offset Segment Value 2  */  
   "OffSegValue2":string,
      /**  Offset Segment Value 3  */  
   "OffSegValue3":string,
      /**  Offset Segment Value 4  */  
   "OffSegValue4":string,
      /**  Offset Segment Value 5  */  
   "OffSegValue5":string,
      /**  Offset Segment Value 6  */  
   "OffSegValue6":string,
      /**  Offset Segment Value 7  */  
   "OffSegValue7":string,
      /**  Offset Segment Value 8  */  
   "OffSegValue8":string,
      /**  Offset Segment Value 9  */  
   "OffSegValue9":string,
      /**  Offset Segment Value 10  */  
   "OffSegValue10":string,
      /**  Offset Segment Value 11  */  
   "OffSegValue11":string,
      /**  Offset Segment Value 12  */  
   "OffSegValue12":string,
      /**  Offset Segment Value 13  */  
   "OffSegValue13":string,
      /**  Offset Segment Value 14  */  
   "OffSegValue14":string,
      /**  Offset Segment Value 15  */  
   "OffSegValue15":string,
      /**  Offset Segment Value 16  */  
   "OffSegValue16":string,
      /**  Offset Segment Value 17  */  
   "OffSegValue17":string,
      /**  Offset Segment Value 18  */  
   "OffSegValue18":string,
      /**  Offset Segment Value 19  */  
   "OffSegValue19":string,
      /**  Offset Segment Value 20  */  
   "OffSegValue20":string,
   "ReverseCategoryID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CNIsCFICode  */  
   "CNIsCFICode":boolean,
      /**  SegValueField  */  
   "SegValueField":string,
      /**  DescFieldName  */  
   "DescFieldName":string,
      /**  GlobalCOASegment  */  
   "GlobalCOASegment":boolean,
      /**  GlobalCOASegmentValues  */  
   "GlobalCOASegmentValues":boolean,
      /**  GlobalLock  */  
   "GlobalLock":boolean,
      /**  GlobalValuesLock  */  
   "GlobalValuesLock":boolean,
      /**  SiteSegment  */  
   "SiteSegment":boolean,
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
   */  
export interface DeleteByID_input{
   extCompanyID:string,
   coACode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLBCOAListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The description or Name of this Chart of Accounts.  */  
   Description:string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  */  
   SeparatorChar:string,
      /**  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  */  
   MultiCompany:boolean,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgDate:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgTime:number,
   CtrlSegList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBCOAListTableset{
   GLBCOAList:Erp_Tablesets_GLBCOAListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLBCOARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  External Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The description or Name of this Chart of Accounts.  */  
   Description:string,
      /**  This is the character that is displayed between each segment of the GL Accounts.  */  
   SeparatorChar:string,
      /**  Identifieds the COA as one that is sent to the External Companies for GL processing.  If the ExtCompID is not null this field must be No.  */  
   MultiCompany:boolean,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  */  
   PerBalFmt:string,
      /**  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  */  
   TBBalFmt:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgDate:string,
      /**  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  */  
   FmtChgTime:number,
   CtrlSegList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  GlobalCOA  */  
   GlobalCOA:boolean,
      /**  GlobalLock  */  
   GlobalLock:boolean,
      /**  RebuildGLAccts  */  
   RebuildGLAccts:boolean,
      /**  Peru CSF: SUNAT Chart of Accounts Code  */  
   PESunatCOA:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_GLBCOASegmentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company ID of the external company this COA was imported from.  */  
   ExtCompanyID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  System generated number from 1 through 20.  */  
   SegmentNbr:number,
      /**  Name of Segment  */  
   SegmentName:string,
      /**  Short name of segment.  */  
   Abbreviation:string,
      /**  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  */  
   MaxLength:number,
      /**  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  */  
   MinLength:number,
      /**  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  */  
   Dynamic:boolean,
      /**  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  */  
   UseRefEntity:boolean,
      /**  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  */  
   RefEntity:string,
      /**  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  */  
   AllowAlpha:boolean,
      /**  Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegValOpt table.  */  
   EntryControl:string,
      /**  Indicates if journal entries are automatically balanced.  */  
   SegSelfBal:boolean,
      /**  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  */  
   Level:number,
      /**  Indicates if this segment is included in the standard trial balance account.  */  
   SummaryBal:boolean,
      /**  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  */  
   DetailBal:boolean,
      /**  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for pjrect accounting where you want to keep the project date balance independent of the financial year.  */  
   KeepOpenBal:boolean,
      /**  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  */  
   DisplayOrder:number,
      /**  Indicates if this segment is subject to Multi-Company GL Journal processing.  If the COA is marked as MultipCompnay then all controlled segments are flagged as multi-company and this cannot be overwritten by the user.  */  
   MultiCompany:boolean,
      /**  Indicates if segment values for segments defined as reference entities are to be created each time a newrecord is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  */  
   AutoCreateSegVals:boolean,
      /**  Account used  when creating balancing transactions for this segment.  */  
   SelfBalAcct:string,
      /**  Balance Seg Value 1  */  
   BalSegValue1:string,
      /**  Balance Seg Value 2  */  
   BalSegValue2:string,
      /**  Balance Seg Value 3  */  
   BalSegValue3:string,
      /**  Balance Seg Value 4  */  
   BalSegValue4:string,
      /**  Balance Seg Value 5  */  
   BalSegValue5:string,
      /**  Balance Seg Value 6  */  
   BalSegValue6:string,
      /**  Balance Seg Value 7  */  
   BalSegValue7:string,
      /**  Balance Seg Value 8  */  
   BalSegValue8:string,
      /**  Balance Seg Value 9  */  
   BalSegValue9:string,
      /**  Balance Seg Value 10  */  
   BalSegValue10:string,
      /**  Balance Seg Value 11  */  
   BalSegValue11:string,
      /**  Balance Seg Value 12  */  
   BalSegValue12:string,
      /**  Balance Seg Value 13  */  
   BalSegValue13:string,
      /**  Balance Seg Value 14  */  
   BalSegValue14:string,
      /**  Balance Seg Value 15  */  
   BalSegValue15:string,
      /**  Balance Seg Value 16  */  
   BalSegValue16:string,
      /**  Balance Seg Value 17  */  
   BalSegValue17:string,
      /**  Balance Seg Value 18  */  
   BalSegValue18:string,
      /**  Balance Seg Value 19  */  
   BalSegValue19:string,
      /**  Balance Seg Value 20  */  
   BalSegValue20:string,
      /**  The Self Balance offset account used when balancing this segment.  */  
   SelfOffAcct:string,
      /**  Offset Segment Value 1  */  
   OffSegValue1:string,
      /**  Offset Segment Value 2  */  
   OffSegValue2:string,
      /**  Offset Segment Value 3  */  
   OffSegValue3:string,
      /**  Offset Segment Value 4  */  
   OffSegValue4:string,
      /**  Offset Segment Value 5  */  
   OffSegValue5:string,
      /**  Offset Segment Value 6  */  
   OffSegValue6:string,
      /**  Offset Segment Value 7  */  
   OffSegValue7:string,
      /**  Offset Segment Value 8  */  
   OffSegValue8:string,
      /**  Offset Segment Value 9  */  
   OffSegValue9:string,
      /**  Offset Segment Value 10  */  
   OffSegValue10:string,
      /**  Offset Segment Value 11  */  
   OffSegValue11:string,
      /**  Offset Segment Value 12  */  
   OffSegValue12:string,
      /**  Offset Segment Value 13  */  
   OffSegValue13:string,
      /**  Offset Segment Value 14  */  
   OffSegValue14:string,
      /**  Offset Segment Value 15  */  
   OffSegValue15:string,
      /**  Offset Segment Value 16  */  
   OffSegValue16:string,
      /**  Offset Segment Value 17  */  
   OffSegValue17:string,
      /**  Offset Segment Value 18  */  
   OffSegValue18:string,
      /**  Offset Segment Value 19  */  
   OffSegValue19:string,
      /**  Offset Segment Value 20  */  
   OffSegValue20:string,
   ReverseCategoryID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CNIsCFICode  */  
   CNIsCFICode:boolean,
      /**  SegValueField  */  
   SegValueField:string,
      /**  DescFieldName  */  
   DescFieldName:string,
      /**  GlobalCOASegment  */  
   GlobalCOASegment:boolean,
      /**  GlobalCOASegmentValues  */  
   GlobalCOASegmentValues:boolean,
      /**  GlobalLock  */  
   GlobalLock:boolean,
      /**  GlobalValuesLock  */  
   GlobalValuesLock:boolean,
      /**  SiteSegment  */  
   SiteSegment:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLBCOATableset{
   GLBCOA:Erp_Tablesets_GLBCOARow[],
   GLBCOASegment:Erp_Tablesets_GLBCOASegmentRow[],
   GLBCOASegValues:Erp_Tablesets_GLBCOASegValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGLBCOATableset{
   GLBCOA:Erp_Tablesets_GLBCOARow[],
   GLBCOASegment:Erp_Tablesets_GLBCOASegmentRow[],
   GLBCOASegValues:Erp_Tablesets_GLBCOASegValuesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param extCompanyID
      @param coACode
   */  
export interface GetByID_input{
   extCompanyID:string,
   coACode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLBCOATableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLBCOATableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLBCOATableset[],
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
   returnObj:Erp_Tablesets_GLBCOAListTableset[],
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
   */  
export interface GetNewGLBCOASegValues_input{
   ds:Erp_Tablesets_GLBCOATableset[],
   extCompanyID:string,
   coACode:string,
   segmentNbr:number,
}

export interface GetNewGLBCOASegValues_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOATableset,
}
}

   /** Required : 
      @param ds
      @param extCompanyID
      @param coACode
   */  
export interface GetNewGLBCOASegment_input{
   ds:Erp_Tablesets_GLBCOATableset[],
   extCompanyID:string,
   coACode:string,
}

export interface GetNewGLBCOASegment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOATableset,
}
}

   /** Required : 
      @param ds
      @param extCompanyID
   */  
export interface GetNewGLBCOA_input{
   ds:Erp_Tablesets_GLBCOATableset[],
   extCompanyID:string,
}

export interface GetNewGLBCOA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOATableset,
}
}

   /** Required : 
      @param whereClauseGLBCOA
      @param whereClauseGLBCOASegment
      @param whereClauseGLBCOASegValues
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLBCOA:string,
   whereClauseGLBCOASegment:string,
   whereClauseGLBCOASegValues:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLBCOATableset[],
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
   ds:Erp_Tablesets_UpdExtGLBCOATableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLBCOATableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLBCOATableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLBCOATableset,
}
}

