import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.BOLSvc
// Description: Bill of Lading Entry
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get BOLs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BOLs
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadRow
   */  
export function get_BOLs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BOLs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BOLs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BOL item
   Description: Calls GetByID to retrieve the BOL item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOL
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
   */  
export function get_BOLs_Company_BOLNum(Company:string, BOLNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BOLHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BOLHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BOL for the service
   Description: Calls UpdateExt to update BOL. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BOL
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BOLs_Company_BOLNum(Company:string, BOLNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete BOL item
   Description: Call UpdateExt to delete BOL item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BOL
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BOLs_Company_BOLNum(Company:string, BOLNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get BOLDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BOLDetails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLDetailRow
   */  
export function get_BOLs_Company_BOLNum_BOLDetails(Company:string, BOLNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BOLDetail item
   Description: Calls GetByID to retrieve the BOLDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLDetail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param BOLLine Desc: BOLLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   */  
export function get_BOLs_Company_BOLNum_BOLDetails_Company_BOLNum_BOLLine(Company:string, BOLNum:string, BOLLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BOLDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BOLDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BOLHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BOLHeadAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadAttchRow
   */  
export function get_BOLs_Company_BOLNum_BOLHeadAttches(Company:string, BOLNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BOLHeadAttch item
   Description: Calls GetByID to retrieve the BOLHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLHeadAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   */  
export function get_BOLs_Company_BOLNum_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company:string, BOLNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BOLHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BOLHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BOLDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BOLDetails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLDetailRow
   */  
export function get_BOLDetails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BOLDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BOLDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BOLDetail item
   Description: Calls GetByID to retrieve the BOLDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param BOLLine Desc: BOLLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   */  
export function get_BOLDetails_Company_BOLNum_BOLLine(Company:string, BOLNum:string, BOLLine:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BOLDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BOLDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BOLDetail for the service
   Description: Calls UpdateExt to update BOLDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BOLDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param BOLLine Desc: BOLLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BOLDetails_Company_BOLNum_BOLLine(Company:string, BOLNum:string, BOLLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete BOLDetail item
   Description: Call UpdateExt to delete BOLDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BOLDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param BOLLine Desc: BOLLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BOLDetails_Company_BOLNum_BOLLine(Company:string, BOLNum:string, BOLLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
   Description: Get BOLHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BOLHeadAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadAttchRow
   */  
export function get_BOLHeadAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BOLHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BOLHeadAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BOLHeadAttch item
   Description: Calls GetByID to retrieve the BOLHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   */  
export function get_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company:string, BOLNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BOLHeadAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_BOLHeadAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BOLHeadAttch for the service
   Description: Calls UpdateExt to update BOLHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BOLHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company:string, BOLNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete BOLHeadAttch item
   Description: Call UpdateExt to delete BOLHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BOLHeadAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param BOLNum Desc: BOLNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company:string, BOLNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseBOLHead:string, whereClauseBOLHeadAttch:string, whereClauseBOLDetail:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseBOLHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBOLHead=" + whereClauseBOLHead
   }
   if(typeof whereClauseBOLHeadAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBOLHeadAttch=" + whereClauseBOLHeadAttch
   }
   if(typeof whereClauseBOLDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBOLDetail=" + whereClauseBOLDetail
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(boLNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof boLNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "boLNum=" + boLNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: .
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBOLHeadUseOTS
   Description: Method to call when changing the UseOTS field the contract header record.
Refreshes the address list and contact info
   OperationID: ChangeBOLHeadUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBOLHeadUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBOLHeadUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBOLHeadUseOTS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/ChangeBOLHeadUseOTS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipToCustID
   Description: Update BOL Header information with values from the Third Party Ship To when the Ship To is changed.
   OperationID: ChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipToCustID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/ChangeShipToCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeType
   Description: This method sets the default values when the BOLType field changes.  This should
only be possible on adds.  The field is not updateable in Update Mode.
   OperationID: ChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/ChangeType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyShipHedOTS
   Description: Purpose: To assign the ShipHed One Time Ship To info (found on the orderhed/orderrel) to the
BolHead fields.
Parameters:  none
Notes:
   OperationID: CopyShipHedOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyShipHedOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyShipHedOTS(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/CopyShipHedOTS", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBillingInfo
   Description: This method populates the address information when the BillID field changes
   OperationID: GetBillingInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBillingInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBillingInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBillingInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetBillingInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetShippingInfo
   Description: This method populates the Shipping information when the ShipID field changes
   OperationID: GetShippingInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShippingInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShippingInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShippingInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetShippingInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSlips
   Description: This method generates a list of linked or unlinked packs.  If the bolNum
field is not 0, then only the packs associated with that record will be returned.
Otherwise unlinked packs will be returned.  The records returned will be unlinked
pack lines (not the headers).
   OperationID: GetSlips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSlips_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSlips_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSlips(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetSlips", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrintBOL
   Description: This method will print out the Bill of Lading.  Gives the option of Print Preview
   OperationID: PrintBOL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintBOL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintBOL_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrintBOL(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/PrintBOL", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateLinks
   Description: If the linkFlag = yes,this method will either creates a new bill of lading linking
all of the selected packs to the new Bill of Lading created.  Or add a packing
slip to an existing Bill of Lading.  All of the packs selected for a new Slip
must have the same BOLType. When adding a pack to an exising BOL, the bolTypes
must match.
If the linkFlag = no, this method will unlink the specified pack from their
Bill of Lading.
The udpated/new Bill of Lading will be returned
   OperationID: UpdateLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLinks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateLinks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/UpdateLinks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateHeadShipTovsPackShipTo
   Description: When linking packages, validates if ShipTo from header match with ShipTo from Packs to link.
If don't match, fill a message to display to the user, continue linking if everything is OK.
When BOL is Linked and ShipTo from Header changes, validates if match with linked packages.
Fills The same mesasge, so user confirms continue or Cancel.
   OperationID: ValidateHeadShipTovsPackShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateHeadShipTovsPackShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateHeadShipTovsPackShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateHeadShipTovsPackShipTo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/ValidateHeadShipTovsPackShipTo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBOLHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBOLHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBOLHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBOLHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBOLHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetNewBOLHead", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBOLHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBOLHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBOLHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBOLHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBOLHeadAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetNewBOLHeadAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBOLDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBOLDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBOLDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBOLDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBOLDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetNewBOLDetail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BOLDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BOLHeadAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BOLHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BOLHeadRow[],
}

export interface Erp_Tablesets_BOLDetailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  */  
   "BOLNum":number,
      /**  Bill of Lading line  */  
   "BOLLine":number,
      /**  Number of Packages (boxes, skids, drums...)  */  
   "Packages":number,
      /**  Packaging Code ( "box" "skd" "drm" ...)  */  
   "PkgCode":string,
      /**  Weight Per Package.  */  
   "Weight":number,
      /**  Unit of Measure of the Weight Class that qualifies the weight.  */  
   "WeightUOM":string,
      /**  NMFC Rate  */  
   "Rate":number,
      /**  NMFC Rate Classification  */  
   "ClassRate":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PkgClassDescription":string,
   "PkgCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BOLHeadAttchRow{
   "Company":string,
   "BOLNum":number,
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

export interface Erp_Tablesets_BOLHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  */  
   "BOLNum":number,
      /**  Bill of Lading Type  */  
   "BOLType":string,
      /**  The actual ship date for the BOL. Default as system date.  */  
   "ShipDate":string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  */  
   "ShipToNum":string,
      /**  Carrier Name  */  
   "Carrier":string,
      /**  Shipper Number  */  
   "ShipperNum":string,
      /**  Pro Number  */  
   "ProNumber":string,
   "FreightCharges":string,
      /**  Collect On Delivery Amount  */  
   "CODAmount":number,
      /**  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Editor widget for project comments.  */  
   "CommentText":string,
      /**  Site Identifier for shipping origination.  */  
   "Plant":string,
      /**  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  Site Identifier.  Used for Transfer Orders.  */  
   "ToPlant":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  Full name of the contact.  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  */  
   "CounterASN":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag indicating if there are Linked Packing Slips  */  
   "LinkedSlip":boolean,
      /**  Shipping Address  */  
   "ShipAddr":string,
      /**  Billing Address  */  
   "BillAddr":string,
      /**  Billing ID either VendorID or CustID  */  
   "BillID":string,
      /**  ShipTo ID (ToPlant, ShipToNum or PurPoint)  */  
   "ShipID":string,
      /**  Billing Name (used for Searches)  */  
   "BillName":string,
      /**  BOLType Description  */  
   "TypeDesc":string,
   "CustAllowOTS":boolean,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  Country name  */  
   "OTSCountryNumDescription":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   "PurPointCountry":string,
      /**  Second address line  */  
   "PurPointAddress2":string,
      /**  State portion of the address  */  
   "PurPointState":string,
      /**  Third address line  */  
   "PurPointAddress3":string,
      /**  Purchase Point Name...can't be blank.  */  
   "PurPointName":string,
      /**  Postal Code or Zip code portion of the address  */  
   "PurPointZip":string,
      /**  First address line  */  
   "PurPointAddress1":string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   "PurPointPrimPCon":number,
      /**  City portion of the address  */  
   "PurPointCity":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "ShipToCustNumBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "ShipToCustNumCustID":string,
      /**  The full name of the customer.  */  
   "ShipToCustNumName":string,
      /**  The Plant name. Used on shipping reports.  */  
   "ToPlantName":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BOLHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  */  
   "BOLNum":number,
      /**  Bill of Lading Type  */  
   "BOLType":string,
      /**  The actual ship date for the BOL. Default as system date.  */  
   "ShipDate":string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  */  
   "ShipToNum":string,
      /**  Carrier Name  */  
   "Carrier":string,
      /**  Shipper Number  */  
   "ShipperNum":string,
      /**  Pro Number  */  
   "ProNumber":string,
   "FreightCharges":string,
      /**  Collect On Delivery Amount  */  
   "CODAmount":number,
      /**  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  */  
   "VendorNum":number,
      /**  The Vendors purchase point ID.  */  
   "PurPoint":string,
      /**  Editor widget for project comments.  */  
   "CommentText":string,
      /**  Site Identifier for shipping origination.  */  
   "Plant":string,
      /**  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  */  
   "EntryPerson":string,
      /**  Site Identifier.  Used for Transfer Orders.  */  
   "ToPlant":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   "UseOTS":boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   "OTSName":string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   "OTSAddress1":string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   "OTSAddress2":string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   "OTSAddress3":string,
      /**  City portion of the One Time Shipto  address.  */  
   "OTSCity":string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   "OTSState":string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   "OTSZIP":string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   "OTSResaleID":string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   "OTSTaxRegionCode":string,
      /**  Full name of the contact.  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  */  
   "CounterASN":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag indicating if there are Linked Packing Slips  */  
   "LinkedSlip":boolean,
      /**  Shipping Address  */  
   "ShipAddr":string,
      /**  Billing Address  */  
   "BillAddr":string,
      /**  The ID of the customer or supplier.  */  
   "BillID":string,
      /**  ShipTo ID (ToPlant, ShipToNum or PurPoint)  */  
   "ShipID":string,
      /**  Billing Name (used for Searches)  */  
   "BillName":string,
      /**  BOLType Description  */  
   "TypeDesc":string,
   "CustAllowOTS":boolean,
      /**  Billing Address Formatted  */  
   "BillAddrFormatted":string,
      /**  Shipping Address Formatted  */  
   "ShipAddrFormatted":string,
      /**  Indicates a customer referenced on the record is inactive.  */  
   "InactiveCustomer":boolean,
   "BitFlag":number,
   "CustNumName":string,
   "CustNumCustID":string,
   "CustNumBTName":string,
   "OTSCountryNumDescription":string,
   "PlantName":string,
   "PurPointAddress1":string,
   "PurPointAddress2":string,
   "PurPointCity":string,
   "PurPointCountry":string,
   "PurPointAddress3":string,
   "PurPointZip":string,
   "PurPointPrimPCon":number,
   "PurPointName":string,
   "PurPointState":string,
   "ShipToCustNumBTName":string,
   "ShipToCustNumCustID":string,
   "ShipToCustNumName":string,
   "ShipToNumInactive":boolean,
   "ShipToNumName":string,
   "ToPlantName":string,
   "VendorNumCurrencyCode":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumAddress2":string,
   "VendorNumCity":string,
   "VendorNumAddress1":string,
   "VendorNumState":string,
   "VendorNumTermsCode":string,
   "VendorNumCountry":string,
   "VendorNumAddress3":string,
   "VendorNumName":string,
   "VendorNumDefaultFOB":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface ChangeBOLHeadUseOTS_input{
   ds:Erp_Tablesets_BOLTableset[],
}

export interface ChangeBOLHeadUseOTS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param iShipToCustID
      @param ds
   */  
export interface ChangeShipToCustID_input{
      /**  Proposed Third-Party Ship To  */  
   iShipToCustID:string,
   ds:Erp_Tablesets_BOLTableset[],
}

export interface ChangeShipToCustID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeType_input{
   ds:Erp_Tablesets_BOLTableset[],
}

export interface ChangeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

export interface CopyShipHedOTS_output{
}

   /** Required : 
      @param boLNum
   */  
export interface DeleteByID_input{
   boLNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_BOLDetailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  */  
   BOLNum:number,
      /**  Bill of Lading line  */  
   BOLLine:number,
      /**  Number of Packages (boxes, skids, drums...)  */  
   Packages:number,
      /**  Packaging Code ( "box" "skd" "drm" ...)  */  
   PkgCode:string,
      /**  Weight Per Package.  */  
   Weight:number,
      /**  Unit of Measure of the Weight Class that qualifies the weight.  */  
   WeightUOM:string,
      /**  NMFC Rate  */  
   Rate:number,
      /**  NMFC Rate Classification  */  
   ClassRate:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PkgClassDescription:string,
   PkgCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BOLHeadAttchRow{
   Company:string,
   BOLNum:number,
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

export interface Erp_Tablesets_BOLHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  */  
   BOLNum:number,
      /**  Bill of Lading Type  */  
   BOLType:string,
      /**  The actual ship date for the BOL. Default as system date.  */  
   ShipDate:string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  */  
   ShipToNum:string,
      /**  Carrier Name  */  
   Carrier:string,
      /**  Shipper Number  */  
   ShipperNum:string,
      /**  Pro Number  */  
   ProNumber:string,
   FreightCharges:string,
      /**  Collect On Delivery Amount  */  
   CODAmount:number,
      /**  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Editor widget for project comments.  */  
   CommentText:string,
      /**  Site Identifier for shipping origination.  */  
   Plant:string,
      /**  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  Site Identifier.  Used for Transfer Orders.  */  
   ToPlant:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  Full name of the contact.  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  */  
   CounterASN:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag indicating if there are Linked Packing Slips  */  
   LinkedSlip:boolean,
      /**  Shipping Address  */  
   ShipAddr:string,
      /**  Billing Address  */  
   BillAddr:string,
      /**  Billing ID either VendorID or CustID  */  
   BillID:string,
      /**  ShipTo ID (ToPlant, ShipToNum or PurPoint)  */  
   ShipID:string,
      /**  Billing Name (used for Searches)  */  
   BillName:string,
      /**  BOLType Description  */  
   TypeDesc:string,
   CustAllowOTS:boolean,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  Country name  */  
   OTSCountryNumDescription:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Country. Can be blank. Printed as last line of mailing name and address.  */  
   PurPointCountry:string,
      /**  Second address line  */  
   PurPointAddress2:string,
      /**  State portion of the address  */  
   PurPointState:string,
      /**  Third address line  */  
   PurPointAddress3:string,
      /**  Purchase Point Name...can't be blank.  */  
   PurPointName:string,
      /**  Postal Code or Zip code portion of the address  */  
   PurPointZip:string,
      /**  First address line  */  
   PurPointAddress1:string,
      /**  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  */  
   PurPointPrimPCon:number,
      /**  City portion of the address  */  
   PurPointCity:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   ShipToCustNumBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   ShipToCustNumCustID:string,
      /**  The full name of the customer.  */  
   ShipToCustNumName:string,
      /**  The Plant name. Used on shipping reports.  */  
   ToPlantName:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BOLHeadListTableset{
   BOLHeadList:Erp_Tablesets_BOLHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BOLHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  */  
   BOLNum:number,
      /**  Bill of Lading Type  */  
   BOLType:string,
      /**  The actual ship date for the BOL. Default as system date.  */  
   ShipDate:string,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  */  
   ShipToNum:string,
      /**  Carrier Name  */  
   Carrier:string,
      /**  Shipper Number  */  
   ShipperNum:string,
      /**  Pro Number  */  
   ProNumber:string,
   FreightCharges:string,
      /**  Collect On Delivery Amount  */  
   CODAmount:number,
      /**  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID.  */  
   PurPoint:string,
      /**  Editor widget for project comments.  */  
   CommentText:string,
      /**  Site Identifier for shipping origination.  */  
   Plant:string,
      /**  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  */  
   EntryPerson:string,
      /**  Site Identifier.  Used for Transfer Orders.  */  
   ToPlant:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  */  
   OTSTaxRegionCode:string,
      /**  Full name of the contact.  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  */  
   CounterASN:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag indicating if there are Linked Packing Slips  */  
   LinkedSlip:boolean,
      /**  Shipping Address  */  
   ShipAddr:string,
      /**  Billing Address  */  
   BillAddr:string,
      /**  The ID of the customer or supplier.  */  
   BillID:string,
      /**  ShipTo ID (ToPlant, ShipToNum or PurPoint)  */  
   ShipID:string,
      /**  Billing Name (used for Searches)  */  
   BillName:string,
      /**  BOLType Description  */  
   TypeDesc:string,
   CustAllowOTS:boolean,
      /**  Billing Address Formatted  */  
   BillAddrFormatted:string,
      /**  Shipping Address Formatted  */  
   ShipAddrFormatted:string,
      /**  Indicates a customer referenced on the record is inactive.  */  
   InactiveCustomer:boolean,
   BitFlag:number,
   CustNumName:string,
   CustNumCustID:string,
   CustNumBTName:string,
   OTSCountryNumDescription:string,
   PlantName:string,
   PurPointAddress1:string,
   PurPointAddress2:string,
   PurPointCity:string,
   PurPointCountry:string,
   PurPointAddress3:string,
   PurPointZip:string,
   PurPointPrimPCon:number,
   PurPointName:string,
   PurPointState:string,
   ShipToCustNumBTName:string,
   ShipToCustNumCustID:string,
   ShipToCustNumName:string,
   ShipToNumInactive:boolean,
   ShipToNumName:string,
   ToPlantName:string,
   VendorNumCurrencyCode:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumAddress2:string,
   VendorNumCity:string,
   VendorNumAddress1:string,
   VendorNumState:string,
   VendorNumTermsCode:string,
   VendorNumCountry:string,
   VendorNumAddress3:string,
   VendorNumName:string,
   VendorNumDefaultFOB:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BOLSlipRow{
   BOLType:string,
      /**  BOLNum field for linked slips  */  
   ShipLog:string,
   PackNum:number,
   OrderNum:string,
   ShipDate:string,
      /**  Name from Packing Slip  */  
   Name:string,
      /**  ShipTo ID for SubContract  */  
   ShipTo:string,
      /**  Name of User who entered the packing slip  */  
   EntryName:string,
   LineNum:number,
   Class:string,
   PkgType:string,
      /**  Indicates if this is a direct transfer  */  
   Direct:boolean,
      /**  L - Linking slip, U - Unlinking slip  */  
   ActionFlag:string,
   Weight:number,
   Packages:number,
      /**  Billing ID, used in creating the linked BOL record  */  
   BillNum:string,
      /**  ShipVia Carrier description  */  
   Carrier:string,
      /**  BOL Line linked to  */  
   BOLLine:number,
   BOLNum:number,
      /**  Flag to indicate whether or not this is generated from a Masterpack to be used when updating the source tables.  */  
   MasterPackFlag:boolean,
   TempCustNum:number,
   ShipToCustNum:number,
   WeightUOM:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BOLSlipTableset{
   BOLSlip:Erp_Tablesets_BOLSlipRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BOLTableset{
   BOLHead:Erp_Tablesets_BOLHeadRow[],
   BOLHeadAttch:Erp_Tablesets_BOLHeadAttchRow[],
   BOLDetail:Erp_Tablesets_BOLDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtBOLTableset{
   BOLHead:Erp_Tablesets_BOLHeadRow[],
   BOLHeadAttch:Erp_Tablesets_BOLHeadAttchRow[],
   BOLDetail:Erp_Tablesets_BOLDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param billID
      @param ds
   */  
export interface GetBillingInfo_input{
      /**  Proposed Billing ID.  */  
   billID:string,
   ds:Erp_Tablesets_BOLTableset[],
}

export interface GetBillingInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param boLNum
   */  
export interface GetByID_input{
   boLNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_BOLTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_BOLTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_BOLTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  tableName  */  
   tableName:string,
      /**  fieldName  */  
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
   returnObj:Erp_Tablesets_BOLHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param boLNum
   */  
export interface GetNewBOLDetail_input{
   ds:Erp_Tablesets_BOLTableset[],
   boLNum:number,
}

export interface GetNewBOLDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param ds
      @param boLNum
   */  
export interface GetNewBOLHeadAttch_input{
   ds:Erp_Tablesets_BOLTableset[],
   boLNum:number,
}

export interface GetNewBOLHeadAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewBOLHead_input{
   ds:Erp_Tablesets_BOLTableset[],
}

export interface GetNewBOLHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param whereClauseBOLHead
      @param whereClauseBOLHeadAttch
      @param whereClauseBOLDetail
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseBOLHead:string,
   whereClauseBOLHeadAttch:string,
   whereClauseBOLDetail:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_BOLTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param shipID
      @param ds
   */  
export interface GetShippingInfo_input{
      /**  Proposed Shipping ID  */  
   shipID:string,
   ds:Erp_Tablesets_BOLTableset[],
}

export interface GetShippingInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param bolNum
      @param bolType
      @param updateLinkFlag
   */  
export interface GetSlips_input{
      /**  Bill of lading for which to get the linked Packs for.
            If 0, then unlinked Packs will be returned  */  
   bolNum:number,
      /**  Type of BOL record to create. If left blank, all unlinked
            packs will be returned so the UI can filter based on BOLType.  Otherwise only
            the specified BOLType records will be returned.  Can be left Blank if returning linked
            packs  */  
   bolType:string,
      /**  it's true when the method is called after Update Linked
            Packs  */  
   updateLinkFlag:boolean,
}

export interface GetSlips_output{
   returnObj:Erp_Tablesets_BOLSlipTableset[],
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
      @param bolNum
      @param printPreview
   */  
export interface PrintBOL_input{
      /**  Bill of Lading number to print  */  
   bolNum:number,
      /**  Flag indicating whether to preview the print job  */  
   printPreview:boolean,
}

export interface PrintBOL_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtBOLTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtBOLTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param linkFlag
      @param bolNum
      @param bolLine
      @param wholePack
      @param ds
   */  
export interface UpdateLinks_input{
      /**  Yes if linking to a pack, no to unlink  */  
   linkFlag:boolean,
      /**  Bill of Lading Number, 0 for creating a new BOL or if unlinking a
            pack  */  
   bolNum:number,
      /**  Bill of Lading Line, 0 for creating a new BOL  */  
   bolLine:number,
      /**  Flag indicates the whole pack (all lines) should be linked
            or if only the selected lines should be linked.  */  
   wholePack:boolean,
   ds:Erp_Tablesets_BOLSlipTableset[],
}

export interface UpdateLinks_output{
   returnObj:Erp_Tablesets_BOLHeadListTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLSlipTableset[],
   vMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_BOLTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BOLTableset[],
}
}

   /** Required : 
      @param bolNum
      @param calledFrom
      @param isLinked
      @param newShipID
      @param ds
   */  
export interface ValidateHeadShipTovsPackShipTo_input{
      /**  BOL Number  */  
   bolNum:number,
      /**  specifies if procedure is called from Linking process or Changing header ShipToID  */  
   calledFrom:string,
      /**  defines if the BOL Header is already linked or not  */  
   isLinked:boolean,
      /**  Is the ShipID to be evaluated vs ShipToID from Packs  */  
   newShipID:string,
   ds:Erp_Tablesets_BOLSlipTableset[],
}

export interface ValidateHeadShipTovsPackShipTo_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

