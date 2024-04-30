import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MXWHTaxCertificateSvc
// Description: CSF Mexico WHT Certificate BO
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/$metadata", {
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
   Description: Get MXWHTaxCertificates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertificates
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadRow
   */  
export function get_MXWHTaxCertificates(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertificates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MXWHTaxCertificates(requestBody:Erp_Tablesets_MXWHTaxCertHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates", {
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
   Summary: Calls GetByID to retrieve the MXWHTaxCertificate item
   Description: Calls GetByID to retrieve the MXWHTaxCertificate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertificate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
   */  
export function get_MXWHTaxCertificates_Company_CertificateNum(Company:string, CertificateNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXWHTaxCertHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")", {
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
         resolve(data as Erp_Tablesets_MXWHTaxCertHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MXWHTaxCertificate for the service
   Description: Calls UpdateExt to update MXWHTaxCertificate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertificate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MXWHTaxCertificates_Company_CertificateNum(Company:string, CertificateNum:string, requestBody:Erp_Tablesets_MXWHTaxCertHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")", {
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
   Summary: Call UpdateExt to delete MXWHTaxCertificate item
   Description: Call UpdateExt to delete MXWHTaxCertificate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertificate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MXWHTaxCertificates_Company_CertificateNum(Company:string, CertificateNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")", {
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
   Description: Get MXWHTaxCertDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXWHTaxCertDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertDtlRow
   */  
export function get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertDtls(Company:string, CertificateNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MXWHTaxCertDtl item
   Description: Calls GetByID to retrieve the MXWHTaxCertDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   */  
export function get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company:string, CertificateNum:string, LineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXWHTaxCertDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")", {
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
         resolve(data as Erp_Tablesets_MXWHTaxCertDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MXWHTaxCertErrors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXWHTaxCertErrors1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertErrorRow
   */  
export function get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertErrors(Company:string, CertificateNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertErrors", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MXWHTaxCertError item
   Description: Calls GetByID to retrieve the MXWHTaxCertError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertError1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param ErrorSeq Desc: ErrorSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   */  
export function get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company:string, CertificateNum:string, ErrorSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXWHTaxCertErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")", {
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
         resolve(data as Erp_Tablesets_MXWHTaxCertErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MXWHTaxCertHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXWHTaxCertHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadAttchRow
   */  
export function get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertHeadAttches(Company:string, CertificateNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item
   Description: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   */  
export function get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company:string, CertificateNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXWHTaxCertHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MXWHTaxCertHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MXWHTaxCertDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertDtlRow
   */  
export function get_MXWHTaxCertDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MXWHTaxCertDtls(requestBody:Erp_Tablesets_MXWHTaxCertDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls", {
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
   Summary: Calls GetByID to retrieve the MXWHTaxCertDtl item
   Description: Calls GetByID to retrieve the MXWHTaxCertDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   */  
export function get_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company:string, CertificateNum:string, LineNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXWHTaxCertDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")", {
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
         resolve(data as Erp_Tablesets_MXWHTaxCertDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MXWHTaxCertDtl for the service
   Description: Calls UpdateExt to update MXWHTaxCertDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company:string, CertificateNum:string, LineNum:string, requestBody:Erp_Tablesets_MXWHTaxCertDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")", {
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
   Summary: Call UpdateExt to delete MXWHTaxCertDtl item
   Description: Call UpdateExt to delete MXWHTaxCertDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company:string, CertificateNum:string, LineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")", {
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
   Description: Get MXWHTaxCertErrors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertErrors
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertErrorRow
   */  
export function get_MXWHTaxCertErrors(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertErrors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MXWHTaxCertErrors(requestBody:Erp_Tablesets_MXWHTaxCertErrorRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors", {
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
   Summary: Calls GetByID to retrieve the MXWHTaxCertError item
   Description: Calls GetByID to retrieve the MXWHTaxCertError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertError
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param ErrorSeq Desc: ErrorSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   */  
export function get_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company:string, CertificateNum:string, ErrorSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXWHTaxCertErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")", {
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
         resolve(data as Erp_Tablesets_MXWHTaxCertErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MXWHTaxCertError for the service
   Description: Calls UpdateExt to update MXWHTaxCertError. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertError
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param ErrorSeq Desc: ErrorSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company:string, CertificateNum:string, ErrorSeq:string, requestBody:Erp_Tablesets_MXWHTaxCertErrorRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")", {
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
   Summary: Call UpdateExt to delete MXWHTaxCertError item
   Description: Call UpdateExt to delete MXWHTaxCertError item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertError
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param ErrorSeq Desc: ErrorSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company:string, CertificateNum:string, ErrorSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")", {
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
   Description: Get MXWHTaxCertHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadAttchRow
   */  
export function get_MXWHTaxCertHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertHeadAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MXWHTaxCertHeadAttches(requestBody:Erp_Tablesets_MXWHTaxCertHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches", {
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
   Summary: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item
   Description: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   */  
export function get_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company:string, CertificateNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MXWHTaxCertHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_MXWHTaxCertHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MXWHTaxCertHeadAttch for the service
   Description: Calls UpdateExt to update MXWHTaxCertHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company:string, CertificateNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_MXWHTaxCertHeadAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete MXWHTaxCertHeadAttch item
   Description: Call UpdateExt to delete MXWHTaxCertHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CertificateNum Desc: CertificateNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company:string, CertificateNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseMXWHTaxCertHead:string, whereClauseMXWHTaxCertHeadAttch:string, whereClauseMXWHTaxCertDtl:string, whereClauseMXWHTaxCertError:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMXWHTaxCertHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMXWHTaxCertHead=" + whereClauseMXWHTaxCertHead
   }
   if(typeof whereClauseMXWHTaxCertHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMXWHTaxCertHeadAttch=" + whereClauseMXWHTaxCertHeadAttch
   }
   if(typeof whereClauseMXWHTaxCertDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMXWHTaxCertDtl=" + whereClauseMXWHTaxCertDtl
   }
   if(typeof whereClauseMXWHTaxCertError!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMXWHTaxCertError=" + whereClauseMXWHTaxCertError
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetRows" + params, {
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(certificateNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof certificateNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "certificateNum=" + certificateNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetList" + params, {
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
   Summary: Invoke method GenerateNewCerts
   Description: Generate New CSF Mexico WHT Certificate Header and Details in DB
   OperationID: GenerateNewCerts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateNewCerts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewCerts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateNewCerts(requestBody:GenerateNewCerts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateNewCerts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GenerateNewCerts", {
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
         resolve(data as GenerateNewCerts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateNewCertsForSuppliers
   Description: Generate New CSF Mexico WHT Certificate Header and Details in DB
   OperationID: GenerateNewCertsForSuppliers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateNewCertsForSuppliers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewCertsForSuppliers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateNewCertsForSuppliers(requestBody:GenerateNewCertsForSuppliers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateNewCertsForSuppliers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GenerateNewCertsForSuppliers", {
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
         resolve(data as GenerateNewCertsForSuppliers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MXWHTaxCertGetNewFilterSearch
   Description: Return Get New Certificates Search Screen Values
   OperationID: MXWHTaxCertGetNewFilterSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MXWHTaxCertGetNewFilterSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MXWHTaxCertGetNewFilterSearch(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MXWHTaxCertGetNewFilterSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertGetNewFilterSearch", {
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
         resolve(data as MXWHTaxCertGetNewFilterSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateMXWHTaxCertificate
   Description: Creates MXWHTaxCertificate, stores it to the URL retrieved from docType.BaseURL, add it as attachment.
   OperationID: GenerateMXWHTaxCertificate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateMXWHTaxCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateMXWHTaxCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateMXWHTaxCertificate(requestBody:GenerateMXWHTaxCertificate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateMXWHTaxCertificate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GenerateMXWHTaxCertificate", {
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
         resolve(data as GenerateMXWHTaxCertificate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMXWHTaxCertificate
   Description: Validate MXWHTaxCertificate before generating XML. If some errors found then return error message
   OperationID: ValidateMXWHTaxCertificate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMXWHTaxCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMXWHTaxCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMXWHTaxCertificate(requestBody:ValidateMXWHTaxCertificate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMXWHTaxCertificate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/ValidateMXWHTaxCertificate", {
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
         resolve(data as ValidateMXWHTaxCertificate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMXWHTaxCertificatesList
   Description: Validate MXWHTaxCertificates List before generating XML. If some errors found then return error message
   OperationID: ValidateMXWHTaxCertificatesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMXWHTaxCertificatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMXWHTaxCertificatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMXWHTaxCertificatesList(requestBody:ValidateMXWHTaxCertificatesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMXWHTaxCertificatesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/ValidateMXWHTaxCertificatesList", {
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
         resolve(data as ValidateMXWHTaxCertificatesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMXWHTaxCertificates
   Description: Validate MXWHTaxCertificates List before generating XML. If some errors found then return error message
   OperationID: ValidateMXWHTaxCertificates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMXWHTaxCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMXWHTaxCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMXWHTaxCertificates(requestBody:ValidateMXWHTaxCertificates_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMXWHTaxCertificates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/ValidateMXWHTaxCertificates", {
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
         resolve(data as ValidateMXWHTaxCertificates_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateMXWHTaxCertificates
   Description: Creates MXWHTaxCertificate, stores it to the URL retrieved from docType.BaseURL, add it as attachment for all certificates numbers in the list.
   OperationID: GenerateMXWHTaxCertificates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateMXWHTaxCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateMXWHTaxCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateMXWHTaxCertificates(requestBody:GenerateMXWHTaxCertificates_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateMXWHTaxCertificates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GenerateMXWHTaxCertificates", {
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
         resolve(data as GenerateMXWHTaxCertificates_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VoidLegalNumber
   Description: Void Legal Number
   OperationID: VoidLegalNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumber(requestBody:VoidLegalNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VoidLegalNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/VoidLegalNumber", {
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
         resolve(data as VoidLegalNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistWHTaxCert
   Description: Validate is WHTaxCertificate already existed
   OperationID: ExistWHTaxCert
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistWHTaxCert_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistWHTaxCert_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistWHTaxCert(requestBody:ExistWHTaxCert_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistWHTaxCert_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/ExistWHTaxCert", {
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
         resolve(data as ExistWHTaxCert_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistWHTaxCert2
   Description: Validate is WHTaxCertificate already existed
   OperationID: ExistWHTaxCert2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistWHTaxCert2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistWHTaxCert2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistWHTaxCert2(requestBody:ExistWHTaxCert2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistWHTaxCert2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/ExistWHTaxCert2", {
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
         resolve(data as ExistWHTaxCert2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRelatedCertificateNum
   Description: RelatedCertificateNum is changing
   OperationID: OnChangingRelatedCertificateNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRelatedCertificateNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRelatedCertificateNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRelatedCertificateNum(requestBody:OnChangingRelatedCertificateNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRelatedCertificateNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/OnChangingRelatedCertificateNum", {
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
         resolve(data as OnChangingRelatedCertificateNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockSuspendedCertificate
   Description: Revert PACProcessing certificate to XMLGenerated
   OperationID: UnlockSuspendedCertificate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlockSuspendedCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockSuspendedCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockSuspendedCertificate(requestBody:UnlockSuspendedCertificate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlockSuspendedCertificate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/UnlockSuspendedCertificate", {
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
         resolve(data as UnlockSuspendedCertificate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCertificatesByCertNumList
   Description: Returns list of Certificates according to given delimited list of cert numbers
   OperationID: GetCertificatesByCertNumList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCertificatesByCertNumList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCertificatesByCertNumList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCertificatesByCertNumList(requestBody:GetCertificatesByCertNumList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCertificatesByCertNumList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetCertificatesByCertNumList", {
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
         resolve(data as GetCertificatesByCertNumList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMXWHTaxCertHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMXWHTaxCertHead(requestBody:GetNewMXWHTaxCertHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMXWHTaxCertHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetNewMXWHTaxCertHead", {
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
         resolve(data as GetNewMXWHTaxCertHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMXWHTaxCertHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertHeadAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMXWHTaxCertHeadAttch(requestBody:GetNewMXWHTaxCertHeadAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMXWHTaxCertHeadAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetNewMXWHTaxCertHeadAttch", {
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
         resolve(data as GetNewMXWHTaxCertHeadAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMXWHTaxCertDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMXWHTaxCertDtl(requestBody:GetNewMXWHTaxCertDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMXWHTaxCertDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetNewMXWHTaxCertDtl", {
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
         resolve(data as GetNewMXWHTaxCertDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMXWHTaxCertError
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertError
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertError_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertError_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMXWHTaxCertError(requestBody:GetNewMXWHTaxCertError_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMXWHTaxCertError_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetNewMXWHTaxCertError", {
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
         resolve(data as GetNewMXWHTaxCertError_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MXWHTaxCertDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertErrorRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MXWHTaxCertErrorRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MXWHTaxCertHeadAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MXWHTaxCertHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MXWHTaxCertHeadRow,
}

export interface Erp_Tablesets_MXWHTaxCertDtlRow{
      /**  Company  */  
   "Company":string,
      /**  CSF Mexico Withholding Certificate Number  */  
   "CertificateNum":number,
      /**  CSF Mexico Line Number  */  
   "LineNum":number,
      /**  TranNum  */  
   "TranNum":number,
      /**  Transaction Date  */  
   "TranDate":string,
      /**  CSF Mexico Payment Type  */  
   "PayType":string,
      /**  TaxType  */  
   "TaxType":string,
      /**  TaxCode  */  
   "TaxCode":string,
      /**  TaxableAmt  */  
   "TaxableAmt":number,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  CSF Mexico Exempt Amountt  */  
   "ExemptAmt":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  CSF Mexico Total Amount  */  
   "TotalAmt":number,
   "BitFlag":number,
   "TaxTranAPInvoiceNum":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MXWHTaxCertErrorRow{
      /**  Company  */  
   "Company":string,
      /**  CertificateNum  */  
   "CertificateNum":number,
      /**  ErrorSeq  */  
   "ErrorSeq":number,
      /**  ErrorMessage  */  
   "ErrorMessage":string,
      /**  StackTrace  */  
   "StackTrace":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MXWHTaxCertHeadAttchRow{
   "Company":string,
   "CertificateNum":number,
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

export interface Erp_Tablesets_MXWHTaxCertHeadListRow{
      /**  Company  */  
   "Company":string,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalPeriodStart  */  
   "FiscalPeriodStart":number,
      /**  FiscalPeriodEnd  */  
   "FiscalPeriodEnd":number,
      /**  Supplier Number  */  
   "SupplierNum":number,
      /**  CSF Mexico Retention Code  */  
   "RetentionCode":string,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MXWHTaxCertHeadRow{
      /**  Company  */  
   "Company":string,
      /**  CSF Mexico Withholding Certificate Number  */  
   "CertificateNum":number,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalPeriodStart  */  
   "FiscalPeriodStart":number,
      /**  FiscalPeriodEnd  */  
   "FiscalPeriodEnd":number,
      /**  Supplier Number  */  
   "SupplierNum":number,
      /**  CSF Mexico Retention Code  */  
   "RetentionCode":string,
      /**  CSF Mexico. If the checkbox is checked, then foreign vendor supplement would be printed; If the checkbox is not checked, then foreign vendor supplement would not be printed.  */  
   "IsForeignSupplement":boolean,
      /**   CSF Mexico. This field defines the value of EsBenefEfectDelCobro node and additionally if the NoBeneficiario element or the Beneficiario element is the one that prints.

If checkbox is checked (EsBenefEfectDelCobro equals SI), then the legal representative information would be included in the xml (Beneficiario nodes)

If checkbox is not checked (EsBenefEfectDelCobro equals NO), then the NoBeneficiario nodes would be the ones to be included.  */  
   "IsSeparateLegalRep":boolean,
      /**  SupplierTaxID  */  
   "SupplierTaxID":string,
      /**  Supplier Legal Name  */  
   "SupplierLegalName":string,
      /**  TranDocTypeID  */  
   "TranDocTypeID":string,
      /**  LegalNumber  */  
   "LegalNumber":string,
      /**  CSF Mexico Issue Date  */  
   "IssueDate":string,
      /**  CSF Mexico Status  */  
   "Status":string,
      /**  TaxableAmt  */  
   "TaxableAmt":number,
      /**  TaxAmt  */  
   "TaxAmt":number,
      /**  CSF Mexico Exempt Amount  */  
   "ExemptAmt":number,
      /**  CSF Mexico Total Amountt  */  
   "TotalAmt":number,
      /**  CSF Mexico Retention Description  */  
   "RetentionDescr":string,
      /**  CSF Mexico Serie  */  
   "Serie":string,
      /**  CSF Mexico Folio  */  
   "Folio":string,
      /**  CSF Mexico Certified Timestamp  */  
   "CertifiedTimestamp":string,
      /**  CSF Mexico Digital Certificate Serial Number  */  
   "CertificateSN":string,
      /**  CSF Mexico Digital Certificate  */  
   "Certificate":string,
      /**  CSF Mexico Fiscal Folio  */  
   "FiscalFolio":string,
      /**  CSF Mexico SAT Certificate Serial Number  */  
   "SATCertificateSN":string,
      /**  CSF Mexico Digital Seal  */  
   "DigitalSeal":string,
      /**  CSF Mexico SAT Digital Seal  */  
   "SATSeal":string,
      /**  CSF Mexico Original String  */  
   "OriginalString":string,
      /**  CSF Mexico Original String TFD  */  
   "OriginalStringTFD":string,
      /**  CSF Mexico Cancellation ID  */  
   "CancellationID":string,
      /**  CSF Mexico Cancellation Status  */  
   "CancellationStatus":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RelatedCertificateNum  */  
   "RelatedCertificateNum":number,
      /**  RelationType  */  
   "RelationType":string,
      /**  Supplier ID  */  
   "SupplierID":string,
      /**  Text of all error messages related to current certificate from MXWHTaxCertError table  */  
   "Errors":string,
      /**  CSF Mexico Status Description  */  
   "StatusDescription":string,
   "BitFlag":number,
   "RetentionCodeLongDesc":string,
   "VendorCurrencyCode":string,
   "VendorTermsCode":string,
   "VendorVendorID":string,
   "VendorZIP":string,
   "VendorName":string,
   "VendorAddress3":string,
   "VendorDefaultFOB":string,
   "VendorState":string,
   "VendorCountry":string,
   "VendorAddress2":string,
   "VendorAddress1":string,
   "VendorCity":string,
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
      @param certificateNum
   */  
export interface DeleteByID_input{
   certificateNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MXWHTaxCertDtlRow{
      /**  Company  */  
   Company:string,
      /**  CSF Mexico Withholding Certificate Number  */  
   CertificateNum:number,
      /**  CSF Mexico Line Number  */  
   LineNum:number,
      /**  TranNum  */  
   TranNum:number,
      /**  Transaction Date  */  
   TranDate:string,
      /**  CSF Mexico Payment Type  */  
   PayType:string,
      /**  TaxType  */  
   TaxType:string,
      /**  TaxCode  */  
   TaxCode:string,
      /**  TaxableAmt  */  
   TaxableAmt:number,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  CSF Mexico Exempt Amountt  */  
   ExemptAmt:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  CSF Mexico Total Amount  */  
   TotalAmt:number,
   BitFlag:number,
   TaxTranAPInvoiceNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MXWHTaxCertErrorRow{
      /**  Company  */  
   Company:string,
      /**  CertificateNum  */  
   CertificateNum:number,
      /**  ErrorSeq  */  
   ErrorSeq:number,
      /**  ErrorMessage  */  
   ErrorMessage:string,
      /**  StackTrace  */  
   StackTrace:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MXWHTaxCertGetNewFilterRow{
      /**  EndingFiscalPeriod  */  
   EndingFiscalPeriod:number,
      /**  Fiscal Year  */  
   FiscalYear:number,
   FiscalYearSuffix:string,
      /**  StartingFiscalPeriod  */  
   StartingFiscalPeriod:number,
      /**  SupplierLabel  */  
   SupplierLabel:string,
      /**  Suppliers  */  
   Suppliers:string,
      /**  SuppliersSelected  */  
   SuppliersSelected:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MXWHTaxCertGetNewTableset{
   MXWHTaxCertGetNewFilter:Erp_Tablesets_MXWHTaxCertGetNewFilterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MXWHTaxCertHeadAttchRow{
   Company:string,
   CertificateNum:number,
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

export interface Erp_Tablesets_MXWHTaxCertHeadListRow{
      /**  Company  */  
   Company:string,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalPeriodStart  */  
   FiscalPeriodStart:number,
      /**  FiscalPeriodEnd  */  
   FiscalPeriodEnd:number,
      /**  Supplier Number  */  
   SupplierNum:number,
      /**  CSF Mexico Retention Code  */  
   RetentionCode:string,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MXWHTaxCertHeadListTableset{
   MXWHTaxCertHeadList:Erp_Tablesets_MXWHTaxCertHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MXWHTaxCertHeadRow{
      /**  Company  */  
   Company:string,
      /**  CSF Mexico Withholding Certificate Number  */  
   CertificateNum:number,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalPeriodStart  */  
   FiscalPeriodStart:number,
      /**  FiscalPeriodEnd  */  
   FiscalPeriodEnd:number,
      /**  Supplier Number  */  
   SupplierNum:number,
      /**  CSF Mexico Retention Code  */  
   RetentionCode:string,
      /**  CSF Mexico. If the checkbox is checked, then foreign vendor supplement would be printed; If the checkbox is not checked, then foreign vendor supplement would not be printed.  */  
   IsForeignSupplement:boolean,
      /**   CSF Mexico. This field defines the value of EsBenefEfectDelCobro node and additionally if the NoBeneficiario element or the Beneficiario element is the one that prints.

If checkbox is checked (EsBenefEfectDelCobro equals SI), then the legal representative information would be included in the xml (Beneficiario nodes)

If checkbox is not checked (EsBenefEfectDelCobro equals NO), then the NoBeneficiario nodes would be the ones to be included.  */  
   IsSeparateLegalRep:boolean,
      /**  SupplierTaxID  */  
   SupplierTaxID:string,
      /**  Supplier Legal Name  */  
   SupplierLegalName:string,
      /**  TranDocTypeID  */  
   TranDocTypeID:string,
      /**  LegalNumber  */  
   LegalNumber:string,
      /**  CSF Mexico Issue Date  */  
   IssueDate:string,
      /**  CSF Mexico Status  */  
   Status:string,
      /**  TaxableAmt  */  
   TaxableAmt:number,
      /**  TaxAmt  */  
   TaxAmt:number,
      /**  CSF Mexico Exempt Amount  */  
   ExemptAmt:number,
      /**  CSF Mexico Total Amountt  */  
   TotalAmt:number,
      /**  CSF Mexico Retention Description  */  
   RetentionDescr:string,
      /**  CSF Mexico Serie  */  
   Serie:string,
      /**  CSF Mexico Folio  */  
   Folio:string,
      /**  CSF Mexico Certified Timestamp  */  
   CertifiedTimestamp:string,
      /**  CSF Mexico Digital Certificate Serial Number  */  
   CertificateSN:string,
      /**  CSF Mexico Digital Certificate  */  
   Certificate:string,
      /**  CSF Mexico Fiscal Folio  */  
   FiscalFolio:string,
      /**  CSF Mexico SAT Certificate Serial Number  */  
   SATCertificateSN:string,
      /**  CSF Mexico Digital Seal  */  
   DigitalSeal:string,
      /**  CSF Mexico SAT Digital Seal  */  
   SATSeal:string,
      /**  CSF Mexico Original String  */  
   OriginalString:string,
      /**  CSF Mexico Original String TFD  */  
   OriginalStringTFD:string,
      /**  CSF Mexico Cancellation ID  */  
   CancellationID:string,
      /**  CSF Mexico Cancellation Status  */  
   CancellationStatus:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RelatedCertificateNum  */  
   RelatedCertificateNum:number,
      /**  RelationType  */  
   RelationType:string,
      /**  Supplier ID  */  
   SupplierID:string,
      /**  Text of all error messages related to current certificate from MXWHTaxCertError table  */  
   Errors:string,
      /**  CSF Mexico Status Description  */  
   StatusDescription:string,
   BitFlag:number,
   RetentionCodeLongDesc:string,
   VendorCurrencyCode:string,
   VendorTermsCode:string,
   VendorVendorID:string,
   VendorZIP:string,
   VendorName:string,
   VendorAddress3:string,
   VendorDefaultFOB:string,
   VendorState:string,
   VendorCountry:string,
   VendorAddress2:string,
   VendorAddress1:string,
   VendorCity:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MXWHTaxCertificateTableset{
   MXWHTaxCertHead:Erp_Tablesets_MXWHTaxCertHeadRow[],
   MXWHTaxCertHeadAttch:Erp_Tablesets_MXWHTaxCertHeadAttchRow[],
   MXWHTaxCertDtl:Erp_Tablesets_MXWHTaxCertDtlRow[],
   MXWHTaxCertError:Erp_Tablesets_MXWHTaxCertErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtMXWHTaxCertificateTableset{
   MXWHTaxCertHead:Erp_Tablesets_MXWHTaxCertHeadRow[],
   MXWHTaxCertHeadAttch:Erp_Tablesets_MXWHTaxCertHeadAttchRow[],
   MXWHTaxCertDtl:Erp_Tablesets_MXWHTaxCertDtlRow[],
   MXWHTaxCertError:Erp_Tablesets_MXWHTaxCertErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param certificateNum
      @param isRelated
   */  
export interface ExistWHTaxCert2_input{
      /**  certificateNum  */  
   certificateNum:number,
      /**  Is Certificate related or not  */  
   isRelated:boolean,
}

export interface ExistWHTaxCert2_output{
   returnObj:string,
}

   /** Required : 
      @param certificateNum
   */  
export interface ExistWHTaxCert_input{
      /**  certificateNum  */  
   certificateNum:number,
}

export interface ExistWHTaxCert_output{
   returnObj:string,
}

   /** Required : 
      @param certificateNum
   */  
export interface GenerateMXWHTaxCertificate_input{
      /**  Certificate number  */  
   certificateNum:number,
}

export interface GenerateMXWHTaxCertificate_output{
}

   /** Required : 
      @param certificateNumsList
   */  
export interface GenerateMXWHTaxCertificates_input{
      /**  List of the Certificates numbers  */  
   certificateNumsList:string,
}

export interface GenerateMXWHTaxCertificates_output{
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param fiscalYear
      @param fiscalYearSuffix
      @param startFiscalPeriod
      @param endFiscalPeriod
      @param suppliersList
      @param warningText
   */  
export interface GenerateNewCertsForSuppliers_input{
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
      /**  Starting Fiscal Period  */  
   startFiscalPeriod:number,
      /**  Ending Fiscal Period  */  
   endFiscalPeriod:number,
      /**  List of Suppliers  */  
   suppliersList:string,
      /**  ref Warnings. Example: There are existing certificates for the same period, supplier, retencionCode  */  
   warningText:string,
}

export interface GenerateNewCertsForSuppliers_output{
parameters : {
      /**  output parameters  */  
   warningText:string,
}
}

   /** Required : 
      @param fiscalYear
      @param fiscalYearSuffix
      @param startFiscalPeriod
      @param endFiscalPeriod
      @param warningText
   */  
export interface GenerateNewCerts_input{
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
      /**  Starting Fiscal Period  */  
   startFiscalPeriod:number,
      /**  Ending Fiscal Period  */  
   endFiscalPeriod:number,
      /**  ref Warnings. Example: There are existing certificates for the same period, supplier, retencionCode  */  
   warningText:string,
}

export interface GenerateNewCerts_output{
parameters : {
      /**  output parameters  */  
   warningText:string,
}
}

   /** Required : 
      @param certificateNum
   */  
export interface GetByID_input{
   certificateNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MXWHTaxCertificateTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MXWHTaxCertificateTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MXWHTaxCertificateTableset[],
}

   /** Required : 
      @param certNumList
   */  
export interface GetCertificatesByCertNumList_input{
      /**  Delimited list of certificates numbers  */  
   certNumList:string,
}

export interface GetCertificatesByCertNumList_output{
   returnObj:Erp_Tablesets_MXWHTaxCertificateTableset[],
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
   returnObj:Erp_Tablesets_MXWHTaxCertHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param certificateNum
   */  
export interface GetNewMXWHTaxCertDtl_input{
   ds:Erp_Tablesets_MXWHTaxCertificateTableset[],
   certificateNum:number,
}

export interface GetNewMXWHTaxCertDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MXWHTaxCertificateTableset,
}
}

   /** Required : 
      @param ds
      @param certificateNum
   */  
export interface GetNewMXWHTaxCertError_input{
   ds:Erp_Tablesets_MXWHTaxCertificateTableset[],
   certificateNum:number,
}

export interface GetNewMXWHTaxCertError_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MXWHTaxCertificateTableset,
}
}

   /** Required : 
      @param ds
      @param certificateNum
   */  
export interface GetNewMXWHTaxCertHeadAttch_input{
   ds:Erp_Tablesets_MXWHTaxCertificateTableset[],
   certificateNum:number,
}

export interface GetNewMXWHTaxCertHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MXWHTaxCertificateTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMXWHTaxCertHead_input{
   ds:Erp_Tablesets_MXWHTaxCertificateTableset[],
}

export interface GetNewMXWHTaxCertHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MXWHTaxCertificateTableset,
}
}

   /** Required : 
      @param whereClauseMXWHTaxCertHead
      @param whereClauseMXWHTaxCertHeadAttch
      @param whereClauseMXWHTaxCertDtl
      @param whereClauseMXWHTaxCertError
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMXWHTaxCertHead:string,
   whereClauseMXWHTaxCertHeadAttch:string,
   whereClauseMXWHTaxCertDtl:string,
   whereClauseMXWHTaxCertError:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MXWHTaxCertificateTableset[],
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

export interface MXWHTaxCertGetNewFilterSearch_output{
   returnObj:Erp_Tablesets_MXWHTaxCertGetNewTableset[],
}

   /** Required : 
      @param strCertificateNum
   */  
export interface OnChangingRelatedCertificateNum_input{
   strCertificateNum:string,
}

export interface OnChangingRelatedCertificateNum_output{
}

   /** Required : 
      @param certNum
   */  
export interface UnlockSuspendedCertificate_input{
      /**  Certificate Number  */  
   certNum:number,
}

export interface UnlockSuspendedCertificate_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMXWHTaxCertificateTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMXWHTaxCertificateTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MXWHTaxCertificateTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MXWHTaxCertificateTableset,
}
}

   /** Required : 
      @param certificateNum
   */  
export interface ValidateMXWHTaxCertificate_input{
      /**  Certificate Number  */  
   certificateNum:number,
}

export interface ValidateMXWHTaxCertificate_output{
   returnObj:string,
}

   /** Required : 
      @param certificateNumsList
   */  
export interface ValidateMXWHTaxCertificatesList_input{
      /**  Certificates Numbers List  */  
   certificateNumsList:string,
}

export interface ValidateMXWHTaxCertificatesList_output{
   returnObj:string,
}

   /** Required : 
      @param certificateNumsList
   */  
export interface ValidateMXWHTaxCertificates_input{
      /**  Certificates Numbers List  */  
   certificateNumsList:number,
}

export interface ValidateMXWHTaxCertificates_output{
   returnObj:string,
}

   /** Required : 
      @param ipCertificateNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  certificateNum  */  
   ipCertificateNum:number,
      /**  reason  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_MXWHTaxCertificateTableset[],
}

