import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PRW2DtlSvc
// Description: Payroll W2 detail file.  Each record in this file represents one W2.
IMPORTANT NOTE: THE REPORT NAME FOR W2EXPORT SHOULD BE 'W2REPORT'.
IT IS A IRS REQUIREMENT.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/$metadata", {
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
   Description: Get PRW2Dtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRW2Dtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlRow
   */  
export function get_PRW2Dtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRW2Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRW2Dtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls", {
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
   Summary: Calls GetByID to retrieve the PRW2Dtl item
   Description: Calls GetByID to retrieve the PRW2Dtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRW2Dtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
   */  
export function get_PRW2Dtls_Company_TaxYear_ControlNum(Company:string, TaxYear:string, ControlNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRW2DtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRW2DtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRW2Dtl for the service
   Description: Calls UpdateExt to update PRW2Dtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRW2Dtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRW2DtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRW2Dtls_Company_TaxYear_ControlNum(Company:string, TaxYear:string, ControlNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")", {
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
   Summary: Call UpdateExt to delete PRW2Dtl item
   Description: Call UpdateExt to delete PRW2Dtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRW2Dtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRW2Dtls_Company_TaxYear_ControlNum(Company:string, TaxYear:string, ControlNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")", {
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
   Description: Get PRW2DtlBoxs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRW2DtlBoxs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlBoxRow
   */  
export function get_PRW2Dtls_Company_TaxYear_ControlNum_PRW2DtlBoxs(Company:string, TaxYear:string, ControlNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")/PRW2DtlBoxs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRW2DtlBox item
   Description: Calls GetByID to retrieve the PRW2DtlBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRW2DtlBox1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      @param BoxType Desc: BoxType   Required: True   Allow empty value : True
      @param BoxSeq Desc: BoxSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   */  
export function get_PRW2Dtls_Company_TaxYear_ControlNum_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company:string, TaxYear:string, ControlNum:string, BoxType:string, BoxSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRW2DtlBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2Dtls(" + Company + "," + TaxYear + "," + ControlNum + ")/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRW2DtlBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PRW2DtlBoxs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRW2DtlBoxs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlBoxRow
   */  
export function get_PRW2DtlBoxs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRW2DtlBoxs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRW2DtlBoxs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs", {
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
   Summary: Calls GetByID to retrieve the PRW2DtlBox item
   Description: Calls GetByID to retrieve the PRW2DtlBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRW2DtlBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      @param BoxType Desc: BoxType   Required: True   Allow empty value : True
      @param BoxSeq Desc: BoxSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   */  
export function get_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company:string, TaxYear:string, ControlNum:string, BoxType:string, BoxSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRW2DtlBoxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PRW2DtlBoxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRW2DtlBox for the service
   Description: Calls UpdateExt to update PRW2DtlBox. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRW2DtlBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      @param BoxType Desc: BoxType   Required: True   Allow empty value : True
      @param BoxSeq Desc: BoxSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRW2DtlBoxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company:string, TaxYear:string, ControlNum:string, BoxType:string, BoxSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")", {
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
   Summary: Call UpdateExt to delete PRW2DtlBox item
   Description: Call UpdateExt to delete PRW2DtlBox item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRW2DtlBox
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TaxYear Desc: TaxYear   Required: True
      @param ControlNum Desc: ControlNum   Required: True
      @param BoxType Desc: BoxType   Required: True   Allow empty value : True
      @param BoxSeq Desc: BoxSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRW2DtlBoxs_Company_TaxYear_ControlNum_BoxType_BoxSeq(Company:string, TaxYear:string, ControlNum:string, BoxType:string, BoxSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/PRW2DtlBoxs(" + Company + "," + TaxYear + "," + ControlNum + "," + BoxType + "," + BoxSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRW2DtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePRW2Dtl:string, whereClausePRW2DtlBox:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePRW2Dtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRW2Dtl=" + whereClausePRW2Dtl
   }
   if(typeof whereClausePRW2DtlBox!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRW2DtlBox=" + whereClausePRW2DtlBox
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(taxYear:string, controlNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof taxYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "taxYear=" + taxYear
   }
   if(typeof controlNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "controlNum=" + controlNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetList" + params, {
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
   Summary: Invoke method CheckPRW2DtlExists
   Description: Checks if a W2 form exists for the year.
   OperationID: CheckPRW2DtlExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRW2DtlExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRW2DtlExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPRW2DtlExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/CheckPRW2DtlExists", {
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
   Summary: Invoke method CheckPRChecksExist
   Description: Checks if there are posted payroll checks for the entered year
   OperationID: CheckPRChecksExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPRChecksExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPRChecksExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPRChecksExist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/CheckPRChecksExist", {
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
   Summary: Invoke method ValidateUser
   Description: Validate if the user has the rights to proceed.
   OperationID: ValidateUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateUser(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/ValidateUser", {
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
   Summary: Invoke method DeletePRW2Dtls
   Description: This procedure deletes the PRW2Dtl records from the database.
   OperationID: DeletePRW2Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePRW2Dtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePRW2Dtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeletePRW2Dtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/DeletePRW2Dtls", {
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
   Summary: Invoke method ExportPRW2Dtls
   Description: This procedure takes the pin code number and tax year as input parameters
and returns the PRW2DtlExportDataSet.  The UI person has to read the records
in the data set and export it in the LineNum order.  It is very important
that the export order be in the line number ascending order.
   OperationID: ExportPRW2Dtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportPRW2Dtls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportPRW2Dtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportPRW2Dtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/ExportPRW2Dtls", {
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
   Summary: Invoke method ExportPRW2DtlsFile
   OperationID: ExportPRW2DtlsFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportPRW2DtlsFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportPRW2DtlsFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportPRW2DtlsFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/ExportPRW2DtlsFile", {
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
   Summary: Invoke method DeleteFile
   Description: Deletes file from UserData storage
   OperationID: DeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/DeleteFile", {
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
   Summary: Invoke method GetAvailableControlNums
   Description: Returns the available controlnums for an employee on w2 file
takes taxyear and empid as input parameters
   OperationID: GetAvailableControlNums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableControlNums_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableControlNums_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableControlNums(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetAvailableControlNums", {
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
   Summary: Invoke method GetEmployeeAddress
   Description: Gets Employee Adress
   OperationID: GetEmployeeAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEmployeeAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmployeeAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmployeeAddress(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetEmployeeAddress", {
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
   Summary: Invoke method GetEmployerAddress
   Description: Gets Employer Adress
   OperationID: GetEmployerAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmployerAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmployerAddress(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetEmployerAddress", {
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
   Summary: Invoke method GetEmployerEIN
   Description: Gets Employer FIN
   OperationID: GetEmployerEIN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEmployerEIN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEmployerEIN(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetEmployerEIN", {
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
   Summary: Invoke method LeaveTaxYear
   Description: This procedrue must be called on leave of TaxYear field.
   OperationID: LeaveTaxYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveTaxYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveTaxYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LeaveTaxYear(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/LeaveTaxYear", {
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
   Summary: Invoke method GetNewPRW2Dtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRW2Dtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRW2Dtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRW2Dtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRW2Dtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetNewPRW2Dtl", {
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
   Summary: Invoke method GetNewPRW2DtlBox
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRW2DtlBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRW2DtlBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRW2DtlBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRW2DtlBox(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetNewPRW2DtlBox", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PRW2DtlSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlBoxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRW2DtlBoxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRW2DtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRW2DtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRW2DtlRow[],
}

export interface Erp_Tablesets_PRW2DtlBoxRow{
      /**  Company  */  
   "Company":string,
      /**  TaxYear  */  
   "TaxYear":number,
      /**  ControlNum  */  
   "ControlNum":number,
      /**  BoxType  */  
   "BoxType":string,
      /**  BoxSeq  */  
   "BoxSeq":number,
      /**  BoxCode  */  
   "BoxCode":string,
      /**  BoxAmount  */  
   "BoxAmount":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRW2DtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Identifies the tax year of this W2 record. Used as a component in the primary index.  */  
   "TaxYear":number,
      /**  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  */  
   "ControlNum":number,
      /**  Encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  */  
   "VoidW2":boolean,
      /**  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  */  
   "FitWages":number,
      /**  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  */  
   "FitTax":number,
      /**  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  */  
   "SSWages":number,
      /**  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  */  
   "SSTax":number,
      /**  Social Security Tips  */  
   "SSTips":number,
      /**  Allocation Tips  */  
   "AllocTips":number,
      /**  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  */  
   "MediWages":number,
      /**  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  */  
   "MediTax":number,
      /**  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  */  
   "AdvanceEIC":number,
      /**  Dependent care benefits. Not generated by system.  */  
   "DependCare":number,
      /**  amount of Nonqualified plans. Not generated by system.  */  
   "NQPlan":number,
      /**  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  */  
   "FringeBenefits":number,
      /**  Statutory Employee  */  
   "Statutory":boolean,
      /**  Deceased  */  
   "Deceased":boolean,
      /**  Pension Plan  */  
   "Pension":boolean,
      /**  Legal Representation  */  
   "LegalRep":boolean,
      /**  New field added for 5.2.  Indicates a reirement plan.  */  
   "RetirePlan":boolean,
      /**  Household Employee  */  
   "HouseHold":boolean,
      /**  Indicates if there is third part sick pay.  */  
   "ThirdPartySickPay":boolean,
      /**  Deferred Compensation  */  
   "DeferredComp":boolean,
      /**  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   "State1TaxTblID":string,
      /**  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   "State1Wages":number,
      /**  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   "State1Tax":number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   "State2TaxTblID":string,
      /**  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  */  
   "State2Wages":number,
      /**  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  */  
   "State2Tax":number,
      /**  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  */  
   "Local1TaxTblID":string,
      /**  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   "Local1Wages":number,
      /**  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   "Local1Tax":number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  */  
   "Local2TaxTblID":string,
      /**  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  */  
   "Local2Wages":number,
      /**  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  */  
   "Local2Tax":number,
      /**  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  */  
   "MiscAmt1":number,
      /**  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   "MiscAmt2":number,
      /**  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   "MiscAmt3":number,
      /**  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  */  
   "MiscAmt4":number,
      /**  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  */  
   "MiscCode1":string,
      /**  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  */  
   "MiscCode2":string,
      /**  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  */  
   "MiscCode3":string,
      /**  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  */  
   "MiscCode4":string,
      /**  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  */  
   "OtherAmt1":number,
      /**  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  */  
   "OtherAmt2":number,
      /**  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  */  
   "OtherAmt3":number,
      /**  Associated Code for OtherAmt1  */  
   "OtherCode1":string,
      /**  Associated Code for OtherAmt2  */  
   "OtherCode2":string,
      /**  Associated Code for OtherAmt3  */  
   "OtherCode3":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  State1TaxDesc  */  
   "State1TaxDesc":string,
      /**  State2TaxDesc  */  
   "State2TaxDesc":string,
   "EmpID":string,
   "SSNum":string,
   "StateTaxID1":string,
   "StateTaxID2":string,
   "EmpName":string,
   "EmployeeAddress":string,
   "FirstName":string,
   "MiddleInitial":string,
   "LastName":string,
   "tmpMiscCode1":string,
   "tmpMiscCode2":string,
   "tmpMiscCode3":string,
   "tmpMiscCode4":string,
      /**  Full description of the payroll class.  */  
   "ClassIDDescription":string,
      /**  Last name of employee  */  
   "EmpLinkLastName":string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmpLinkName":string,
      /**  First name of employee.  */  
   "EmpLinkFirstName":string,
      /**  Last name of employee  */  
   "vrEmpLinkLastName":string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "vrEmpLinkName":string,
      /**  First name of employee.  */  
   "vrEmpLinkFirstName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRW2DtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Identifies the tax year of this W2 record. Used as a component in the primary index.  */  
   "TaxYear":number,
      /**  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  */  
   "ControlNum":number,
      /**  Encoded value which identifies the employee.  */  
   "EmpLink":string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   "ClassID":string,
      /**  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  */  
   "VoidW2":boolean,
      /**  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  */  
   "FitWages":number,
      /**  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  */  
   "FitTax":number,
      /**  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  */  
   "SSWages":number,
      /**  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  */  
   "SSTax":number,
      /**  Social Security Tips  */  
   "SSTips":number,
      /**  Allocation Tips  */  
   "AllocTips":number,
      /**  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  */  
   "MediWages":number,
      /**  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  */  
   "MediTax":number,
      /**  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  */  
   "AdvanceEIC":number,
      /**  Dependent care benefits. Not generated by system.  */  
   "DependCare":number,
      /**  amount of Nonqualified plans. Not generated by system.  */  
   "NQPlan":number,
      /**  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  */  
   "FringeBenefits":number,
      /**  Statutory Employee  */  
   "Statutory":boolean,
      /**  Deceased  */  
   "Deceased":boolean,
      /**  Pension Plan  */  
   "Pension":boolean,
      /**  Legal Representation  */  
   "LegalRep":boolean,
      /**  New field added for 5.2.  Indicates a reirement plan.  */  
   "RetirePlan":boolean,
      /**  Household Employee  */  
   "HouseHold":boolean,
      /**  Indicates if there is third part sick pay.  */  
   "ThirdPartySickPay":boolean,
      /**  Deferred Compensation  */  
   "DeferredComp":boolean,
      /**  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   "State1TaxTblID":string,
      /**  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   "State1Wages":number,
      /**  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   "State1Tax":number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   "State2TaxTblID":string,
      /**  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  */  
   "State2Wages":number,
      /**  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  */  
   "State2Tax":number,
      /**  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  */  
   "Local1TaxTblID":string,
      /**  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   "Local1Wages":number,
      /**  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   "Local1Tax":number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  */  
   "Local2TaxTblID":string,
      /**  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  */  
   "Local2Wages":number,
      /**  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  */  
   "Local2Tax":number,
      /**  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  */  
   "MiscAmt1":number,
      /**  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   "MiscAmt2":number,
      /**  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   "MiscAmt3":number,
      /**  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  */  
   "MiscAmt4":number,
      /**  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  */  
   "MiscCode1":string,
      /**  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  */  
   "MiscCode2":string,
      /**  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  */  
   "MiscCode3":string,
      /**  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  */  
   "MiscCode4":string,
      /**  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  */  
   "OtherAmt1":number,
      /**  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  */  
   "OtherAmt2":number,
      /**  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  */  
   "OtherAmt3":number,
      /**  Associated Code for OtherAmt1  */  
   "OtherCode1":string,
      /**  Associated Code for OtherAmt2  */  
   "OtherCode2":string,
      /**  Associated Code for OtherAmt3  */  
   "OtherCode3":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  State1TaxDesc  */  
   "State1TaxDesc":string,
      /**  State2TaxDesc  */  
   "State2TaxDesc":string,
      /**  SmtrInfo  */  
   "SmtrInfo":string,
      /**  ContactInfo  */  
   "ContactInfo":string,
      /**  PrefNotiCode  */  
   "PrefNotiCode":string,
      /**  Contact Email Address  */  
   "ContactEMail":string,
      /**  Phone Extension  */  
   "ContactExt":string,
   "ContactFax":string,
      /**  Contact Name  */  
   "ContactName":string,
   "ContactPhone":string,
   "EmployeeAddress":string,
   "EmpName":string,
   "FirstName":string,
   "LastName":string,
   "MiddleInitial":string,
      /**   Preferred method of notification code...

1. Email/Internet
2. U.S. Postal Service  */  
   "PrefMethNotificationCode":number,
   "SmtrCity":string,
      /**  Submitter Delivery Address  */  
   "SmtrDeliveryAddr":string,
      /**  Room Number, Suite Number etc...  */  
   "SmtrLocation":string,
      /**  Submitter Name  */  
   "SmtrName":string,
   "SmtrState":string,
   "SmtrZip":string,
   "SmtrZipExt":string,
   "StateTaxID2":string,
   "EmpID":string,
   "SSNum":string,
   "StateTaxID1":string,
   "BitFlag":number,
   "ClassIDDescription":string,
   "EmpLinkName":string,
   "EmpLinkLastName":string,
   "EmpLinkFirstName":string,
   "EmpLinkClassID":string,
   "vrEmpLinkName":string,
   "vrEmpLinkLastName":string,
   "vrEmpLinkFirstName":string,
   "vrEmpLinkClassID":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param InTaxYear
   */  
export interface CheckPRChecksExist_input{
      /**  Tax Year  */  
   InTaxYear:number,
}

export interface CheckPRChecksExist_output{
   returnObj:boolean,
}

   /** Required : 
      @param InTaxYear
   */  
export interface CheckPRW2DtlExists_input{
      /**  The tax year  */  
   InTaxYear:number,
}

export interface CheckPRW2DtlExists_output{
parameters : {
      /**  output parameters  */  
   DataExists:boolean,
}
}

   /** Required : 
      @param taxYear
      @param controlNum
   */  
export interface DeleteByID_input{
   taxYear:number,
   controlNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param filename
   */  
export interface DeleteFile_input{
      /**  File name of a file in UserData folder we need to delete  */  
   filename:string,
}

export interface DeleteFile_output{
}

   /** Required : 
      @param TaxYrFill
      @param ds
   */  
export interface DeletePRW2Dtls_input{
      /**  Tax Year  */  
   TaxYrFill:number,
   ds:Erp_Tablesets_PRW2DtlTableset[],
}

export interface DeletePRW2Dtls_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRW2DtlTableset[],
}
}

export interface Erp_Tablesets_PRW2DtlBoxRow{
      /**  Company  */  
   Company:string,
      /**  TaxYear  */  
   TaxYear:number,
      /**  ControlNum  */  
   ControlNum:number,
      /**  BoxType  */  
   BoxType:string,
      /**  BoxSeq  */  
   BoxSeq:number,
      /**  BoxCode  */  
   BoxCode:string,
      /**  BoxAmount  */  
   BoxAmount:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRW2DtlExportRow{
   ExportLine:string,
   LineNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRW2DtlExportTableset{
   PRW2DtlExport:Erp_Tablesets_PRW2DtlExportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PRW2DtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifies the tax year of this W2 record. Used as a component in the primary index.  */  
   TaxYear:number,
      /**  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  */  
   ControlNum:number,
      /**  Encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  */  
   VoidW2:boolean,
      /**  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  */  
   FitWages:number,
      /**  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  */  
   FitTax:number,
      /**  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  */  
   SSWages:number,
      /**  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  */  
   SSTax:number,
      /**  Social Security Tips  */  
   SSTips:number,
      /**  Allocation Tips  */  
   AllocTips:number,
      /**  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  */  
   MediWages:number,
      /**  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  */  
   MediTax:number,
      /**  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  */  
   AdvanceEIC:number,
      /**  Dependent care benefits. Not generated by system.  */  
   DependCare:number,
      /**  amount of Nonqualified plans. Not generated by system.  */  
   NQPlan:number,
      /**  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  */  
   FringeBenefits:number,
      /**  Statutory Employee  */  
   Statutory:boolean,
      /**  Deceased  */  
   Deceased:boolean,
      /**  Pension Plan  */  
   Pension:boolean,
      /**  Legal Representation  */  
   LegalRep:boolean,
      /**  New field added for 5.2.  Indicates a reirement plan.  */  
   RetirePlan:boolean,
      /**  Household Employee  */  
   HouseHold:boolean,
      /**  Indicates if there is third part sick pay.  */  
   ThirdPartySickPay:boolean,
      /**  Deferred Compensation  */  
   DeferredComp:boolean,
      /**  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   State1TaxTblID:string,
      /**  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   State1Wages:number,
      /**  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   State1Tax:number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   State2TaxTblID:string,
      /**  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  */  
   State2Wages:number,
      /**  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  */  
   State2Tax:number,
      /**  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  */  
   Local1TaxTblID:string,
      /**  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   Local1Wages:number,
      /**  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   Local1Tax:number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  */  
   Local2TaxTblID:string,
      /**  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  */  
   Local2Wages:number,
      /**  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  */  
   Local2Tax:number,
      /**  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  */  
   MiscAmt1:number,
      /**  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   MiscAmt2:number,
      /**  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   MiscAmt3:number,
      /**  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  */  
   MiscAmt4:number,
      /**  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  */  
   MiscCode1:string,
      /**  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  */  
   MiscCode2:string,
      /**  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  */  
   MiscCode3:string,
      /**  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  */  
   MiscCode4:string,
      /**  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  */  
   OtherAmt1:number,
      /**  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  */  
   OtherAmt2:number,
      /**  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  */  
   OtherAmt3:number,
      /**  Associated Code for OtherAmt1  */  
   OtherCode1:string,
      /**  Associated Code for OtherAmt2  */  
   OtherCode2:string,
      /**  Associated Code for OtherAmt3  */  
   OtherCode3:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  State1TaxDesc  */  
   State1TaxDesc:string,
      /**  State2TaxDesc  */  
   State2TaxDesc:string,
   EmpID:string,
   SSNum:string,
   StateTaxID1:string,
   StateTaxID2:string,
   EmpName:string,
   EmployeeAddress:string,
   FirstName:string,
   MiddleInitial:string,
   LastName:string,
   tmpMiscCode1:string,
   tmpMiscCode2:string,
   tmpMiscCode3:string,
   tmpMiscCode4:string,
      /**  Full description of the payroll class.  */  
   ClassIDDescription:string,
      /**  Last name of employee  */  
   EmpLinkLastName:string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmpLinkName:string,
      /**  First name of employee.  */  
   EmpLinkFirstName:string,
      /**  Last name of employee  */  
   vrEmpLinkLastName:string,
      /**  This is the employees full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   vrEmpLinkName:string,
      /**  First name of employee.  */  
   vrEmpLinkFirstName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRW2DtlListTableset{
   PRW2DtlList:Erp_Tablesets_PRW2DtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PRW2DtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifies the tax year of this W2 record. Used as a component in the primary index.  */  
   TaxYear:number,
      /**  A sequential number beginning with 1 for the tax year assigned by the system used as a component of the index which uniquely identifies the record in the database.  */  
   ControlNum:number,
      /**  Encoded value which identifies the employee.  */  
   EmpLink:string,
      /**  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  */  
   ClassID:string,
      /**  Indicates if this W2 is voided.  This value prints on the W2. This is marked when an error has been made on a W2.  Amounts shown on void forms are NOT included in the subtotal form W-2  */  
   VoidW2:boolean,
      /**  Taxable Wages for federal income tax reporting.  It is a summary of PRChkTax.TaxableAmt  */  
   FitWages:number,
      /**  Amount withheld for  federal income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "FIT"  */  
   FitTax:number,
      /**  Taxable Wages for Social Security tax. A summary of PRChkTax.TaxableAmt of TaxType "SS" and EmployerExp = No.  */  
   SSWages:number,
      /**  Amount withheld for  Social Security tax. A summary of PRChkTax.TaxAmt where PRTaxMas.TaxType "SS" and EmployerExp = No.  */  
   SSTax:number,
      /**  Social Security Tips  */  
   SSTips:number,
      /**  Allocation Tips  */  
   AllocTips:number,
      /**  Taxable Wages for Medicare tax reporting.  It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "MEDI" and EmployerExp = No.  */  
   MediWages:number,
      /**  Amount withheld for Medicare tax.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "MEDI"  */  
   MediTax:number,
      /**  If this field is populated, enter this code when it is requested by your tax return preparation software. It is possible your software or preparer will not request the code. The code is not entered on paper-filed returns.  */  
   AdvanceEIC:number,
      /**  Dependent care benefits. Not generated by system.  */  
   DependCare:number,
      /**  amount of Nonqualified plans. Not generated by system.  */  
   NQPlan:number,
      /**  Total value of the taxable fringe benefits included in FIT Wages (box 1) as other compensation. Not generated by system.  */  
   FringeBenefits:number,
      /**  Statutory Employee  */  
   Statutory:boolean,
      /**  Deceased  */  
   Deceased:boolean,
      /**  Pension Plan  */  
   Pension:boolean,
      /**  Legal Representation  */  
   LegalRep:boolean,
      /**  New field added for 5.2.  Indicates a reirement plan.  */  
   RetirePlan:boolean,
      /**  Household Employee  */  
   HouseHold:boolean,
      /**  Indicates if there is third part sick pay.  */  
   ThirdPartySickPay:boolean,
      /**  Deferred Compensation  */  
   DeferredComp:boolean,
      /**  TaxTlbID of PRChkTax records that are summarized into the State1... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   State1TaxTblID:string,
      /**  Taxable Wages for State1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   State1Wages:number,
      /**  Amount withheld for State#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given TaxTblID.  */  
   State1Tax:number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields. This is not used for printing purposes, it is used by the system in order to summarize the tax amounts correctly.  */  
   State2TaxTblID:string,
      /**  Taxable Wages for State2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "SIT" for a given TaxTblID.  */  
   State2Wages:number,
      /**  Amount withheld for State #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "SIT" for the given state  */  
   State2Tax:number,
      /**  TaxTlbID of PRChkTax records that are summarized into the Local1... fields. Unlike the State1TaxTlbID this is printed on the W2purposes.  */  
   Local1TaxTblID:string,
      /**  Taxable Wages for Local1. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   Local1Wages:number,
      /**  Amount withheld for Local#1 income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given TaxTblID.  */  
   Local1Tax:number,
      /**  TaxTlbID of PRChkTax records that are summarized into the State2... fields.  Unlike the State1TaxTlbID this is printed  */  
   Local2TaxTblID:string,
      /**  Taxable Wages for Local2. It is a summary of PRChkTax.TaxableAmt where PRTaxMas.TaxType = "Local" for a given TaxTblID.  */  
   Local2Wages:number,
      /**  Amount withheld for Local #2  income tax reporting.  It is a summary of PRChkTax.TaxAmt where PRTaxMas.TaxType = "Local" for the given state  */  
   Local2Tax:number,
      /**  Now used for box 12. Amount for Box 13.  Contains the YTD deduction amount of deductions that are for employee contributions (401K)  That is where the PRDeduct.SpecialType = "EEC".  */  
   MiscAmt1:number,
      /**  Now used for box 12. 2nd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   MiscAmt2:number,
      /**  Now used for box 12. 3rd Amount for Box 13.  Enter by user through W2 Maintenance program  */  
   MiscAmt3:number,
      /**  4th Amount for Box 12D.  New in 5.2. Enter by user through W2 Maintenance program  */  
   MiscAmt4:number,
      /**  Now used for box 12. Associated Code for MiscAmt1 (Amount 1 for Box 13).   The system will place a "D" here if the employee has any deductions which are marked as SpecialType = "EEC".  See MiscAmt1.  */  
   MiscCode1:string,
      /**  Now used for box 12. Associated Code for MiscAmt2 (Amount 2 in Box 13).   Entered by the user through W2 maintenance.  */  
   MiscCode2:string,
      /**  Now used for box 12. Associated Code for MiscAmt3 (Amount 3 in Box 13).   Entered by the user through W2 maintenance.  */  
   MiscCode3:string,
      /**  Associated Code for MiscAmt4 (Amount in Box 12D).   New in 5.2. Entered by the user through W2 maintenance.  */  
   MiscCode4:string,
      /**  Amount for 1996 Box 14 element amount 1.  Entered by the user if needed via the W2 edit program..  */  
   OtherAmt1:number,
      /**  Amount for 1996 Box 14 element amount 2.  Entered by the user if needed via the W2 edit program.  */  
   OtherAmt2:number,
      /**  Amount for 1996 Box 14 element amount 3.  Entered by the user if needed via the W2 edit program.  */  
   OtherAmt3:number,
      /**  Associated Code for OtherAmt1  */  
   OtherCode1:string,
      /**  Associated Code for OtherAmt2  */  
   OtherCode2:string,
      /**  Associated Code for OtherAmt3  */  
   OtherCode3:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  State1TaxDesc  */  
   State1TaxDesc:string,
      /**  State2TaxDesc  */  
   State2TaxDesc:string,
      /**  SmtrInfo  */  
   SmtrInfo:string,
      /**  ContactInfo  */  
   ContactInfo:string,
      /**  PrefNotiCode  */  
   PrefNotiCode:string,
      /**  Contact Email Address  */  
   ContactEMail:string,
      /**  Phone Extension  */  
   ContactExt:string,
   ContactFax:string,
      /**  Contact Name  */  
   ContactName:string,
   ContactPhone:string,
   EmployeeAddress:string,
   EmpName:string,
   FirstName:string,
   LastName:string,
   MiddleInitial:string,
      /**   Preferred method of notification code...

1. Email/Internet
2. U.S. Postal Service  */  
   PrefMethNotificationCode:number,
   SmtrCity:string,
      /**  Submitter Delivery Address  */  
   SmtrDeliveryAddr:string,
      /**  Room Number, Suite Number etc...  */  
   SmtrLocation:string,
      /**  Submitter Name  */  
   SmtrName:string,
   SmtrState:string,
   SmtrZip:string,
   SmtrZipExt:string,
   StateTaxID2:string,
   EmpID:string,
   SSNum:string,
   StateTaxID1:string,
   BitFlag:number,
   ClassIDDescription:string,
   EmpLinkName:string,
   EmpLinkLastName:string,
   EmpLinkFirstName:string,
   EmpLinkClassID:string,
   vrEmpLinkName:string,
   vrEmpLinkLastName:string,
   vrEmpLinkFirstName:string,
   vrEmpLinkClassID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRW2DtlTableset{
   PRW2Dtl:Erp_Tablesets_PRW2DtlRow[],
   PRW2DtlBox:Erp_Tablesets_PRW2DtlBoxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPRW2DtlTableset{
   PRW2Dtl:Erp_Tablesets_PRW2DtlRow[],
   PRW2DtlBox:Erp_Tablesets_PRW2DtlBoxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param PinNum
      @param TaxYrFill
   */  
export interface ExportPRW2DtlsFile_input{
   PinNum:string,
   TaxYrFill:number,
}

export interface ExportPRW2DtlsFile_output{
   returnObj:string,
}

   /** Required : 
      @param PinNum
      @param TaxYrFill
   */  
export interface ExportPRW2Dtls_input{
      /**  Pin code Number  */  
   PinNum:string,
      /**  Tax Year  */  
   TaxYrFill:number,
}

export interface ExportPRW2Dtls_output{
   returnObj:Erp_Tablesets_PRW2DtlExportTableset[],
}

   /** Required : 
      @param ipEmpID
      @param ipTaxYear
   */  
export interface GetAvailableControlNums_input{
      /**  The Employee ID to get the controlnums  */  
   ipEmpID:string,
      /**  The TaxYearto get the controlnums  */  
   ipTaxYear:number,
}

export interface GetAvailableControlNums_output{
parameters : {
      /**  output parameters  */  
   opControlNums:string,
}
}

   /** Required : 
      @param taxYear
      @param controlNum
   */  
export interface GetByID_input{
   taxYear:number,
   controlNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PRW2DtlTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PRW2DtlTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PRW2DtlTableset[],
}

   /** Required : 
      @param EmpID
   */  
export interface GetEmployeeAddress_input{
      /**  Employee ID  */  
   EmpID:string,
}

export interface GetEmployeeAddress_output{
parameters : {
      /**  output parameters  */  
   EmployeeAddress:string,
}
}

export interface GetEmployerAddress_output{
parameters : {
      /**  output parameters  */  
   EmployerAddress:string,
}
}

export interface GetEmployerEIN_output{
parameters : {
      /**  output parameters  */  
   oEIN:string,
}
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
   returnObj:Erp_Tablesets_PRW2DtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param taxYear
      @param controlNum
      @param boxType
   */  
export interface GetNewPRW2DtlBox_input{
   ds:Erp_Tablesets_PRW2DtlTableset[],
   taxYear:number,
   controlNum:number,
   boxType:string,
}

export interface GetNewPRW2DtlBox_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRW2DtlTableset[],
}
}

   /** Required : 
      @param ds
      @param taxYear
   */  
export interface GetNewPRW2Dtl_input{
   ds:Erp_Tablesets_PRW2DtlTableset[],
   taxYear:number,
}

export interface GetNewPRW2Dtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRW2DtlTableset[],
}
}

   /** Required : 
      @param whereClausePRW2Dtl
      @param whereClausePRW2DtlBox
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePRW2Dtl:string,
   whereClausePRW2DtlBox:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PRW2DtlTableset[],
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
      @param TaxYrFill
   */  
export interface LeaveTaxYear_input{
      /**  Tax Year  */  
   TaxYrFill:number,
}

export interface LeaveTaxYear_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPRW2DtlTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPRW2DtlTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PRW2DtlTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PRW2DtlTableset[],
}
}

export interface ValidateUser_output{
   returnObj:boolean,
}

