import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.POSvc
// Description: Purchase Order Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/$metadata", {
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
   Description: Get POes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderRow
   */  
export function get_POes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes", {
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
   Summary: Calls GetByID to retrieve the PO item
   Description: Calls GetByID to retrieve the PO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderRow
   */  
export function get_POes_Company_PONum(Company:string, PONum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PO for the service
   Description: Calls UpdateExt to update PO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POes_Company_PONum(Company:string, PONum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")", {
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
   Summary: Call UpdateExt to delete PO item
   Description: Call UpdateExt to delete PO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PO
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POes_Company_PONum(Company:string, PONum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")", {
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
   Description: Get PODetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailRow
   */  
export function get_POes_Company_PONum_PODetails(Company:string, PONum:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/PODetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PODetail item
   Description: Calls GetByID to retrieve the PODetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailRow
   */  
export function get_POes_Company_PONum_PODetails_Company_PONUM_POLine(Company:string, PONum:string, PONUM:string, POLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/PODetails(" + Company + "," + PONUM + "," + POLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get POHeadMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeadMiscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeadMiscRow
   */  
export function get_POes_Company_PONum_POHeadMiscs(Company:string, PONum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeadMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeadMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeadMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the POHeadMisc item
   Description: Calls GetByID to retrieve the POHeadMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeadMisc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   */  
export function get_POes_Company_PONum_POHeadMiscs_Company_PONum_POLine_SeqNum(Company:string, PONum:string, POLine:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeadMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeadMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get POHeaderMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeaderMiscTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderMiscTaxRow
   */  
export function get_POes_Company_PONum_POHeaderMiscTaxes(Company:string, PONum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderMiscTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the POHeaderMiscTax item
   Description: Calls GetByID to retrieve the POHeaderMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderMiscTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   */  
export function get_POes_Company_PONum_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, SeqNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeaderMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeaderMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get POHeaderTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeaderTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderTaxRow
   */  
export function get_POes_Company_PONum_POHeaderTaxes(Company:string, PONum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the POHeaderTax item
   Description: Calls GetByID to retrieve the POHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   */  
export function get_POes_Company_PONum_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get POHeaderAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POHeaderAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderAttchRow
   */  
export function get_POes_Company_PONum_POHeaderAttches(Company:string, PONum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the POHeaderAttch item
   Description: Calls GetByID to retrieve the POHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   */  
export function get_POes_Company_PONum_POHeaderAttches_Company_PONum_DrawingSeq(Company:string, PONum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POes(" + Company + "," + PONum + ")/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PODetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailRow
   */  
export function get_PODetails(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PODetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails", {
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
   Summary: Calls GetByID to retrieve the PODetail item
   Description: Calls GetByID to retrieve the PODetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailRow
   */  
export function get_PODetails_Company_PONUM_POLine(Company:string, PONUM:string, POLine:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PODetail for the service
   Description: Calls UpdateExt to update PODetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PODetails_Company_PONUM_POLine(Company:string, PONUM:string, POLine:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")", {
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
   Summary: Call UpdateExt to delete PODetail item
   Description: Call UpdateExt to delete PODetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PODetails_Company_PONUM_POLine(Company:string, PONUM:string, POLine:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")", {
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
   Description: Get PORels items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORels1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelRow
   */  
export function get_PODetails_Company_PONUM_POLine_PORels(Company:string, PONUM:string, POLine:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PORels", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PORel item
   Description: Calls GetByID to retrieve the PORel item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORel1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param PONum Desc: PONum   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelRow
   */  
export function get_PODetails_Company_PONUM_POLine_PORels_Company_PONum_POLine_PORelNum(Company:string, PONUM:string, POLine:string, PONum:string, PORelNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PODetailInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailInsps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailInspRow
   */  
export function get_PODetails_Company_PONUM_POLine_PODetailInsps(Company:string, PONUM:string, POLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PODetailInsp item
   Description: Calls GetByID to retrieve the PODetailInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailInsp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   */  
export function get_PODetails_Company_PONUM_POLine_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company:string, PONUM:string, POLine:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PODetailTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailTaxRow
   */  
export function get_PODetails_Company_PONUM_POLine_PODetailTaxes(Company:string, PONUM:string, POLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PODetailTax item
   Description: Calls GetByID to retrieve the PODetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param PONum Desc: PONum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   */  
export function get_PODetails_Company_PONUM_POLine_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONUM:string, POLine:string, PONum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get POMiscs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POMiscs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POMiscRow
   */  
export function get_PODetails_Company_PONUM_POLine_POMiscs(Company:string, PONUM:string, POLine:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/POMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the POMisc item
   Description: Calls GetByID to retrieve the POMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POMisc1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param PONum Desc: PONum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POMiscRow
   */  
export function get_PODetails_Company_PONUM_POLine_POMiscs_Company_PONum_POLine_SeqNum(Company:string, PONUM:string, POLine:string, PONum:string, SeqNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PODetailAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailAttchRow
   */  
export function get_PODetails_Company_PONUM_POLine_PODetailAttches(Company:string, PONUM:string, POLine:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PODetailAttch item
   Description: Calls GetByID to retrieve the PODetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   */  
export function get_PODetails_Company_PONUM_POLine_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company:string, PONUM:string, POLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetails(" + Company + "," + PONUM + "," + POLine + ")/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PORels items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORels
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelRow
   */  
export function get_PORels(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORels
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PORels(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels", {
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
   Summary: Calls GetByID to retrieve the PORel item
   Description: Calls GetByID to retrieve the PORel item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelRow
   */  
export function get_PORels_Company_PONum_POLine_PORelNum(Company:string, PONum:string, POLine:string, PORelNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PORel for the service
   Description: Calls UpdateExt to update PORel. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PORels_Company_PONum_POLine_PORelNum(Company:string, PONum:string, POLine:string, PORelNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
   Summary: Call UpdateExt to delete PORel item
   Description: Call UpdateExt to delete PORel item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORel
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PORels_Company_PONum_POLine_PORelNum(Company:string, PONum:string, POLine:string, PORelNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", {
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
   Description: Get PORelTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORelTGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTGLCRow
   */  
export function get_PORels_Company_PONum_POLine_PORelNum_PORelTGLCs(Company:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PORelTGLC item
   Description: Calls GetByID to retrieve the PORelTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   */  
export function get_PORels_Company_PONum_POLine_PORelNum_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company:string, PONum:string, POLine:string, PORelNum:string, BookID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PORelTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORelTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTaxRow
   */  
export function get_PORels_Company_PONum_POLine_PORelNum_PORelTaxes(Company:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PORelTax item
   Description: Calls GetByID to retrieve the PORelTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   */  
export function get_PORels_Company_PONum_POLine_PORelNum_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PORelAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PORelAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelAttchRow
   */  
export function get_PORels_Company_PONum_POLine_PORelNum_PORelAttches(Company:string, PONum:string, POLine:string, PORelNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PORelAttch item
   Description: Calls GetByID to retrieve the PORelAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   */  
export function get_PORels_Company_PONum_POLine_PORelNum_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORels(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PORelTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelTGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTGLCRow
   */  
export function get_PORelTGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PORelTGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs", {
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
   Summary: Calls GetByID to retrieve the PORelTGLC item
   Description: Calls GetByID to retrieve the PORelTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   */  
export function get_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company:string, PONum:string, POLine:string, PORelNum:string, BookID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelTGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelTGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PORelTGLC for the service
   Description: Calls UpdateExt to update PORelTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company:string, PONum:string, POLine:string, PORelNum:string, BookID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")", {
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
   Summary: Call UpdateExt to delete PORelTGLC item
   Description: Call UpdateExt to delete PORelTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelTGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param BookID Desc: BookID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PORelTGLCs_Company_PONum_POLine_PORelNum_BookID(Company:string, PONum:string, POLine:string, PORelNum:string, BookID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTGLCs(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + BookID + ")", {
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
   Description: Get PORelTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelTaxRow
   */  
export function get_PORelTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PORelTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes", {
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
   Summary: Calls GetByID to retrieve the PORelTax item
   Description: Calls GetByID to retrieve the PORelTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   */  
export function get_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PORelTax for the service
   Description: Calls UpdateExt to update PORelTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete PORelTax item
   Description: Call UpdateExt to delete PORelTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PORelTaxes_Company_PONum_POLine_PORelNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, PORelNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelTaxes(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get PORelAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelAttchRow
   */  
export function get_PORelAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PORelAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches", {
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
   Summary: Calls GetByID to retrieve the PORelAttch item
   Description: Calls GetByID to retrieve the PORelAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   */  
export function get_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PORelAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PORelAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PORelAttch for the service
   Description: Calls UpdateExt to update PORelAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PORelAttch item
   Description: Call UpdateExt to delete PORelAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param PORelNum Desc: PORelNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PORelAttches_Company_PONum_POLine_PORelNum_DrawingSeq(Company:string, PONum:string, POLine:string, PORelNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PORelAttches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + "," + DrawingSeq + ")", {
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
   Description: Get PODetailInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailInsps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailInspRow
   */  
export function get_PODetailInsps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PODetailInsps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps", {
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
   Summary: Calls GetByID to retrieve the PODetailInsp item
   Description: Calls GetByID to retrieve the PODetailInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   */  
export function get_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company:string, PONUM:string, POLine:string, PlanSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailInspRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailInspRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PODetailInsp for the service
   Description: Calls UpdateExt to update PODetailInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company:string, PONUM:string, POLine:string, PlanSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")", {
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
   Summary: Call UpdateExt to delete PODetailInsp item
   Description: Call UpdateExt to delete PODetailInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailInsp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param PlanSeq Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PODetailInsps_Company_PONUM_POLine_PlanSeq(Company:string, PONUM:string, POLine:string, PlanSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailInsps(" + Company + "," + PONUM + "," + POLine + "," + PlanSeq + ")", {
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
   Description: Get PODetailTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailTaxRow
   */  
export function get_PODetailTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PODetailTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes", {
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
   Summary: Calls GetByID to retrieve the PODetailTax item
   Description: Calls GetByID to retrieve the PODetailTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   */  
export function get_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PODetailTax for the service
   Description: Calls UpdateExt to update PODetailTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete PODetailTax item
   Description: Call UpdateExt to delete PODetailTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PODetailTaxes_Company_PONum_POLine_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailTaxes(" + Company + "," + PONum + "," + POLine + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get POMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POMiscs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POMiscRow
   */  
export function get_POMiscs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POMiscs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs", {
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
   Summary: Calls GetByID to retrieve the POMisc item
   Description: Calls GetByID to retrieve the POMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POMiscRow
   */  
export function get_POMiscs_Company_PONum_POLine_SeqNum(Company:string, PONum:string, POLine:string, SeqNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POMisc for the service
   Description: Calls UpdateExt to update POMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POMiscs_Company_PONum_POLine_SeqNum(Company:string, PONum:string, POLine:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete POMisc item
   Description: Call UpdateExt to delete POMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POMiscs_Company_PONum_POLine_SeqNum(Company:string, PONum:string, POLine:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
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
   Description: Get PODetailMiscTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PODetailMiscTaxes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailMiscTaxRow
   */  
export function get_POMiscs_Company_PONum_POLine_SeqNum_PODetailMiscTaxes(Company:string, PONum:string, POLine:string, SeqNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")/PODetailMiscTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PODetailMiscTax item
   Description: Calls GetByID to retrieve the PODetailMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailMiscTax1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param PONUM Desc: PONUM   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   */  
export function get_POMiscs_Company_PONum_POLine_SeqNum_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, POLine:string, SeqNum:string, PONUM:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PODetailMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailMiscTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailMiscTaxRow
   */  
export function get_PODetailMiscTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailMiscTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PODetailMiscTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes", {
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
   Summary: Calls GetByID to retrieve the PODetailMiscTax item
   Description: Calls GetByID to retrieve the PODetailMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   */  
export function get_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONUM:string, POLine:string, SeqNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PODetailMiscTax for the service
   Description: Calls UpdateExt to update PODetailMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONUM:string, POLine:string, SeqNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete PODetailMiscTax item
   Description: Call UpdateExt to delete PODetailMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PODetailMiscTaxes_Company_PONUM_POLine_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONUM:string, POLine:string, SeqNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailMiscTaxes(" + Company + "," + PONUM + "," + POLine + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get PODetailAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PODetailAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PODetailAttchRow
   */  
export function get_PODetailAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PODetailAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PODetailAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches", {
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
   Summary: Calls GetByID to retrieve the PODetailAttch item
   Description: Calls GetByID to retrieve the PODetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PODetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   */  
export function get_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company:string, PONUM:string, POLine:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PODetailAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PODetailAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PODetailAttch for the service
   Description: Calls UpdateExt to update PODetailAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PODetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PODetailAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company:string, PONUM:string, POLine:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PODetailAttch item
   Description: Call UpdateExt to delete PODetailAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PODetailAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONUM Desc: PONUM   Required: True
      @param POLine Desc: POLine   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PODetailAttches_Company_PONUM_POLine_DrawingSeq(Company:string, PONUM:string, POLine:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PODetailAttches(" + Company + "," + PONUM + "," + POLine + "," + DrawingSeq + ")", {
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
   Description: Get POHeadMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeadMiscs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeadMiscRow
   */  
export function get_POHeadMiscs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeadMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeadMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeadMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POHeadMiscs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs", {
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
   Summary: Calls GetByID to retrieve the POHeadMisc item
   Description: Calls GetByID to retrieve the POHeadMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeadMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   */  
export function get_POHeadMiscs_Company_PONum_POLine_SeqNum(Company:string, PONum:string, POLine:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeadMiscRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeadMiscRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POHeadMisc for the service
   Description: Calls UpdateExt to update POHeadMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeadMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeadMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POHeadMiscs_Company_PONum_POLine_SeqNum(Company:string, PONum:string, POLine:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete POHeadMisc item
   Description: Call UpdateExt to delete POHeadMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeadMisc
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param POLine Desc: POLine   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POHeadMiscs_Company_PONum_POLine_SeqNum(Company:string, PONum:string, POLine:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeadMiscs(" + Company + "," + PONum + "," + POLine + "," + SeqNum + ")", {
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
   Description: Get POHeaderMiscTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeaderMiscTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderMiscTaxRow
   */  
export function get_POHeaderMiscTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeaderMiscTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POHeaderMiscTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes", {
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
   Summary: Calls GetByID to retrieve the POHeaderMiscTax item
   Description: Calls GetByID to retrieve the POHeaderMiscTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   */  
export function get_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, SeqNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeaderMiscTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeaderMiscTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POHeaderMiscTax for the service
   Description: Calls UpdateExt to update POHeaderMiscTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeaderMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderMiscTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, SeqNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete POHeaderMiscTax item
   Description: Call UpdateExt to delete POHeaderMiscTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeaderMiscTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POHeaderMiscTaxes_Company_PONum_SeqNum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, SeqNum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderMiscTaxes(" + Company + "," + PONum + "," + SeqNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get POHeaderTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeaderTaxes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderTaxRow
   */  
export function get_POHeaderTaxes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeaderTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POHeaderTaxes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes", {
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
   Summary: Calls GetByID to retrieve the POHeaderTax item
   Description: Calls GetByID to retrieve the POHeaderTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   */  
export function get_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeaderTaxRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeaderTaxRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POHeaderTax for the service
   Description: Calls UpdateExt to update POHeaderTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeaderTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Summary: Call UpdateExt to delete POHeaderTax item
   Description: Call UpdateExt to delete POHeaderTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeaderTax
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param TaxCode Desc: TaxCode   Required: True   Allow empty value : True
      @param RateCode Desc: RateCode   Required: True   Allow empty value : True
      @param ECAcquisitionSeq Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POHeaderTaxes_Company_PONum_TaxCode_RateCode_ECAcquisitionSeq(Company:string, PONum:string, TaxCode:string, RateCode:string, ECAcquisitionSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderTaxes(" + Company + "," + PONum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", {
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
   Description: Get POHeaderAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POHeaderAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderAttchRow
   */  
export function get_POHeaderAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POHeaderAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_POHeaderAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches", {
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
   Summary: Calls GetByID to retrieve the POHeaderAttch item
   Description: Calls GetByID to retrieve the POHeaderAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POHeaderAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   */  
export function get_POHeaderAttches_Company_PONum_DrawingSeq(Company:string, PONum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_POHeaderAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_POHeaderAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update POHeaderAttch for the service
   Description: Calls UpdateExt to update POHeaderAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POHeaderAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POHeaderAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_POHeaderAttches_Company_PONum_DrawingSeq(Company:string, PONum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete POHeaderAttch item
   Description: Call UpdateExt to delete POHeaderAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POHeaderAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PONum Desc: PONum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_POHeaderAttches_Company_PONum_DrawingSeq(Company:string, PONum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/POHeaderAttches(" + Company + "," + PONum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POHeaderListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClausePOHeader:string, whereClausePOHeaderAttch:string, whereClausePODetail:string, whereClausePODetailAttch:string, whereClausePORel:string, whereClausePORelAttch:string, whereClausePORelTax:string, whereClausePORelTGLC:string, whereClausePODetailInsp:string, whereClausePODetailTax:string, whereClausePOMisc:string, whereClausePODetailMiscTax:string, whereClausePOHeadMisc:string, whereClausePOHeaderMiscTax:string, whereClausePOHeaderTax:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePOHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOHeader=" + whereClausePOHeader
   }
   if(typeof whereClausePOHeaderAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOHeaderAttch=" + whereClausePOHeaderAttch
   }
   if(typeof whereClausePODetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePODetail=" + whereClausePODetail
   }
   if(typeof whereClausePODetailAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePODetailAttch=" + whereClausePODetailAttch
   }
   if(typeof whereClausePORel!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePORel=" + whereClausePORel
   }
   if(typeof whereClausePORelAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePORelAttch=" + whereClausePORelAttch
   }
   if(typeof whereClausePORelTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePORelTax=" + whereClausePORelTax
   }
   if(typeof whereClausePORelTGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePORelTGLC=" + whereClausePORelTGLC
   }
   if(typeof whereClausePODetailInsp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePODetailInsp=" + whereClausePODetailInsp
   }
   if(typeof whereClausePODetailTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePODetailTax=" + whereClausePODetailTax
   }
   if(typeof whereClausePOMisc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOMisc=" + whereClausePOMisc
   }
   if(typeof whereClausePODetailMiscTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePODetailMiscTax=" + whereClausePODetailMiscTax
   }
   if(typeof whereClausePOHeadMisc!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOHeadMisc=" + whereClausePOHeadMisc
   }
   if(typeof whereClausePOHeaderMiscTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOHeaderMiscTax=" + whereClausePOHeaderMiscTax
   }
   if(typeof whereClausePOHeaderTax!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePOHeaderTax=" + whereClausePOHeaderTax
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetRows" + params, {
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
export function get_GetByID(poNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof poNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "poNum=" + poNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetList" + params, {
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
   Summary: Invoke method ChangeTaxFixedAmount
   Description: Method to call when changing the fixed amount on the PORelTax table currently
   OperationID: ChangeTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxFixedAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxFixedAmount", {
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
   Summary: Invoke method ChangeTaxReportableAmt
   Description: Method to call when changing the reportable amount on either POHeaderMiscTax / PODetailMiscTax or PORelTax
reportable amounts based on the new reportable amount.
   OperationID: ChangeTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxReportableAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxReportableAmt", {
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
   Summary: Invoke method ChangeTaxTaxableAmt
   Description: Method to call when changing the taxable amount on either POHeaderMiscTax / PODetailMiscTax or PORelTax
taxable amounts based on the new taxable amount.
   OperationID: ChangeTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxTaxableAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxTaxableAmt", {
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
   Summary: Invoke method ChangeTaxTaxAmt
   Description: Method to call when changing the tax amount on a either a POHeaderMiscTax / PODetailMiscTax or a PORelTax row
tax amounts based on the new tax amount.
   OperationID: ChangeTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxTaxAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxTaxAmt", {
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
   Summary: Invoke method ChangeTaxDeductable
   Description: Method to call when changing the tax deductable on a Release line tax record.
   OperationID: ChangeTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxDeductable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxDeductable", {
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
   Summary: Invoke method ChangeTaxTaxCode
   Description: Method to call when changing the tax code on a the POHeaderMiscTax, PODetailMiscTax or PORelTax.  Validates the tax code and
updates PORelTax tax amounts based on the new tax code.
   OperationID: ChangeTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxTaxCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxTaxCode", {
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
   Summary: Invoke method ChangeTaxRateCode
   Description: Method to call when changing the rate code on a tax record related to Release Tax Line.  Validates the rate and tax code
   OperationID: ChangeTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxRateCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxRateCode", {
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
   Summary: Invoke method ChangeTaxPercent
   Description: Method to call when changing the tax percent on a tax release line record.  Updates PORelTax
tax amounts based on the new tax percent only when one tax record exists.
   OperationID: ChangeTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTaxPercent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTaxPercent", {
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
   Summary: Invoke method ChangeExpAcct
   Description: This method sets the flag in PORelTGLC that indicates if the account
has been overridden from the default.
   OperationID: ChangeExpAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExpAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExpAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeExpAcct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeExpAcct", {
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
   Summary: Invoke method ValidateAcctForGLControl
   Description: Validates an account has been entered for glcontrol of a PUR-UKN PORel record
   OperationID: ValidateAcctForGLControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAcctForGLControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAcctForGLControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAcctForGLControl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ValidateAcctForGLControl", {
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
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInspection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ValidateInspection", {
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
   Summary: Invoke method ValidataPartToLinkToContract
   Description: Validate Parts allowed for Planning Contracts.
   OperationID: ValidataPartToLinkToContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidataPartToLinkToContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidataPartToLinkToContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidataPartToLinkToContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ValidataPartToLinkToContract", {
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
   Summary: Invoke method ValidatePOLinesTaxCategoryTypes
   Description: Method to validate that all Purchase Order lines have Tax Categories with the same Tax Category Type
   OperationID: ValidatePOLinesTaxCategoryTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePOLinesTaxCategoryTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePOLinesTaxCategoryTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePOLinesTaxCategoryTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ValidatePOLinesTaxCategoryTypes", {
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
   Summary: Invoke method GetNewPOHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPOHeader", {
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
   Summary: Invoke method GetNewPOHeaderAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeaderAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeaderAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeaderAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOHeaderAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPOHeaderAttch", {
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
   Summary: Invoke method GetNewPODetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPODetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPODetail", {
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
   Summary: Invoke method GetNewPODetailAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPODetailAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPODetailAttch", {
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
   Summary: Invoke method GetNewPORel
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPORel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPORel", {
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
   Summary: Invoke method GetNewPORelAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORelAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORelAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORelAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPORelAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPORelAttch", {
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
   Summary: Invoke method GetNewPORelTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORelTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORelTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORelTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPORelTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPORelTax", {
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
   Summary: Invoke method GetNewPORelTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORelTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORelTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORelTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPORelTGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPORelTGLC", {
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
   Summary: Invoke method GetNewPODetailInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPODetailInsp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPODetailInsp", {
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
   Summary: Invoke method GetNewPODetailTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPODetailTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPODetailTax", {
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
   Summary: Invoke method GetNewPOMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOMisc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPOMisc", {
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
   Summary: Invoke method GetNewPODetailMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPODetailMiscTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPODetailMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPODetailMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPODetailMiscTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPODetailMiscTax", {
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
   Summary: Invoke method GetNewPOHeadMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeadMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeadMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeadMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOHeadMisc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPOHeadMisc", {
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
   Summary: Invoke method GetNewPOHeaderMiscTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeaderMiscTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeaderMiscTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeaderMiscTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOHeaderMiscTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPOHeaderMiscTax", {
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
   Summary: Invoke method GetNewPOHeaderTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOHeaderTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOHeaderTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOHeaderTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPOHeaderTax(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewPOHeaderTax", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/UpdateExt", {
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
   Summary: Invoke method CheckForMRPAttributes
   Description: Check for potential warnings / confirmations before performing the PO update
   OperationID: CheckForMRPAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForMRPAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForMRPAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForMRPAttributes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckForMRPAttributes", {
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
   Summary: Invoke method CalcAutoPORelTGLC
   Description: Auto Calculate PORelTGLC
   OperationID: CalcAutoPORelTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcAutoPORelTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAutoPORelTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcAutoPORelTGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CalcAutoPORelTGLC", {
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
   Summary: Invoke method CheckBeforeUpdate
   Description: Check for potential warnings / confirmations before performing the PO update
   OperationID: CheckBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBeforeUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckBeforeUpdate", {
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
   Summary: Invoke method CheckLOCWithMessages
   Description: Provides a way to call CheckLOC from MetaUI.
Checks outstanding amounts to limit on APLOC (if applicable)
This should be called before updating POHeader, PODetail,PORel, POMisc, or POHeadMisc
If limit is exceeded a string is returned asking the user if they want to override.
If Releases have distinct Due Date and LOC is marked as "Ship Complete", a string is returned asking the user if they want to continue.
   OperationID: CheckLOCWithMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLOCWithMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLOCWithMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckLOCWithMessages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckLOCWithMessages", {
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
   Summary: Invoke method CheckLOC
   Description: Checks outstanding amounts to limit on APLOC (if applicable)
This should be called before updating POHeader, PODetail,PORel, POMisc, or POHeadMisc
If limit is exceeded a string is returned asking the user if they want to override.
If Releases have distinct Due Date and LOC is marked as "Ship Complete", a string is returned asking the user if they want to continue.
Not able to be used with MetaUI because of the output param array.
   OperationID: CheckLOC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckLOC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckLOC", {
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
   Summary: Invoke method CheckPODetailCNBonded
   Description: Purpose:  Check Bonded on line
Parameters:
<param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckPODetailCNBonded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPODetailCNBonded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPODetailCNBonded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPODetailCNBonded(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckPODetailCNBonded", {
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
   Summary: Invoke method CheckPONum
   Description: Method to call when entering proposed PO Number.  This method will return
two output variables.  One is a logical field to indicate if the PO number
entered is existing or not.  The other variable is for the error message
in case the proposed PO number is invalid.
Removed Return from the end of this procedure
   OperationID: CheckPONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPONum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckPONum", {
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
   Summary: Invoke method chkPODatesChanges
   Description: SCR 142197 - New logic to let the user know which date fields chenged
Checks to see if certain fields changed on the order header or order line.  If they did,
a question is presented to the user asking if these changes should carry over
to the order lines and/or order releases.  This method returns the text of the message
to ask.  When adding a header it is not necessary to call this method because there
won't be any lines or releases to propogate the changes to.  The user can answer yes
or no, but processing doesn't stop based on the answer.  The answer should be stored
in the dataset in field OrderHed.UpdateDtlAndRelRecords.
   OperationID: chkPODatesChanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/chkPODatesChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/chkPODatesChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_chkPODatesChanges(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/chkPODatesChanges", {
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
   Summary: Invoke method CloseOrder
   Description: Filters up available open orders/lines
   OperationID: CloseOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CloseOrder", {
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
   Summary: Invoke method CloseOrderLine
   Description: Filters up available open lines
   OperationID: CloseOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CloseOrderLine", {
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
   Summary: Invoke method CloseRelease
   Description: Run this method to close a release .
   OperationID: CloseRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseRelease(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CloseRelease", {
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
   Summary: Invoke method PreDuplicatePO
   Description: Checks attributes before duplicating a PO
   OperationID: PreDuplicatePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDuplicatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDuplicatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreDuplicatePO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PreDuplicatePO", {
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
   Summary: Invoke method DuplicatePO
   Description: Duplicates PO
   OperationID: DuplicatePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicatePO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/DuplicatePO", {
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
   Summary: Invoke method GetAPLOCDescription
   Description: This method should be invoked when it is required to set the APLOC Description changes.
   OperationID: GetAPLOCDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPLOCDescription(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetAPLOCDescription", {
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
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetCodeDescList", {
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
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyBase(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetCurrencyBase", {
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
   Summary: Invoke method GetDefaultBuyer
   Description: Returns default buyer information for the current user.
   OperationID: GetDefaultBuyer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultBuyer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultBuyer(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetDefaultBuyer", {
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
   Summary: Invoke method GetDefaultGLAccountAllPOReleases
   Description: Get Default GL Account for All the Releases.
<param name="pPONum">PO Number</param><param name="ds" type="Epicor.Mfg.BO.PODataSet">The Purchase Order data set </param>
   OperationID: GetDefaultGLAccountAllPOReleases
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultGLAccountAllPOReleases_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultGLAccountAllPOReleases_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultGLAccountAllPOReleases(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetDefaultGLAccountAllPOReleases", {
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
   Summary: Invoke method GetDropShipPOHeaderList
   Description: Perform a GetList but only return POs that exist on a DropShipDtl
   OperationID: GetDropShipPOHeaderList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDropShipPOHeaderList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDropShipPOHeaderList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDropShipPOHeaderList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetDropShipPOHeaderList", {
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
   Summary: Invoke method GetNewConsolidatedPO
   Description: Method to call when adding a Consolidated PO
   OperationID: GetNewConsolidatedPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsolidatedPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsolidatedPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewConsolidatedPO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewConsolidatedPO", {
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
   Summary: Invoke method GetNewContractPO
   Description: Method to call when adding a Consolidated PO
   OperationID: GetNewContractPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContractPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContractPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewContractPO(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetNewContractPO", {
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
   Summary: Invoke method GetGlbCompanyList
   Description: Returns a list of available companies to choose from for the
Global Company field.  Returns the list in code1`desc1~code2`desc2 format.
   OperationID: GetGlbCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlbCompanyList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetGlbCompanyList", {
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
   Summary: Invoke method GetPartSubList
   Description: Public method to get the poapvmsg dataset.
   OperationID: GetPartSubList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartSubList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartSubList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartSubList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetPartSubList", {
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
   Summary: Invoke method GetPOReceipts
   Description: Gets RcvDtl's and DropShipDtl's for a given PONum.
   OperationID: GetPOReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOReceipts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetPOReceipts", {
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
   Summary: Invoke method GetPORelationshipMap
   Description: Returns a serialized json string to show a Relationship Map for PO
   OperationID: GetPORelationshipMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPORelationshipMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPORelationshipMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPORelationshipMap(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetPORelationshipMap", {
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
   Summary: Invoke method GetRowsForAPInvoice
   Description: Invokes GetRows filtering on PO's for the specified Invoice
   OperationID: GetRowsForAPInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForAPInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForAPInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForAPInvoice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetRowsForAPInvoice", {
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
   Summary: Invoke method GetRowsForPayment
   Description: Invokes GetRows filtering on PO's for the specified Payment
   OperationID: GetRowsForPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForPayment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetRowsForPayment", {
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
   Summary: Invoke method GetRowsForReceipt
   Description: Invokes GetRows filtering on PO's for the specified Pack slip
   OperationID: GetRowsForReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsForReceipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetRowsForReceipt", {
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
   Summary: Invoke method GetShipToAddressForCompany
   Description: Gets the ShipTo Address for the current company
   OperationID: GetShipToAddressForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipToAddressForCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetShipToAddressForCompany", {
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
   Summary: Invoke method GetShipToAddressForCustomer
   Description: Gets the ShipTo Address for a customer
   OperationID: GetShipToAddressForCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipToAddressForCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetShipToAddressForCustomer", {
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
   Summary: Invoke method GetShipToAddressForSite
   Description: Gets the ShipTo Address for a Site
   OperationID: GetShipToAddressForSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipToAddressForSite(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetShipToAddressForSite", {
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
   Summary: Invoke method GetShipToAddressForSupplier
   Description: Gets the ShipTo Address for a Supplier
   OperationID: GetShipToAddressForSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipToAddressForSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipToAddressForSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipToAddressForSupplier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetShipToAddressForSupplier", {
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
   Summary: Invoke method ReopenOrder
   Description: Reopens order
   OperationID: ReopenOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReopenOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReopenOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReopenOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ReopenOrder", {
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
   Summary: Invoke method ReopenOrderLine
   Description: Reopens order line
   OperationID: ReopenOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReopenOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReopenOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReopenOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ReopenOrderLine", {
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
   Summary: Invoke method VerifyReopenRelease
   Description: Precheck before reopening an order release.
   OperationID: VerifyReopenRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyReopenRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyReopenRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyReopenRelease(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/VerifyReopenRelease", {
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
   Summary: Invoke method ReOpenRelease
   Description: Run this method to reopen a release.
   OperationID: ReOpenRelease
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReOpenRelease_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReOpenRelease_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReOpenRelease(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ReOpenRelease", {
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
   Summary: Invoke method SetReadyToCalc
   Description: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
<param name="poNum">poNum </param><param name="calledFromUI">calledFromUI</param><param name="ds">APInvoice dataset</param>
   OperationID: SetReadyToCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetReadyToCalc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/SetReadyToCalc", {
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
   Summary: Invoke method ChangeContractUOM
   Description: Call this method when the PODetail.ContractQtyUOM changes.
   OperationID: ChangeContractUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeContractUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContractUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeContractUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeContractUOM", {
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
   Summary: Invoke method ChangeDetailAssemblySeq
   Description: Invoke when assembly on the detail sheet changes. It will validate the release and
zero out the JobSeq.
   OperationID: ChangeDetailAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailAssemblySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailAssemblySeq", {
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
   Summary: Invoke method ChangeDetailCalcOurQty
   Description: Run this method when our quantity on the detail changes.
   OperationID: ChangeDetailCalcOurQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailCalcOurQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailCalcOurQty", {
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
   Summary: Invoke method ChangeDetailCostPerCode
   Description: Run this method when the Cost Per factor on the detail changes.
   OperationID: ChangeDetailCostPerCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCostPerCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCostPerCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailCostPerCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailCostPerCode", {
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
   Summary: Invoke method ChangeDetailCalcVendQty
   Description: Run this method when supplier quantity on the detail changes.
   OperationID: ChangeDetailCalcVendQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcVendQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcVendQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailCalcVendQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailCalcVendQty", {
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
   Summary: Invoke method ChangeDetailCommodityCode
   Description: Validate entered Commodity Code
   OperationID: ChangeDetailCommodityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCommodityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCommodityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailCommodityCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailCommodityCode", {
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
   Summary: Invoke method ChangeDetailIUM
   Description: Call this method when the IUM changes on the PODetail.
   OperationID: ChangeDetailIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailIUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailIUM", {
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
   Summary: Invoke method ChangeDetailJobNum
   Description: This method is used when the jobnumber on the detail screen changes .
   OperationID: ChangeDetailJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailJobNum", {
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
   Summary: Invoke method ChangeDetailJobSeq
   Description: Invoke when Job/mtl sequence on the Detail sheet changes. I
   OperationID: ChangeDetailJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailJobSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailJobSeq", {
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
   Summary: Invoke method ChangeDetailMangCust
   Description: Run this method when MangCustID on the detail changes.
   OperationID: ChangeDetailMangCust
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailMangCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailMangCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailMangCust(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailMangCust", {
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
   Summary: Invoke method ChangeDetailMfgNum
   Description: Call this method when the MfgNum changes on the PODetail.
   OperationID: ChangeDetailMfgNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailMfgNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailMfgNum", {
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
   Summary: Invoke method ChangeDetailMfgPartNum
   Description: Call this method when the MfgPartNum changes on the PODetail.
   OperationID: ChangeDetailMfgPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailMfgPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailMfgPartNum", {
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
   Summary: Invoke method ChangeDetailOrderLine
   Description: Call this method when the OrderLine changes on the PODetail.
   OperationID: ChangeDetailOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailOrderLine", {
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
   Summary: Invoke method ChangeDetailOrderNum
   Description: Call this method when the OrderNum changes on the PODetail.
   OperationID: ChangeDetailOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailOrderNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailOrderNum", {
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
   Summary: Invoke method ChangeDetailOverridePriceList
   Description: Run this method when the override pricelist is unchecked
   OperationID: ChangeDetailOverridePriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOverridePriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOverridePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailOverridePriceList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailOverridePriceList", {
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
   Summary: Invoke method ChangeDetailPartClass
   Description: Run this method when the Class ID on the detail screen changes .
   OperationID: ChangeDetailPartClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailPartClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPartClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailPartClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailPartClass", {
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
   Summary: Invoke method ChangeDetailPartNum
   Description: Run this method when the partnumber on the detail screen changes .
   OperationID: ChangeDetailPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailPartNum", {
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
   Summary: Invoke method ChangeDetailContractID
   Description: Run this method when the Contract ID on the detail screen changes
   OperationID: ChangeDetailContractID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailContractID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailContractID", {
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
   Summary: Invoke method ChangeDetailPUM
   Description: Call this method when the PUM changes on the PODetail.
   OperationID: ChangeDetailPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailPUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailPUM", {
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
   Summary: Invoke method ChangeDetailRevisionNum
   Description: Change PO Detail Revision Number
   OperationID: ChangeDetailRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailRevisionNum", {
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
   Summary: Invoke method ChangeUOMConfirm
   Description: Confirm is attributes exit before changing UOM
   OperationID: ChangeUOMConfirm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUOMConfirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUOMConfirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUOMConfirm(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeUOMConfirm", {
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
   Summary: Invoke method ChangeDetailTaxCatID
   Description: Call this method when changing the Tax Category
   OperationID: ChangeDetailTaxCatID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailTaxCatID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailTaxCatID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailTaxCatID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailTaxCatID", {
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
   Summary: Invoke method ChangeDetailTranType
   Description: Call this method when the TranType (LineType) changes on the PODetail.
It will update the price on the release
   OperationID: ChangeDetailTranType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailTranType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailTranType", {
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
   Summary: Invoke method ChangingDetailRevisionNum
   Description: Change PO Detail Revision Number
   OperationID: ChangingDetailRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangingDetailRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangingDetailRevisionNum", {
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
   Summary: Invoke method ChangeDetailVenPartNum
   Description: Call this method when the VenPartNum changes on the PODetail.
   OperationID: ChangeDetailVenPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailVenPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailVenPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailVenPartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeDetailVenPartNum", {
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
   Summary: Invoke method ChangeUnitPrice
   Description: Calculates the UnitPrice or DocUnitPrice depending of the Currency Switch.
   OperationID: ChangeUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUnitPrice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeUnitPrice", {
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
   Summary: Invoke method ChangeUnitPriceConfirmOverride
   Description: Checks if the source of the unit price is from a supplier price list, if so
will prompt for confirmation of overriding if flag is set against purchase configuration.
   OperationID: ChangeUnitPriceConfirmOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnitPriceConfirmOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPriceConfirmOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUnitPriceConfirmOverride(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeUnitPriceConfirmOverride", {
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
   Summary: Invoke method ChangeQtyOption
   Description: This method is used when the QtyOption on the detail screen changes.
   OperationID: ChangeQtyOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQtyOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQtyOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeQtyOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeQtyOption", {
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
   Summary: Invoke method GetBasePartAndConfigType
   Description: Retrieve the based configured part and config type
   OperationID: GetBasePartAndConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartAndConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartAndConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBasePartAndConfigType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetBasePartAndConfigType", {
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
   Summary: Invoke method GetBasePartForConfig
   Description: This method will retrieve the base configured part number to be passed
to configuration entry
   OperationID: GetBasePartForConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBasePartForConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBasePartForConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBasePartForConfig(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetBasePartForConfig", {
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
   Summary: Invoke method GetPlantsForPart
   Description: Gets Plant for appropriate Part
   OperationID: GetPlantsForPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPlantsForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantsForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPlantsForPart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetPlantsForPart", {
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
   Summary: Invoke method PartStatusValidationMessages
   Description: The method is to be run on leave of the PartNum, Revision fields before the
GetPartInfo or Update methods are run.  This returns all the questions that
need to be asked before a part can be changed.
   OperationID: PartStatusValidationMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartStatusValidationMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartStatusValidationMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartStatusValidationMessages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/PartStatusValidationMessages", {
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
   Summary: Invoke method GetValidManufacturers
   Description: Return the valid Manufacturers set to a specific part.
   OperationID: GetValidManufacturers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValidManufacturers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidManufacturers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetValidManufacturers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetValidManufacturers", {
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
   Summary: Invoke method ChangeApproveSwitch
   Description: Invoke this method when the Approve switch on the summary screen changes.
   OperationID: ChangeApproveSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeApproveSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeApproveSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeApproveSwitch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeApproveSwitch", {
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
   Summary: Invoke method ChangedApproveSwitch
   Description: Invoke this method when the Approve switch has changed to True and we need to invoke the 'Approval' logic and the Supplier minimum value tests.
   OperationID: ChangedApproveSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedApproveSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedApproveSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedApproveSwitch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangedApproveSwitch", {
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
   Summary: Invoke method ChangeConfirmSwitch
   Description: Invoke this method when the Confirm switch on the summary screen changes.
   OperationID: ChangeConfirmSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConfirmSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConfirmSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeConfirmSwitch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeConfirmSwitch", {
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
   Summary: Invoke method ChangeCountry
   Description: Changes country
   OperationID: ChangeCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCountry(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeCountry", {
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
   Summary: Invoke method ChangeCurrencyCode
   Description: Run this method when the currency code changes on the poheader.
This method will pull in the exchange rate.
   OperationID: ChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeCurrencyCode", {
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
   Summary: Invoke method ChangePOTaxRegionCode
   Description: Change Tax Region Code
   OperationID: ChangePOTaxRegionCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOTaxRegionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOTaxRegionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOTaxRegionCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOTaxRegionCode", {
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
   Summary: Invoke method ChangePOType
   Description: This method should be invoked when the newPOType changes.
   OperationID: ChangePOType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOType", {
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
   Summary: Invoke method ChangePrcConNum
   Description: This method should be invoked when the PrcConNum changes. This method will validate
the vendorCnt and pull in the new default information.
   OperationID: ChangePrcConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePrcConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrcConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePrcConNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePrcConNum", {
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
   Summary: Invoke method ChangePrcConNumByName
   Description: This method should be invoked when the PrcConNum changes.This method will validate
the vendorCnt and pull in the new default information based on the contact's name.
   OperationID: ChangePrcConNumByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePrcConNumByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrcConNumByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePrcConNumByName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePrcConNumByName", {
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
   Summary: Invoke method ChangePrcConNumByNameOrNum
   Description: This method should be invoked when the PrcConNum changes.This method will validate
the vendorCnt and pull in the new default information based on the contact's num or name.
   OperationID: ChangePrcConNumByNameOrNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePrcConNumByNameOrNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrcConNumByNameOrNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePrcConNumByNameOrNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePrcConNumByNameOrNum", {
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
   Summary: Invoke method ChangePurPoint
   Description: Invoke this method to change the purchase point on the POHeader. This method
will validate the PP and pull in default information.
   OperationID: ChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePurPoint(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePurPoint", {
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
   Summary: Invoke method ChangeVendor
   Description: This method should be invoked when the vendor ID changes. This method will validate
the vendor and pull in the new default vendor information.
1. Validate Vendor ID / Vendor Num
2. check for inactive vendor
3. check Vendor for Approved flag
4. check item(s) for conficts with AprvVend
   OperationID: ChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeVendor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeVendor", {
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
   Summary: Invoke method CheckRateGrpCode
   Description: Update Quote Detail information when the Part Number is changed.
   OperationID: CheckRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRateGrpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckRateGrpCode", {
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
   Summary: Invoke method ChangedHeaderTaxManual
   Description: Method to call when the Manual Tax Flag has Changed from True to False.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangedHeaderTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedHeaderTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedHeaderTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedHeaderTaxManual(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangedHeaderTaxManual", {
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
   Summary: Invoke method ChangeHeaderTaxFixedAmount
   Description: Method to call when changing the fixed amount on a tax record.  Updates POHeaderTax
tax amounts based on the new fixed amount.
   OperationID: ChangeHeaderTaxFixedAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxFixedAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxFixedAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxFixedAmount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxFixedAmount", {
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
   Summary: Invoke method ChangeHeaderTaxTaxPercent
   Description: Method to call when changing the tax percent on a tax record.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangeHeaderTaxTaxPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxTaxPercent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxTaxPercent", {
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
   Summary: Invoke method ChangeHeaderTaxRateCode
   Description: Method to call when changing the tax percent on a tax record.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangeHeaderTaxRateCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxRateCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxRateCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxRateCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxRateCode", {
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
   Summary: Invoke method ChangeHeaderTaxRateCodeMaster
   Description: Method to call when changing the rate code on a tax record.  Validates the rate and tax code
   OperationID: ChangeHeaderTaxRateCodeMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxRateCodeMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxRateCodeMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxRateCodeMaster(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxRateCodeMaster", {
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
   Summary: Invoke method ChangeHeaderTaxReportableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates POHeaderTax
tax amounts based on the new taxable amount.
   OperationID: ChangeHeaderTaxReportableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxReportableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxReportableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxReportableAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxReportableAmt", {
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
   Summary: Invoke method ChangeHeaderTaxTaxableAmt
   Description: Method to call when changing the taxable amount on a tax record.  Updates POHeaderTax
tax amounts based on the new taxable amount.
   OperationID: ChangeHeaderTaxTaxableAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxableAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxableAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxTaxableAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxTaxableAmt", {
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
   Summary: Invoke method ChangeHeaderTaxTaxAmt
   Description: Method to call when changing the fixed tax amount on a tax record.  Updates POHeaderTax
tax amounts based on the new tax amount.
   OperationID: ChangeHeaderTaxTaxAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxTaxAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxTaxAmt", {
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
   Summary: Invoke method ChangeHeaderTaxTaxCode
   Description: Method to call when changing the tax code on a POHeader Tax record.  Validates the tax code and
updates POHeaderTax tax amounts based on the new tax code.
   OperationID: ChangeHeaderTaxTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxTaxCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxTaxCode", {
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
   Summary: Invoke method ChangeHeaderTaxTaxDeductable
   Description: Method to call when changing the tax deductable on a tax record.  Updates POHeaderTax
tax amounts based on the new tax percent.
   OperationID: ChangeHeaderTaxTaxDeductable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHeaderTaxTaxDeductable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHeaderTaxTaxDeductable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeHeaderTaxTaxDeductable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeHeaderTaxTaxDeductable", {
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
   Summary: Invoke method ChangeCurrencySwitch
   Description: Run this method when the currency toggle changes on the POHeadeMisc.
It will update the currency symbol.
   OperationID: ChangeCurrencySwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencySwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencySwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencySwitch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeCurrencySwitch", {
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
   Summary: Invoke method ChangePOHeadMiscAmt
   Description: Method to call when changing the miscellanous amount on a miscellaneous charge.
Updates the respective miscellanous charge table with default values based on the new amount.
   OperationID: ChangePOHeadMiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOHeadMiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOHeadMiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOHeadMiscAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOHeadMiscAmt", {
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
   Summary: Invoke method ChangePOHeadMiscCode
   Description: Run this method when the misc code is changed on the POHeadMisc.
It will recalaculate amounts.
   OperationID: ChangePOHeadMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOHeadMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOHeadMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOHeadMiscCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOHeadMiscCode", {
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
   Summary: Invoke method ChangePOHeadMiscPrcnt
   Description: Run this method when the percentage changes on the POHeadMisc.
It will recalaculate doc and base amounts.
   OperationID: ChangePOHeadMiscPrcnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOHeadMiscPrcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOHeadMiscPrcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOHeadMiscPrcnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOHeadMiscPrcnt", {
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
   Summary: Invoke method ChangePOMiscAmt
   Description: Method to call when changing the miscellanous amount on a miscellaneous charge.
Updates the respective miscellanous charge table with default values based on the new amount.
   OperationID: ChangePOMiscAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOMiscAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOMiscAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOMiscAmt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOMiscAmt", {
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
   Summary: Invoke method ChangePOMiscCode
   Description: Run this method when the misc code is changed on the POMisc.
It will recalaculate amounts.
   OperationID: ChangePOMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOMiscCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOMiscCode", {
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
   Summary: Invoke method ChangePoMiscCurrSwitch
   Description: Run this method when the currency toggle changes on the POMisc.
It will update the currency symbol and recalaculate doc and base amounts.
   OperationID: ChangePoMiscCurrSwitch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePoMiscCurrSwitch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePoMiscCurrSwitch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePoMiscCurrSwitch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePoMiscCurrSwitch", {
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
   Summary: Invoke method ChangePOMiscPrcnt
   Description: Run this method when the percentage changes on the POMisc.
It will recalaculate doc and base amounts.
   OperationID: ChangePOMiscPrcnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOMiscPrcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOMiscPrcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePOMiscPrcnt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePOMiscPrcnt", {
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
   Summary: Invoke method ChangeRelAssemblySeq
   Description: Invoke when assembly on the release sheet changes. It will validate the release and
zero out the JobSeq.
   OperationID: ChangeRelAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelAssemblySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelAssemblySeq", {
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
   Summary: Invoke method ChangeRelGlbCompany
   Description: This method should be called when the GlbCompany field on a po release changes.
It will populate default values in PORel based on the new GlbCompany value.
   OperationID: ChangeRelGlbCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelGlbCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelGlbCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelGlbCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelGlbCompany", {
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
   Summary: Invoke method ChangeRelGlbPlant
   Description: This method should be called when the GlbPlant field on a po release changes.
It will populate default values in PORel based on the new GlbPlant value.
   OperationID: ChangeRelGlbPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelGlbPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelGlbPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelGlbPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelGlbPlant", {
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
   Summary: Invoke method ChangeRelGlbWarehouse
   Description: This method should be called when the GlbWarehouse field on a po release changes.
It will populate default values in PORel based on the new GlbWarehouse value.
   OperationID: ChangeRelGlbWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelGlbWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelGlbWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelGlbWarehouse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelGlbWarehouse", {
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
   Summary: Invoke method ChangeRelIUM
   Description: Call this method when the IUM changes on the PORel.
   OperationID: ChangeRelIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelIUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelIUM", {
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
   Summary: Invoke method ChangeRelJobNum
   Description: /// Purpose: Invoke after the jobnumber has changed either on the release sheet .
///
   OperationID: ChangeRelJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelJobNum", {
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
   Summary: Invoke method ChangeRelJobSeq
   Description: Invoke when Job/mtl sequence on the release sheet changes. It will validate the release and
zero out the JobSeq.
   OperationID: ChangeRelJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelJobSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelJobSeq", {
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
   Summary: Invoke method ChangeRelJobSeqWarning
   Description: Gets specified material or operation record and changes the warning message.
   OperationID: ChangeRelJobSeqWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelJobSeqWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelJobSeqWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelJobSeqWarning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelJobSeqWarning", {
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
   Summary: Invoke method ChangeBTOOrderLineWarning
   Description: Check Order detail is valid and issue a error / warning accordingly.
   OperationID: ChangeBTOOrderLineWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBTOOrderLineWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBTOOrderLineWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBTOOrderLineWarning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeBTOOrderLineWarning", {
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
   Summary: Invoke method ChangeRelMangCust
   Description: Run this method when MangCustID on the release changes.
   OperationID: ChangeRelMangCust
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelMangCust_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelMangCust_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelMangCust(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelMangCust", {
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
   Summary: Invoke method ChangeRelOrderLine
   Description: Call this method when the OrderLine changes on the PORel.
   OperationID: ChangeRelOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelOrderLine(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelOrderLine", {
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
   Summary: Invoke method ChangeRelOrderNum
   Description: Call this method when the OrderNum changes on the PORel.
   OperationID: ChangeRelOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelOrderNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelOrderNum", {
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
   Summary: Invoke method ChangeRelOrderRelNum
   Description: Call this method when the OrderRelNum changes on the PORel.
   OperationID: ChangeRelOrderRelNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelOrderRelNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelOrderRelNum", {
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
   Summary: Invoke method ChangeRelOurQty
   Description: This should be run after OurQty (PORel.XRelQty) changed on the PO release.
   OperationID: ChangeRelOurQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelOurQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelOurQty", {
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
   Summary: Invoke method ChangeRelPlant
   Description: Call this method when the Plant is changed on PORel.
   OperationID: ChangeRelPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelPlant(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelPlant", {
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
   Summary: Invoke method ChangeRelPUM
   Description: Call this method when the PUM changes on the PORel.
   OperationID: ChangeRelPUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelPUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelPUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelPUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelPUM", {
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
   Summary: Invoke method ChangeRelTaxExempt
   Description: Call this method when changing the Tax Exempt to toggle Taxable Flag
   OperationID: ChangeRelTaxExempt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelTaxExempt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelTaxExempt", {
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
   Summary: Invoke method ChangeRelVendQty
   Description: This should be run after VendorQty (PORel.RelQty) changed on the PO release.
   OperationID: ChangeRelVendQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelVendQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelVendQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRelVendQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeRelVendQty", {
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
   Summary: Invoke method ChangePORelContract
   Description: Call this method when the PORel.ContractID changes.
   OperationID: ChangePORelContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePORelContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePORelContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePORelContract(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangePORelContract", {
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
   Summary: Invoke method ChangeTranType
   Description: Call this method when the TranType (LineType) changes on the POREL.
ExpAccount will change
   OperationID: ChangeTranType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangeTranType", {
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
   Summary: Invoke method CheckComplianceFail
   Description: Check for every release of the PO if it is compliant.
   OperationID: CheckComplianceFail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckComplianceFail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckComplianceFail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckComplianceFail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckComplianceFail", {
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
   Summary: Invoke method CheckProjectID
   Description: Validate Projec ID value
   OperationID: CheckProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckProjectID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/CheckProjectID", {
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
   Summary: Invoke method GetDefaultGLAccount
   Description: Get Default GL Account.
<param name="pPONum">PO Number</param><param name="pPOLine">PO Line number</param><param name="pPORelNum">PO Release number</param><param name="ds" type="Epicor.Mfg.BO.PODataSet">The Purchase Order data set </param>
   OperationID: GetDefaultGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultGLAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/GetDefaultGLAccount", {
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
   Summary: Invoke method ChangedTaxManual
   Description: Method to call when changing the manual tax calculation value on a line tax record.  Updates PORelTax
tax amounts based on the new value of the flag back to system-calculated tax.
   OperationID: ChangedTaxManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedTaxManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedTaxManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangedTaxManual(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.POSvc/ChangedTaxManual", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PODetailAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailInspRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PODetailInspRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailMiscTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PODetailMiscTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PODetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PODetailTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PODetailTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeadMiscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POHeadMiscRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POHeaderAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POHeaderListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderMiscTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POHeaderMiscTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POHeaderRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POHeaderTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POHeaderTaxRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POMiscRow{
   "odatametadata":string,
   "value":Erp_Tablesets_POMiscRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PORelAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PORelRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PORelTGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelTaxRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PORelTaxRow[],
}

export interface Erp_Tablesets_PODetailAttchRow{
   "Company":string,
   "PONUM":number,
   "POLine":number,
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

export interface Erp_Tablesets_PODetailInspRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase order number that the detail line item is linked to.  */  
   "PONUM":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "POLine":number,
      /**  A sequence number that uniquely identifies the PartMtlInsp record within the Part material  */  
   "PlanSeq":number,
      /**  The inspection plan part number (configurator part number).  */  
   "InspPlanPartNum":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   "SpecID":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "SpecHedDescription":string,
   "BitFlag":number,
   "InspPlanDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PODetailMiscTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Purchase order that this release record is related to.  */  
   "PONUM":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Sequence Number  */  
   "SeqNum":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  ** NOT USED TO BE DROPPED 10.2 **  */  
   "MiscCode":string,
      /**  ReportableAmt  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  User ID of the user who created the record  */  
   "CreatedBy":string,
      /**  The date/ time that the record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date/ time that the record was last changed  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  Indicates if this row was created as part of the migration process.  */  
   "Migrated":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Desc. Collection Type  */  
   "DescCollectionType":string,
   "DocScrDedTaxAmt":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "DocScrFixedAmount":number,
   "Rpt1ScrFixedAmount":number,
   "Rpt2ScrFixedAmount":number,
   "Rpt3ScrFixedAmount":number,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PODetailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  */  
   "OpenLine":boolean,
      /**   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  */  
   "VoidLine":boolean,
      /**  Purchase order number that the detail line item is linked to.  */  
   "PONUM":number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   "POLine":number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   "LineDesc":string,
      /**  (Our) Unit Of Measure.  */  
   "IUM":string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   "UnitCost":number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   "DocUnitCost":number,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  */  
   "OrderQty":number,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  */  
   "XOrderQty":number,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Purchasing UOM  */  
   "PUM":string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "CostPerCode":string,
      /**  OUR internal Part number for this item.  */  
   "PartNum":string,
      /**  Supplier Part Number  */  
   "VenPartNum":string,
      /**  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  */  
   "CommentText":string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   "ClassID":string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   "VendorNum":number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   "AdvancePayBal":number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   "DocAdvancePayBal":number,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   "Confirmed":boolean,
      /**  Indicates this line has a pending date change  */  
   "DateChgReq":boolean,
      /**  Indicates this line has a pending qty change  */  
   "QtyChgReq":boolean,
      /**  Requested pending partnumber change  */  
   "PartNumChgReq":string,
      /**  Requested pending revision change  */  
   "RevisionNumChgReq":string,
      /**  Date Supplier Confirmed the PO  */  
   "ConfirmDate":string,
      /**  Can be "web" or "client"  */  
   "ConfirmVia":string,
      /**  Requested Price change.  SRM  */  
   "PrcChgReq":number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   "PurchCode":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Linked to sales order line.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Is this line active on the Contract Purchase Order?  */  
   "ContractActive":boolean,
      /**  Quantity for this Contract Purchase Order Line.  */  
   "ContractQty":number,
      /**  Unit Price for this Contract Purchase Order Line.  */  
   "ContractUnitCost":number,
      /**  Document Unit Price for this Contract Purchase Order Line.  */  
   "ContractDocUnitCost":number,
      /**  Advanced Payments Balance in Rpt1 currency.  */  
   "Rpt1AdvancePayBal":number,
      /**  Advanced Payments Balance in Rpt2 currency.  */  
   "Rpt2AdvancePayBal":number,
      /**  Advanced Payments Balance in Rpt3 currency.  */  
   "Rpt3AdvancePayBal":number,
      /**  Unit price in the vendors unit of measure and Rpt1 currency.  */  
   "Rpt1UnitCost":number,
      /**  Unit price in the vendors unit of measure and Rpt2 currency.  */  
   "Rpt2UnitCost":number,
      /**  Unit price in the vendors unit of measure and Rpt3 currency.  */  
   "Rpt3UnitCost":number,
      /**  Unit Of Measure of the ContractQty.  */  
   "ContractQtyUOM":string,
      /**  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  */  
   "Rpt1ContractUnitCost":number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  */  
   "Rpt2ContractUnitCost":number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  */  
   "Rpt3ContractUnitCost":number,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  */  
   "BaseQty":number,
      /**   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   "BaseUOM":string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderNum":number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderLine":number,
      /**   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   "VendorPartOpts":string,
      /**   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   "MfgPartOpts":string,
      /**   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  */  
   "SubPartOpts":string,
      /**  Manufacturer Unique ID  */  
   "MfgNum":number,
      /**  Manufacturer's Part Number.  */  
   "MfgPartNum":string,
      /**  Substitute Part Number  */  
   "SubPartNum":string,
      /**   Substitute Part Type
O = Original
S = Substitute  */  
   "SubPartType":string,
      /**   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   "ConfigUnitCost":number,
      /**  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   "ConfigBaseUnitCost":number,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   "ConvOverRide":boolean,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   "BasePartNum":string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   "BaseRevisionNum":string,
      /**  Direction  */  
   "Direction":string,
      /**  Per  */  
   "Per":string,
      /**  MaintainPricingUnits  */  
   "MaintainPricingUnits":boolean,
      /**  OverrideConversion  */  
   "OverrideConversion":boolean,
      /**  RowsManualFactor  */  
   "RowsManualFactor":boolean,
      /**  KeepRowsManualFactorTmp  */  
   "KeepRowsManualFactorTmp":boolean,
      /**  ShipToSupplierDate  */  
   "ShipToSupplierDate":string,
      /**  Factor  */  
   "Factor":number,
      /**  PricingQty  */  
   "PricingQty":number,
      /**  PricingUnitPrice  */  
   "PricingUnitPrice":number,
      /**  UOM  */  
   "UOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  DocPricingUnitPrice  */  
   "DocPricingUnitPrice":number,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   "OverridePriceList":boolean,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   "QtyOption":string,
      /**  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  */  
   "OrigComment":string,
      /**  SmartString  */  
   "SmartString":string,
      /**  SmartStringProcessed  */  
   "SmartStringProcessed":boolean,
      /**  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  */  
   "DueDate":string,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   "LinkToContract":boolean,
      /**  SelCurrPricingUnitPrice  */  
   "SelCurrPricingUnitPrice":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date and time that the record was last changed  */  
   "ChangeDate":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   "TaxCatID":string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   "NoTaxRecalc":boolean,
      /**  Unit price in the vendors unit of measure inclusive of tax in base currency.  */  
   "InUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in document currency.  */  
   "DocInUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   "Rpt1InUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   "Rpt2InUnitCost":number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   "Rpt3InUnitCost":number,
      /**  Advanced Payments Balance inclusive of tax in base currency.  */  
   "InAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in document currency.  */  
   "DocInAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in Rpt1 currency.  */  
   "Rpt1InAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in Rpt2 currency.  */  
   "Rpt2InAdvancePayBal":number,
      /**  Advanced Payments Balance inclusive of tax in Rpt3 currency.  */  
   "Rpt3InAdvancePayBal":number,
      /**  Contract unit cost inclusive of tax in base currency.  */  
   "InContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in document currency.  */  
   "DocInContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in Rpt1 currency.  */  
   "Rpt1InContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in Rpt2 currency.  */  
   "Rpt2InContractUnitCost":number,
      /**  Contract unit cost inclusive of tax in Rpt3 currency.  */  
   "Rpt3InContractUnitCost":number,
      /**  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  */  
   "DocExtCost":number,
      /**  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  */  
   "ExtCost":number,
      /**  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  */  
   "Rpt1ExtCost":number,
      /**  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  */  
   "Rpt2ExtCost":number,
      /**  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  */  
   "Rpt3ExtCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  */  
   "DocMiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  */  
   "MiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  */  
   "Rpt1MiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  */  
   "Rpt2MiscCost":number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  */  
   "Rpt3MiscCost":number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   "TotalTax":number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   "DocTotalTax":number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   "Rpt1TotalTax":number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   "Rpt2TotalTax":number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   "Rpt3TotalTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   "TotalSATax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   "DocTotalSATax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalSATax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalSATax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalSATax":number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   "TotalDedTax":number,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   "DocTotalDedTax":number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalDedTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalDedTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalDedTax":number,
      /**  CommodityCode  */  
   "CommodityCode":string,
      /**  CNBonded  */  
   "CNBonded":boolean,
      /**  Acknowledge code received from EDI  */  
   "EDIAckCode":string,
      /**  Additional comments to send with Acknowledge  */  
   "EDIAckComment":string,
      /**  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  */  
   "AskRefCode":boolean,
   "CalcAssemblySeq":number,
   "CalcDocTotalCost":number,
   "CalcDueDate":string,
   "CalcJobNum":string,
   "CalcJobSeq":number,
   "CalcJobSeqType":string,
   "calcLeadTime":number,
   "CalcMangCustID":string,
   "CalcMangCustName":string,
   "CalcMangCustNum":number,
   "CalcMfg":string,
   "CalcMfgPart":string,
   "calcMinOrderQty":number,
   "CalcOurQty":number,
   "calcPartPUM":string,
      /**  purchasing factor  */  
   "CalcPurchasingFactor":number,
   "CalcPurchasingFactorDirection":string,
   "CalcTotalCost":number,
   "CalcTranType":string,
   "CalcVendQty":number,
   "Configured":string,
   "ConsolidatedPO":boolean,
   "ContractOrder":boolean,
      /**  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   "CostPerCodeContract":string,
   "CPFactor":number,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DelPoSug":boolean,
   "DisablePartRevBtn":boolean,
      /**  Display Account Description.  */  
   "DispAcctDescription":string,
      /**  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  */  
   "DispExpAccount":string,
   "DisplaySymbol":string,
   "DocDisplaySymbol":string,
   "DocScrUnitCost":number,
      /**  False if vendor or class requires inspection, otherwise true.  */  
   "EnableRcvInspectionReq":boolean,
      /**  The Chart ID component of the default G/L account.  */  
   "ExpChart":string,
      /**  The Division Component of the default expence G/L account.  */  
   "ExpDivision":string,
      /**  The Department component of the default G/L account.  */  
   "ExpGLDept":string,
   "FromPOSugChg":boolean,
   "LinkedSOConfig":boolean,
   "MultiRel":boolean,
   "NonMasterPart":boolean,
   "OpCode":string,
   "PartQtyBearing":boolean,
   "POHeaderApprove":boolean,
      /**  True if there is only one release and it's open.  */  
   "PORelOneOpenRelease":boolean,
   "PriceBrkBTNSensitive":boolean,
      /**  Reference Code Description  */  
   "RefCodeDesc":string,
      /**  Reference Code Status  */  
   "RefCodeStatus":string,
      /**  Link to the related code in GlRefCod.RefCode  */  
   "ReferenceCode":string,
   "Rpt1CalcTotalCost":number,
   "Rpt1ScrUnitCost":number,
   "Rpt2CalcTotalCost":number,
   "Rpt2ScrUnitCost":number,
   "Rpt3CalcTotalCost":number,
   "Rpt3ScrUnitCost":number,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   "ScrUnitCost":number,
   "SetCheveron":boolean,
   "SubAvail":boolean,
   "UpdateRelRecords":boolean,
      /**  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  */  
   "UpdateRelTaxable":boolean,
      /**  Purchase Point used in the Supplier Tracker.  */  
   "VendPurPoint":string,
   "AllowPORecon":boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   "EnableDynAttrButton":boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   "AttributeQtyMismatch":boolean,
   "CalcJobMtlSeq":number,
   "CalcJobOprSeq":number,
      /**  Flag to indicate the current PO Line has at least one Buy To Order Release  */  
   "HasBuyToOrderRelease":boolean,
      /**  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  */  
   "LineAmtCalcd":boolean,
   "BitFlag":number,
   "ClassInactive":boolean,
   "ClassDescription":string,
   "CommodityCodeDescription":string,
   "GlPurchPurchDesc":string,
   "MfgNumMfgID":string,
   "MfgNumName":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumAttrClassID":string,
   "PONUMCurrencyCode":string,
   "PONUMOrderDate":string,
   "PONUMInPrice":boolean,
   "PONUMShipName":string,
   "PONUMShipToConName":string,
   "TaxCatIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "DeliveryInstructions_c":string,
}

export interface Erp_Tablesets_PODetailTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Purchase order number.  */  
   "PONum":number,
      /**  The line # of PODetail record  */  
   "POLine":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  Reportable Amount  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  User ID of the user who created the record  */  
   "CreatedBy":string,
      /**  The date / time that the record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date/ time that the record was last changed  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  ResolutionNum  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "DocScrDedTaxAmt":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "DocScrFixedAmount":number,
   "Rpt1ScrFixedAmount":number,
   "Rpt2ScrFixedAmount":number,
   "Rpt3ScrFixedAmount":number,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_POHeadMiscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   "PONum":number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  */  
   "POLine":number,
      /**  Sequence Number  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "MiscAmt":number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "DocMiscAmt":number,
      /**  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  */  
   "Taxable":boolean,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "InvoicedAmt":number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "DocInvoicedAmt":number,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  */  
   "OrderSeqNum":number,
      /**  Linked to sales order misc charge.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoicedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoicedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoicedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "InMiscAmt":number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "DocInMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InMiscAmt":number,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "InInvoiceAmt":number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "DocInInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InInvoiceAmt":number,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   "NoTaxRecalc":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrencySymbol":string,
   "DocCurrencySymbol":string,
   "POHeaderApprove":boolean,
   "Rpt1ScrMiscAmt":number,
   "Rpt2ScrMiscAmt":number,
   "Rpt3ScrMiscAmt":number,
   "ScrDocMiscAmt":number,
   "ScrMiscAmt":number,
      /**  Description of Tax ID  */  
   "TaxIDDescription":string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   "DocTotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   "DocTotalSATax":number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   "DocTotalTax":number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   "Rpt1TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   "Rpt2TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   "Rpt3TotalTax":number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   "TotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   "TotalSATax":number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   "TotalTax":number,
   "BitFlag":number,
   "MiscCodeTaxCatID":string,
   "MiscCodeLCAmount":number,
   "MiscCodeLCCurrencyCode":string,
   "MiscCodeLCDisburseMethod":string,
   "MiscCodeDescription":string,
   "PONumInPrice":boolean,
   "PONumShipToConName":string,
   "PONumShipName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_POHeaderAttchRow{
   "Company":string,
   "PONum":number,
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

export interface Erp_Tablesets_POHeaderListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  */  
   "OpenOrder":boolean,
      /**  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  */  
   "VoidOrder":boolean,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   "PONum":number,
      /**  Entry Person  */  
   "EntryPerson":string,
      /**  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  */  
   "OrderDate":string,
      /**  Incoterms  */  
   "FOB":string,
      /**  Ship Via Code  */  
   "ShipViaCode":string,
      /**  Terms  */  
   "TermsCode":string,
      /**  defaults from the company file.  */  
   "ShipName":string,
      /**  First adress line  */  
   "ShipAddress1":string,
      /**  Second address line  */  
   "ShipAddress2":string,
      /**  Third address line  */  
   "ShipAddress3":string,
      /**  City portion of the address  */  
   "ShipCity":string,
      /**  Statee portion of the address  */  
   "ShipState":string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   "ShipCountry":string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   "OrderHeld":boolean,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "ShipToConName":string,
      /**  Indicates if the PO can be printed. Print functions are not available if this is = No.  */  
   "ReadyToPrint":boolean,
   "VendorVendorID":string,
   "VendorName":string,
   "BuyerIDName":string,
   "FOBDescription":string,
      /**  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  */  
   "ApprovedDate":string,
      /**  The BuyerID  that approved the PO. (See ApprovedDate for related info)  */  
   "ApprovedBy":string,
   "ShipViaCodeDescription":string,
   "TermsCodeDescription":string,
      /**   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  */  
   "Approve":boolean,
      /**   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  */  
   "ApprovalStatus":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  */  
   "POType":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_POHeaderMiscTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  Sequence Number  */  
   "SeqNum":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   "MiscCode":string,
      /**  ReportableAmt  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  User ID o fthe user who created the record  */  
   "CreatedBy":string,
      /**  The date / time that the record was created  */  
   "CreatedOn":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date/ time that the record was last changed  */  
   "ChangedOn":string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  Indicates if this row was created as part of the migration process.  */  
   "Migrated":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "DocScrDedTaxAmt":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "DocScrFixedAmount":number,
   "Rpt1ScrFixedAmount":number,
   "Rpt2ScrFixedAmount":number,
   "Rpt3ScrFixedAmount":number,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_POHeaderRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  */  
   "OpenOrder":boolean,
      /**  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  */  
   "VoidOrder":boolean,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   "PONum":number,
      /**  Entry Person  */  
   "EntryPerson":string,
      /**  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  */  
   "OrderDate":string,
      /**  Incoterms  */  
   "FOB":string,
      /**  Ship Via Code  */  
   "ShipViaCode":string,
      /**  Terms  */  
   "TermsCode":string,
      /**  defaults from the company file.  */  
   "ShipName":string,
      /**  First adress line  */  
   "ShipAddress1":string,
      /**  Second address line  */  
   "ShipAddress2":string,
      /**  Third address line  */  
   "ShipAddress3":string,
      /**  City portion of the address  */  
   "ShipCity":string,
      /**  Statee portion of the address  */  
   "ShipState":string,
      /**  Postal code or Zip code portion of the address  */  
   "ShipZIP":string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   "ShipCountry":string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   "BuyerID":string,
      /**  The freight charge is to be paid by the vendor.  */  
   "FreightPP":boolean,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  */  
   "PrcConNum":number,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   "VendorNum":number,
      /**  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
      /**  Contains comments about over all  purchase order. These will be printed on the purchase order.  */  
   "CommentText":string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   "OrderHeld":boolean,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   "ShipToConName":string,
      /**  Indicates if the PO can be printed. Print functions are not available if this is = No.  */  
   "ReadyToPrint":boolean,
      /**  N = New, C = Change Order  */  
   "PrintAs":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   "ShipCountryNum":number,
      /**  This field indicates if the system should generate purchase order booking records. Booking tables are used to track changes to POheader.  */  
   "LogChanges":boolean,
      /**  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  */  
   "ApprovedDate":string,
      /**  The BuyerID  that approved the PO. (See ApprovedDate for related info)  */  
   "ApprovedBy":string,
      /**   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  */  
   "Approve":boolean,
      /**   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  */  
   "ApprovalStatus":string,
      /**   An internally used field that represents the total amount of the PO (in base currency) captured the last time the po was approved/rejected.  Note: this only pertains to PO that required approval in the first place otherwise it's zero.  The limit checking process will compare PO amounts to the greater of the buyers limit or this amount. Basically, if the PO was already approved once for a specific amount then it should not require subsequent approval until that amount is exceeded.
Note: This also contains the PO amount if it was rejected. In this case, the PO remains as rejected until they reduce the PO amount.  */  
   "ApprovedAmount":number,
      /**  Indicates the Supplier will respond via Suppliers workbench  */  
   "PostToWeb":boolean,
      /**  Date Buyer posted the PO  */  
   "PostDate":string,
      /**  Vendor reference number.  */  
   "VendorRefNum":string,
      /**  Indicated this PO requires a confirmation.  This would default yes for any Web Vendor  */  
   "ConfirmReq":boolean,
      /**  Indicated Supplier Confirmed the PO  */  
   "Confirmed":boolean,
      /**   Indicates if the Supplier has confirmed that they intend to fill the Order, and that it will be done through Supplier Connect("web"), 
phoned in a confirmation and clicked on the Confirmed checkbox in Epicor ("client"), or they clicked on the "Reject" checkbox in Supplier Connect("rejected").  */  
   "ConfirmVia":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  Linked to sales order.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Cross reference PO number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefPONum":string,
      /**  Consolidated PO flag.  Used in Consolidated Purchasing.  */  
   "ConsolidatedPO":boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Is this Purchase Order a Contract Purchase Order?  */  
   "ContractOrder":boolean,
      /**  The date the Contract Purchase Order is active.  */  
   "ContractStartDate":string,
      /**  The date the Contract Purchase Order expires.  */  
   "ContractEndDate":string,
      /**  Print Header Address flag  */  
   "PrintHeaderAddress":boolean,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  */  
   "POType":string,
      /**  Letter of Credit ID.  */  
   "APLOCID":string,
      /**  Transaction Document for the record.  */  
   "TranDocTypeID":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  ICPOLocked  */  
   "ICPOLocked":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Specifies the date by which you need to receive the whole Purchase Order. If you set the Due Date before create lines and releases, it will act as a default value when adding new lines/releases.  */  
   "DueDate":string,
      /**  Specifies the date on which the supplier has promised to ship the whole Purchase Order. If you set the Promise Date before create lines and releases, it will act as a default value when adding releases.  */  
   "PromiseDate":string,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date and time that the record was last changed.  */  
   "ChangeDate":string,
      /**  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  */  
   "POTaxReadyToProcess":boolean,
      /**  The Tax Liability for this Purchase Order  */  
   "TaxRegionCode":string,
      /**  Tax Point  */  
   "TaxPoint":string,
      /**  Date Used to calculate Tax Rates  */  
   "TaxRateDate":string,
      /**  Total Tax amount for this PO in base currency, Totals the TaxAmt from the POTax records of this purchase order  */  
   "TotalTax":number,
      /**  Total Tax amount for this PO in document currency, Totals the DocTaxAmt from the POTax records of this purchase order  */  
   "DocTotalTax":number,
      /**  Total Tax amount for this PO in Rpt1 currency, Totals the Rpt1TaxAmt from the POTax records of this purchase order  */  
   "Rpt1TotalTax":number,
      /**  Total Tax amount for this PO in Rpt2 currency, Totals the Rpt2TaxAmt from the POTax records of this purchase order  */  
   "Rpt2TotalTax":number,
      /**  Total Tax amount for this PO in Rpt3 currency, Totals the Rpt3TaxAmt from the POTax records of this purchase order  */  
   "Rpt3TotalTax":number,
      /**  Total Order Withholding Taxes in base currency  */  
   "TotalWhTax":number,
      /**  Total Order Withholding Taxes in document currency  */  
   "DocTotalWhTax":number,
      /**  Total Order Withholding Taxes in Rpt1 currency  */  
   "Rpt1TotalWhTax":number,
      /**  Total Order Withholding Taxes in Rpt2 currency  */  
   "Rpt2TotalWhTax":number,
      /**  Total Order Withholding Taxes in Rpt3 currency  */  
   "Rpt3TotalWhTax":number,
      /**  Total Order Self Assessed Taxes in base currency.  */  
   "TotalSATax":number,
      /**  Total Order Self Assessed Taxes in document currency.  */  
   "DocTotalSATax":number,
      /**  Total Order Self Assessed Taxes in Rpt1 currency.  */  
   "Rpt1TotalSATax":number,
      /**  Total Order Self Assessed Taxes in Rpt2 currency.  */  
   "Rpt2TotalSATax":number,
      /**  Total Order Self Assessed Taxes in Rpt3 currency.  */  
   "Rpt3TotalSATax":number,
      /**  Indicates that the tax is included in the unit price  */  
   "InPrice":boolean,
      /**  This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   "HdrTaxNoUpdt":boolean,
      /**  Tax Rate Group Code - FUTUREUSE  */  
   "TaxRateGrpCode":string,
      /**  Total deductable tax amount in base currency.  */  
   "TotalDedTax":number,
      /**  Total deductable tax amount in document currency.  */  
   "DocTotalDedTax":number,
      /**  Total deductable tax amount in Rpt1 currency.  */  
   "Rpt1TotalDedTax":number,
      /**  Total deductable tax amount in Rpt2 currency.  */  
   "Rpt2TotalDedTax":number,
      /**  Total deductable tax amount in Rpt3 currency.  */  
   "Rpt3TotalDedTax":number,
      /**  Total charge amount for the PO in base currency,  This is the sum of PODetail.ExtCost for non voided lines.  */  
   "TotalCharges":number,
      /**  Total amount for all miscellaneous charges associated to this PO in base currency.  This is the sum of POMisc.MiscAmt.  */  
   "TotalMiscCharges":number,
      /**  Total amount for the PO in base currency.  This is the sum of POMisc.MiscAmt + PODetail.ExtCost + POHeader.TotalTax.  */  
   "TotalOrder":number,
      /**  Total charge amount for the PO in document currency,  This is the sum of PODetail.DocExtCost for non voided lines.  */  
   "DocTotalCharges":number,
      /**  Total amount for all miscellaneous charges associated to this PO in document currency.  This is the sum of POMisc.DocMiscAmt.  */  
   "DocTotalMisc":number,
      /**  Total amount for the PO in document currency.  This is the sum of POMisc.DocMiscAmt + PODetail.DocExtCost + POHeader.DocTotalTax.  */  
   "DocTotalOrder":number,
      /**  Total charge amount for the PO in Rpt1 currency,  This is the sum of PODetail.Rpt1ExtCost for non voided lines.  */  
   "Rpt1TotalCharges":number,
      /**  Total charge amount for the PO in Rpt2 currency,  This is the sum of PODetail.Rpt2ExtCost for non voided lines.  */  
   "Rpt2TotalCharges":number,
      /**  Total charge amount for the PO in Rpt3 currency,  This is the sum of PODetail.Rpt3ExtCost for non voided lines.  */  
   "Rpt3TotalCharges":number,
      /**  Total amount for all miscellaneous charges associated to this PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt.  */  
   "Rpt1TotalMiscCharges":number,
      /**  Total amount for all miscellaneous charges associated to this PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt.  */  
   "Rpt2TotalMiscCharges":number,
      /**  Total amount for all miscellaneous charges associated to this PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt.  */  
   "Rpt3TotalMiscCharges":number,
      /**  Total amount for the PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt + PODetail.Rpt1ExtCost + POHeader.Rpt1TotalTax.  */  
   "Rpt1TotalOrder":number,
      /**  Total amount for the PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt + PODetail.Rpt2ExtCost + POHeader.Rpt2TotalTax.  */  
   "Rpt2TotalOrder":number,
      /**  Total amount for the PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt + PODetail.Rpt3ExtCost + POHeader.Rpt3TotalTax.  */  
   "Rpt3TotalOrder":number,
      /**  APTaxRoundOption  */  
   "APTaxRoundOption":number,
      /**  CNBonded  */  
   "CNBonded":boolean,
      /**  EDI Revision number that marks changes in the purchase order since the last time the purchase order was sent.  */  
   "EDIRevNum":number,
      /**  Flag used to mark the Purchase Order as posted to EDI  */  
   "EDIPosted":boolean,
      /**  Date when the PO was last acknowledge from EDI Portal  */  
   "EDIPostedDate":string,
      /**  Date when the PO was last acknowledge from EDI Portal  */  
   "EDIAckDate":string,
      /**  Temporarily stores the return message from the PO approval process  */  
   "ApproveMessage":string,
      /**  Used when switching the Vendor and need to prompt if the user wants to recalculate unit costs.  */  
   "RecalcUnitCosts":boolean,
   "RuleCode":number,
   "UpdateDtlAndRelRecords":boolean,
   "VendCntFaxNum":string,
   "VendCntPhoneNumber":string,
   "ApproveChkBxSensitive":boolean,
   "BaseCurrencyID":string,
   "ConfirmChkBxSensitive":boolean,
      /**  Flag for UI to know when to Enable/Disable the SupplierID field in POEntry  */  
   "EnableSupplierID":boolean,
      /**  True is there are lines for this PO  */  
   "HasLines":boolean,
   "HoldChkBxSensitive":boolean,
   "MassPrntChkBxSensitive":boolean,
   "RefCodeCurrSymbol":string,
      /**  The formatted vendor address  */  
   "VendAddrFormat":string,
   "EDIEnable":boolean,
   "BitFlag":number,
   "APLOCDescription":string,
   "BuyerIDName":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeCurrencyID":string,
   "FOBDescription":string,
   "RateGrpDescription":string,
   "ShipCountryNumDescription":string,
   "ShipViaCodeInactive":boolean,
   "ShipViaCodeDescription":string,
   "ShipViaCodeWebDesc":string,
   "TaxRegionCodeDescription":string,
   "TermsCodeDescription":string,
   "VendorVendorID":string,
   "VendorZIP":string,
   "VendorDefaultFOB":string,
   "VendorCity":string,
   "VendorName":string,
   "VendorCountry":string,
   "VendorAddress3":string,
   "VendorTermsCode":string,
   "VendorAddress1":string,
   "VendorAddress2":string,
   "VendorCurrencyCode":string,
   "VendorState":string,
   "VendorEDISupplier":boolean,
   "VendorCntName":string,
   "VendorCntEmailAddress":string,
   "VendorCntPhoneNum":string,
   "VendorCntFaxNum":string,
   "VendorPPAddress3":string,
   "VendorPPCountry":string,
   "VendorPPZip":string,
   "VendorPPState":string,
   "VendorPPAddress1":string,
   "VendorPPName":string,
   "VendorPPPrimPCon":number,
   "VendorPPAddress2":string,
   "VendorPPCity":string,
   "XbSystAllowLinkedPOChg":boolean,
   "XbSystPOUserInt2Label":string,
   "XbSystPOUserDate3Label":string,
   "XbSystPOUserChar3Label":string,
   "XbSystPOUserChar4Label":string,
   "XbSystPOUserChar2Label":string,
   "XbSystPOUserDate2Label":string,
   "XbSystPOUserInt1Label":string,
   "XbSystPOUserDec1Label":string,
   "XbSystPOUserDec2Label":string,
   "XbSystPOUserDate4Label":string,
   "XbSystPOUserDate1Label":string,
   "XbSystPOUserChar1Label":string,
   "XbSystDisableOverridePriceListOption":boolean,
   "XbSystPOTaxCalculate":boolean,
   "XbSystAPTaxLnLevel":boolean,
      /**  RowMod  */  
   "RowMod":string,
   "UD_SysRevID":string,
   "PrePaymentFlag_c":boolean,
   "PrePaymentTerms_c":string,
   "ProductFamily_c":string,
   "VendorConfirmationNo_c":string,
   "POTerms_c":string,
}

export interface Erp_Tablesets_POHeaderTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   "PONum":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last changed (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  Collection Type  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution Date  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  TextCode  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  flag to indicate if this record is used only to total detail records,  */  
   "SummaryOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BaseCurrSymbol":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrSymbol":string,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "EnableSuperGRate":boolean,
   "Rpt1ScrDedTaxAmt":number,
      /**  Display field for Rpt1ScrFixedAmount  */  
   "Rpt1ScrFixedAmount":number,
   "ScrDedTaxAmt":number,
   "ScrDocDedTaxAmt":number,
      /**  Doc Fixed Amount  */  
   "ScrDocFixedAmount":number,
   "ScrDocReportableAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
      /**  Display field for Rpt2FixedAmount  */  
   "Rpt2ScrFixedAmount":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
      /**  Display field for Rpt3rFixedAmount  */  
   "Rpt3ScrFixedAmount":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDocTaxableAmt":number,
   "ScrDocTaxAmt":number,
   "ScrDocTaxAmtVar":number,
      /**  FixedAmount  */  
   "ScrFixedAmount":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_POMiscRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   "PONum":number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  */  
   "POLine":number,
      /**  Sequence Number  */  
   "SeqNum":number,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   "MiscCode":string,
      /**  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  */  
   "Description":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "MiscAmt":number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "DocMiscAmt":number,
      /**  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  */  
   "Taxable":boolean,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "InvoicedAmt":number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "DocInvoicedAmt":number,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  */  
   "OrderSeqNum":number,
      /**  Linked to sales order misc charge.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Reporting currency value of this field  */  
   "Rpt1InvoicedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InvoicedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InvoicedAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2MiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3MiscAmt":number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   "Percentage":number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   "Type":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "InMiscAmt":number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   "DocInMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InMiscAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InMiscAmt":number,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "InInvoiceAmt":number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   "DocInInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1InInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2InInvoiceAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3InInvoiceAmt":number,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   "NoTaxRecalc":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
   "CurrencySwitch":boolean,
   "CurrencySymbol":string,
   "DocCurrencySymbol":string,
   "POHeaderApprove":boolean,
   "Rpt1ScrMiscAmt":number,
   "Rpt2ScrMiscAmt":number,
   "Rpt3ScrMiscAmt":number,
   "ScrDocMiscAmt":number,
   "ScrMiscAmt":number,
      /**  Description of Tax ID  */  
   "TaxIDDescription":string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   "DocTotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   "DocTotalSATax":number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   "DocTotalTax":number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   "Rpt1TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   "Rpt2TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   "Rpt3TotalTax":number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   "TotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   "TotalSATax":number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   "TotalTax":number,
   "BitFlag":number,
   "MiscCodeLCCurrencyCode":string,
   "MiscCodeLCAmount":number,
   "MiscCodeDescription":string,
   "MiscCodeLCDisburseMethod":string,
   "MiscCodeTaxCatID":string,
   "PONumInPrice":boolean,
   "PONumShipName":string,
   "PONumShipToConName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PORelAttchRow{
   "Company":string,
   "PONum":number,
   "POLine":number,
   "PORelNum":number,
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

export interface Erp_Tablesets_PORelRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   "OpenRelease":boolean,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  */  
   "VoidRelease":boolean,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   "DueDate":string,
      /**  Order quantity for this release in our unit of measure.  */  
   "XRelQty":number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  */  
   "PurchasingFactor":number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   "RelQty":number,
      /**  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  */  
   "JobNum":string,
      /**  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  */  
   "AssemblySeq":number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   "JobSeqType":string,
      /**  Seq # of specific material or subcontract operation record.  */  
   "JobSeq":number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   "WarehouseCode":string,
      /**  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  */  
   "ReceivedQty":number,
      /**  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  */  
   "ExpOverride":boolean,
      /**  Requisition which generated this PORel record.  */  
   "ReqNum":number,
      /**  Requisition line which generated this PORel record.  */  
   "ReqLine":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   "PromiseDt":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   "Confirmed":boolean,
      /**  Can be "web", "client", or "rejected"  */  
   "ConfirmVia":string,
      /**   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  */  
   "ReqChgDate":string,
      /**   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  */  
   "ReqChgQty":number,
      /**  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  */  
   "LockRel":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  */  
   "RefDisplayAccount":string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   "RefType":string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   "RefCode":string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   "RefCodeDesc":string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   "OrderNum":number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   "OrderLine":number,
      /**  Order Release Line created for this PO Release for the Inter-Company Trading.  */  
   "OrderRelNum":number,
      /**  Linked to sales order release.  */  
   "Linked":boolean,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  */  
   "ShippedQty":number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   "TranType":string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   "GlbCompany":string,
      /**  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  */  
   "GlbPlant":string,
      /**  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  */  
   "GlbWarehouse":string,
      /**  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  */  
   "GlbCreateJobMtl":boolean,
      /**  Shipped Date  */  
   "ShippedDate":string,
      /**  ID field to the ContainerHeader table.  */  
   "ContainerID":number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   "PurchasingFactorDirection":string,
      /**  This field holds the previous value of Due Date.  */  
   "PreviousDueDate":string,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  */  
   "BaseQty":number,
      /**   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   "BaseUOM":string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderNum":number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderLine":number,
      /**  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  */  
   "BTOOrderRelNum":number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order POs.  */  
   "DropShip":boolean,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  */  
   "ShipToNum":string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  */  
   "SoldToNum":number,
      /**  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  */  
   "SMIRcvdQty":number,
      /**  Contains the key value for the shipping contact.  */  
   "ShpConNum":number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  */  
   "MangCustNum":number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  */  
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
      /**  One Time Ship To Contact Name  */  
   "OTSContact":string,
      /**  Fax number for the One Time ShipTo.  */  
   "OTSFaxNum":string,
      /**  Phone number for the One Time ShipTo  */  
   "OTSPhoneNum":string,
      /**  One Time Shipping Country Number  */  
   "OTSCountryNum":number,
      /**  Displays the cause why the item is not compliant.  */  
   "ComplianceMsg":string,
      /**  Open Purchase Release flag  */  
   "PORelOpen":boolean,
      /**  Mapping  */  
   "Mapping":boolean,
      /**  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  */  
   "PhaseID":string,
      /**  Project Phase ID  */  
   "WBSPhaseID":string,
      /**  IsMultiRel  */  
   "IsMultiRel":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Field to track the SMIRcvdQty that has not yet been moved to stock  */  
   "SMIRemQty":number,
      /**  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  */  
   "LockQty":boolean,
      /**  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  */  
   "LockDate":boolean,
      /**  Indicates Due Date has been changed.  */  
   "DueDateChanged":boolean,
      /**  The identifier of the planning contract.  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   "LinkToContract":boolean,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  */  
   "Status":string,
      /**  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  */  
   "ArrivedQty":number,
      /**  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  */  
   "InvoicedQty":number,
      /**  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  */  
   "NeedByDate":string,
      /**  Set to 'true' if 'NeedByDate' was derived from a valid demand.  */  
   "LockNeedByDate":boolean,
      /**  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  */  
   "InspectionQty":number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   "FailedQty":number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   "PassedQty":number,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   "ProjProcessed":boolean,
      /**  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  */  
   "DeliverTo":string,
      /**  Taxable  */  
   "Taxable":boolean,
      /**  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  */  
   "TaxExempt":string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   "NoTaxRecalc":boolean,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  When the Promise Date is changed, this is the previous PromiseDt  */  
   "ReqChgPromiseDate":string,
      /**  One Time ShipTo email address.  */  
   "OTSEMailAddress":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Unit of measure for the NumberOfPieces.  */  
   "NumberOfPiecesUOM":string,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  Indicates if this release is  "FIRM".  */  
   "FirmRelease":boolean,
      /**  OTSTaxValidationStatus  */  
   "OTSTaxValidationStatus":number,
      /**  OTSTaxValidationDate  */  
   "OTSTaxValidationDate":string,
      /**  Name of the ship reference that is going to be stored.  */  
   "EDIShipReferenceType":string,
      /**  Data that is going to be stored as ship reference.  */  
   "EDIShipReferenceData":string,
      /**  Estimated time when the shipment will arrive.  */  
   "EDIEstimatedDockDate":string,
      /**  Quantity sent by the supplier.  */  
   "EDIShipQty":number,
      /**  Unit of Measure of the EDIShipQty.  */  
   "EDIShipQtyUOM":string,
   "ConsolidatedPO":boolean,
      /**  Is this Release related to a Contract Purchase Order?  */  
   "ContractOrder":boolean,
   "DelPoSug":boolean,
      /**  Display GL Account  */  
   "DispGLAcct":string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   "DocTotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   "DocTotalSATax":number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   "DocTotalTax":number,
      /**  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  */  
   "EnableBTOOrderNum":boolean,
      /**  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  */  
   "EnableGLAcct":boolean,
   "EstUnitCost":number,
   "ExpDesc":string,
   "FromPOSugChg":boolean,
   "GlbPlantName":string,
   "GlbWhseName":string,
   "Inspection":boolean,
   "IUM":string,
      /**  This field will be used in the UI to Lock and unLock a release.  */  
   "Lock":boolean,
      /**  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  */  
   "MangCustID":string,
      /**  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  */  
   "MangCustName":string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   "NotCompliant":boolean,
      /**  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   "OrderHeld":boolean,
   "POHeaderApprove":boolean,
      /**  Identifies the type of PO  */  
   "POType":string,
      /**  Replicate PUM on detail  */  
   "PUM":string,
      /**  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   "PurPoint":string,
   "RefCodeStatus":string,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   "Rpt1TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   "Rpt1TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   "Rpt2TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   "Rpt2TotalTax":number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalDedTax":number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   "Rpt3TotalSATax":number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   "Rpt3TotalTax":number,
   "ShipToAddressList":string,
      /**  Description text of the Status field  */  
   "StatusDescription":string,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   "TotalDedTax":number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   "TotalSATax":number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   "TotalTax":number,
      /**   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  */  
   "TranTypeDesc":string,
      /**  Indicates if Glb fields should be used in place of the non-global equivalent  */  
   "UseGlbFields":boolean,
      /**  Related Supplier ID  */  
   "VendorID":string,
      /**  Related Vendor Name  */  
   "VendorName":string,
      /**  Logical indicating if the container has been shipped.  */  
   "ContainerShipped":boolean,
      /**  The formatted ship to address  */  
   "ShipToAddrFormatted":string,
      /**  ID of related Attribute Class.  */  
   "AttrClassID":string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   "TrackInventoryAttributes":boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   "EnableDynAttrButton":boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   "AttributeQtyMismatch":boolean,
   "JobMtlSeq":number,
   "JobOprSeq":number,
   "TrackInventoryByRevision":boolean,
   "BitFlag":number,
   "AssemblySeqDescription":string,
   "ContainerHeaderPromiseDate":string,
   "ContainerHeaderDueDate":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "PlantName":string,
   "POLineRevisionNum":string,
   "POLineLineDesc":string,
   "POLineVenPartNum":string,
   "POLinePartNum":string,
   "PONumShipName":string,
   "PONumShipToConName":string,
   "ProjectIDDescription":string,
   "ReqLineLineDesc":string,
   "ReqNumShipName":string,
   "ReqNumShipToConName":string,
   "ShipToCustNumInactive":boolean,
   "ShipToCustNumBTName":string,
   "ShipToCustNumCustID":string,
   "ShipToCustNumName":string,
   "ShipToNumInactive":boolean,
   "SoldToNumCustID":string,
   "SoldToNumBTName":string,
   "SoldToNumName":string,
   "SoldToNumInactive":boolean,
   "WarehouseCodeDescription":string,
   "WBSPhaseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PORelTGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   "TGLCTranNum":number,
      /**  String identifier of the account context.  */  
   "GLAcctContext":string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   "BookID":string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   "COACode":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "GLAccount":string,
      /**  Indicates if the user can update or delete this record.  */  
   "UserCanModify":boolean,
      /**  Segement Value 1 of the account for this context.  */  
   "SegValue1":string,
      /**  Segement Value 2 of the account for this context.  */  
   "SegValue2":string,
      /**  Segement Value 3 of the account for this context.  */  
   "SegValue3":string,
      /**  Segement Value 4 of the account for this context.  */  
   "SegValue4":string,
      /**  Segement Value 5 of the account for this context.  */  
   "SegValue5":string,
      /**  Segement Value 6 of the account for this context.  */  
   "SegValue6":string,
      /**  Segement Value 7 of the account for this context.  */  
   "SegValue7":string,
      /**  Segement Value 8 of the account for this context.  */  
   "SegValue8":string,
      /**  Segement Value 9 of the account for this context.  */  
   "SegValue9":string,
      /**  Segement Value 10 of the account for this context.  */  
   "SegValue10":string,
      /**  Segement Value 11 of the account for this context.  */  
   "SegValue11":string,
      /**  Segement Value 12 of the account for this context.  */  
   "SegValue12":string,
      /**  Segement Value 13 of the account for this context.  */  
   "SegValue13":string,
      /**  Segement Value 14 of the account for this context.  */  
   "SegValue14":string,
      /**  Segement Value 15 of the account for this context.  */  
   "SegValue15":string,
      /**  Segement Value 16 of the account for this context.  */  
   "SegValue16":string,
      /**  Segement Value 17 of the account for this context.  */  
   "SegValue17":string,
      /**  Segement Value 18 of the account for this context.  */  
   "SegValue18":string,
      /**  Segement Value 19 of the account for this context.  */  
   "SegValue19":string,
      /**  Segement Value 20 of the account for this context.  */  
   "SegValue20":string,
      /**  Unique Identifier of the system GL Control Type.  */  
   "SysGLControlType":string,
      /**  System generated GL Control Identifier.  */  
   "SysGLControlCode":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   "FiscalYear":number,
      /**  JournalCode of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Journal number of the related GLJrnDtl.  */  
   "JournalNum":number,
      /**  JournalLine of the related GLJrnDtl.  */  
   "JournalLine":number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   "TranDate":string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   "TranSource":string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   "LaborDtlSeq":number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysDate":string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "SysTime":number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   "TranNum":number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   "ARInvoiceNum":number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   "TransAmt":number,
      /**  Invoice Line Number associated with this GL Journal  */  
   "InvoiceLine":number,
      /**  The sequence number associated with this GL journal  */  
   "SeqNum":number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   "VendorNum":number,
      /**  Vendor's invoice number.  */  
   "APInvoiceNum":string,
      /**  Date record was created  */  
   "CreateDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  BookCreditAmount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  A unique code that identifies the document currency.  */  
   "CurrencyCode":string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   "RecordType":string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   "CorrAccUID":number,
      /**  this field equals ABTUID which was created during posting  */  
   "ABTUID":string,
      /**  Technical identifier.  */  
   "RuleUID":number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   "Statistical":number,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  IsModifiedByUser  */  
   "IsModifiedByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MovementNum  */  
   "MovementNum":number,
      /**  MovementType  */  
   "MovementType":string,
      /**  Plant  */  
   "Plant":string,
      /**  POLine of PORel  */  
   "POLine":number,
      /**  PONum of PORel  */  
   "PONum":number,
      /**  PORelNum of PORel  */  
   "PORelNum":number,
   "ReqRef":boolean,
      /**  Indicates if the user selected a different account from the default.  */  
   "AcctOverride":boolean,
      /**  Column used to know if the book assigned is the Main Book.  */  
   "IsMainBook":boolean,
   "BitFlag":number,
   "COADescription":string,
   "GLAccountAccountDesc":string,
   "GLAccountGLAcctDisp":string,
   "GLAccountGLShortAcct":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PORelTaxRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Purchase order that this release record is related to.  */  
   "PONum":number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   "POLine":number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   "PORelNum":number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   "TaxCode":string,
      /**  Tax Rate Code.  */  
   "RateCode":string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   "ECAcquisitionSeq":number,
      /**  ReportableAmt  */  
   "ReportableAmt":number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   "DocReportableAmt":number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   "TaxableAmt":number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   "DocTaxableAmt":number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   "Percent":number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   "TaxAmt":number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   "DocTaxAmt":number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   "Manual":boolean,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last changed (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   "ReverseCharge":boolean,
      /**  Reporting currency value of this field  */  
   "Rpt1ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3ReportableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmt":number,
      /**  CollectionType  */  
   "CollectionType":number,
      /**  Timing of when to report taxes  */  
   "Timing":number,
      /**  Exemption Type  */  
   "ExemptType":number,
      /**  Exemption Percent  */  
   "ExemptPercent":number,
      /**  Resolution Number  */  
   "ResolutionNum":string,
      /**  Resolution date.  */  
   "ResolutionDate":string,
      /**  Date to determine the tax rate.  */  
   "TaxRateDate":string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DefTaxableAmt":number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   "DocDefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxableAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxableAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DefTaxAmt":number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   "DocDefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DefTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DefTaxAmt":number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   "ManAdd":boolean,
      /**  Deducatable Tax Amount  */  
   "DedTaxAmt":number,
      /**  Deducatable Tax Amount  */  
   "DocDedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt1DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt2DedTaxAmt":number,
      /**  Reporting currency value of this field  */  
   "Rpt3DedTaxAmt":number,
      /**  Fixed Tax Amount  */  
   "FixedAmount":number,
      /**  Document Fixed Tax Amount  */  
   "DocFixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt1FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt2FixedAmount":number,
      /**  Reporting currency value of this field  */  
   "Rpt3FixedAmount":number,
      /**  Unique Identifier for Legal Text  */  
   "TextCode":string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "TaxAmtVar":number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   "DocTaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt1TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt2TaxAmtVar":number,
      /**  Reporting currency value of this field  */  
   "Rpt3TaxAmtVar":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencySwitch":boolean,
   "CurrencyCode":string,
   "DocScrDedTaxAmt":number,
   "DocScrReportableAmt":number,
   "DocScrTaxableAmt":number,
   "DocScrTaxAmt":number,
   "DocScrTaxAmtVar":number,
   "Rpt1ScrDedTaxAmt":number,
   "Rpt1ScrReportableAmt":number,
   "Rpt1ScrTaxableAmt":number,
   "Rpt1ScrTaxAmt":number,
   "Rpt1ScrTaxAmtVar":number,
   "Rpt2ScrDedTaxAmt":number,
   "Rpt2ScrReportableAmt":number,
   "Rpt2ScrTaxableAmt":number,
   "Rpt2ScrTaxAmt":number,
   "Rpt2ScrTaxAmtVar":number,
   "Rpt3ScrDedTaxAmt":number,
   "Rpt3ScrReportableAmt":number,
   "Rpt3ScrTaxableAmt":number,
   "Rpt3ScrTaxAmt":number,
   "Rpt3ScrTaxAmtVar":number,
   "ScrDedTaxAmt":number,
   "ScrReportableAmt":number,
   "ScrTaxableAmt":number,
   "ScrTaxAmt":number,
   "ScrTaxAmtVar":number,
   "DocScrFixedAmount":number,
   "Rpt1ScrFixedAmount":number,
   "Rpt2ScrFixedAmount":number,
   "Rpt3ScrFixedAmount":number,
      /**  Display Fixed Amount in base currency.  */  
   "ScrFixedAmount":number,
      /**  Collection Type Description  */  
   "DescCollectionType":string,
   "BitFlag":number,
   "RateCodeDescription":string,
   "TaxCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param calcTranType
   */  
export interface CalcAutoPORelTGLC_input{
      /**  Transaction Type  */  
   calcTranType:string,
}

export interface CalcAutoPORelTGLC_output{
   returnObj:boolean,
}

   /** Required : 
      @param ApproveValue
      @param ds
   */  
export interface ChangeApproveSwitch_input{
      /**  Was PO approved? Yes/No  */  
   ApproveValue:boolean,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeApproveSwitch_output{
parameters : {
      /**  output parameters  */  
   ViolationMsg:string,
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipOrderNum
      @param ipOrderLine
      @param ipPONum
      @param ipPOLine
   */  
export interface ChangeBTOOrderLineWarning_input{
      /**  Order Number  */  
   ipOrderNum:number,
      /**  Order Line  */  
   ipOrderLine:number,
      /**  PO Number  */  
   ipPONum:number,
      /**  PO Line  */  
   ipPOLine:number,
}

export interface ChangeBTOOrderLineWarning_output{
parameters : {
      /**  output parameters  */  
   opWrnMsg:string,
}
}

   /** Required : 
      @param confirmValue
      @param ds
   */  
export interface ChangeConfirmSwitch_input{
      /**  Was PO confirmed? Yes/No  */  
   confirmValue:boolean,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeConfirmSwitch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewUOM
      @param ds
   */  
export interface ChangeContractUOM_input{
      /**  New UOM  */  
   NewUOM:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeContractUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeCountry_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param iCurrencyCode
      @param ds
   */  
export interface ChangeCurrencyCode_input{
      /**  Currency Code  */  
   iCurrencyCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeCurrencySwitch_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeCurrencySwitch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewAsmSeq
      @param ds
   */  
export interface ChangeDetailAssemblySeq_input{
      /**  New Assembly to be tested  */  
   NewAsmSeq:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newCalcOurQty
      @param ds
   */  
export interface ChangeDetailCalcOurQty_input{
      /**  New Quantity  */  
   newCalcOurQty:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailCalcOurQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newCalcVendQty
      @param ds
   */  
export interface ChangeDetailCalcVendQty_input{
      /**  New Quantity  */  
   newCalcVendQty:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailCalcVendQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newCommodityCode
      @param ds
   */  
export interface ChangeDetailCommodityCode_input{
      /**  New Commodity Code  */  
   newCommodityCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailCommodityCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newContractID
      @param ds
   */  
export interface ChangeDetailContractID_input{
      /**  New Contract ID  */  
   newContractID:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailContractID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newCostPerCode
      @param ds
   */  
export interface ChangeDetailCostPerCode_input{
   newCostPerCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailCostPerCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newIUM
      @param ds
   */  
export interface ChangeDetailIUM_input{
      /**  New IUM  */  
   newIUM:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailIUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewJobNum
      @param ds
   */  
export interface ChangeDetailJobNum_input{
      /**  New Job Number  */  
   NewJobNum:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewJobSeqNum
      @param ds
   */  
export interface ChangeDetailJobSeq_input{
      /**  New job/mtl seq to be tested  */  
   NewJobSeqNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewMangCust
      @param ds
   */  
export interface ChangeDetailMangCust_input{
      /**  New MangCustID  */  
   NewMangCust:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailMangCust_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newMfgNum
      @param ds
   */  
export interface ChangeDetailMfgNum_input{
      /**  New MfgNum  */  
   newMfgNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailMfgNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newMfgPartNum
      @param ds
   */  
export interface ChangeDetailMfgPartNum_input{
      /**  New MfgPartNum  */  
   newMfgPartNum:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailMfgPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipOrderLine
      @param ds
   */  
export interface ChangeDetailOrderLine_input{
      /**  New OrderLine  */  
   ipOrderLine:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipOrderNum
      @param ds
   */  
export interface ChangeDetailOrderNum_input{
      /**  New OrderNum  */  
   ipOrderNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param overridePriceList
      @param ds
   */  
export interface ChangeDetailOverridePriceList_input{
      /**  True is override pricelist has been checked  */  
   overridePriceList:boolean,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailOverridePriceList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newPUM
      @param ds
   */  
export interface ChangeDetailPUM_input{
      /**  New PUM  */  
   newPUM:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailPUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewClassID
      @param ds
   */  
export interface ChangeDetailPartClass_input{
      /**  New Class ID  */  
   NewClassID:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailPartClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewPartNum
      @param SysRowID
      @param rowType
      @param isSubstitute
      @param ds
   */  
export interface ChangeDetailPartNum_input{
      /**  New Part Number  */  
   NewPartNum:string,
      /**  Sys Row ID for match (conflict resolution only)  */  
   SysRowID:string,
      /**  Row Type for match (conflict resolution only)  */  
   rowType:string,
      /**  True whether it is a Substitute Part  */  
   isSubstitute:boolean,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailPartNum_output{
parameters : {
      /**  output parameters  */  
   NewPartNum:string,
   multipleMatch:boolean,
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDetailRevisionNum_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newTaxCatID
      @param ds
   */  
export interface ChangeDetailTaxCatID_input{
      /**  New Tax Category  */  
   newTaxCatID:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailTaxCatID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newTranType
      @param ds
   */  
export interface ChangeDetailTranType_input{
      /**  New Transaction Type  */  
   newTranType:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailTranType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newVenPartNum
      @param ds
   */  
export interface ChangeDetailVenPartNum_input{
      /**  New VenPartNum  */  
   newVenPartNum:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeDetailVenPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedAccountNum
      @param inTGLCTranNum
      @param ds
   */  
export interface ChangeExpAcct_input{
      /**  The proposed account number  */  
   proposedAccountNum:string,
      /**  The TGLCTranNum of the PORelTGLC record to be checked  */  
   inTGLCTranNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeExpAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedFixedAmt
      @param ds
   */  
export interface ChangeHeaderTaxFixedAmount_input{
      /**  The proposed fixed amount  */  
   proposedFixedAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedRateCode
      @param ds
   */  
export interface ChangeHeaderTaxRateCodeMaster_input{
      /**  The proposed rate code  */  
   proposedRateCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxRateCodeMaster_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeHeaderTaxRateCode_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedReportableAmt
      @param ds
   */  
export interface ChangeHeaderTaxReportableAmt_input{
      /**  The proposed reportable amount  */  
   proposedReportableAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedTaxAmt
      @param ds
   */  
export interface ChangeHeaderTaxTaxAmt_input{
      /**  The proposed tax amount  */  
   proposedTaxAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedTaxCode
      @param ds
   */  
export interface ChangeHeaderTaxTaxCode_input{
      /**  The proposed tax code  */  
   proposedTaxCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedTaxDeductable
      @param ds
   */  
export interface ChangeHeaderTaxTaxDeductable_input{
      /**  The proposed tax deductable  */  
   proposedTaxDeductable:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxTaxDeductable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedTaxPercent
      @param ds
   */  
export interface ChangeHeaderTaxTaxPercent_input{
      /**  The proposed tax percent  */  
   proposedTaxPercent:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedTaxableAmt
      @param ds
   */  
export interface ChangeHeaderTaxTaxableAmt_input{
      /**  The proposed taxable amount  */  
   proposedTaxableAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeHeaderTaxTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedMiscAmt
      @param ds
   */  
export interface ChangePOHeadMiscAmt_input{
      /**  The proposed miscellanous amount  */  
   proposedMiscAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOHeadMiscAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newMiscCode
      @param ds
   */  
export interface ChangePOHeadMiscCode_input{
      /**  The code of misc charge  */  
   newMiscCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOHeadMiscCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePOHeadMiscPrcnt_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOHeadMiscPrcnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param proposedMiscAmt
      @param ds
   */  
export interface ChangePOMiscAmt_input{
      /**  The proposed miscellanous amount  */  
   proposedMiscAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOMiscAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newMiscCode
      @param ds
   */  
export interface ChangePOMiscCode_input{
      /**  The code of misc charge  */  
   newMiscCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOMiscCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePOMiscPrcnt_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOMiscPrcnt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipContractID
      @param ds
   */  
export interface ChangePORelContract_input{
      /**  New ContractID  */  
   ipContractID:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePORelContract_output{
parameters : {
      /**  output parameters  */  
   ipContractID:string,
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newTaxRegionCode
      @param ds
   */  
export interface ChangePOTaxRegionCode_input{
      /**  New PUM  */  
   newTaxRegionCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOTaxRegionCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newPOType
      @param ds
   */  
export interface ChangePOType_input{
      /**  Proposed newPOType to be validated  */  
   newPOType:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePOType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangePoMiscCurrSwitch_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePoMiscCurrSwitch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param prcConNumOrName
      @param ds
   */  
export interface ChangePrcConNumByNameOrNum_input{
      /**  Vendor's contact name or num  */  
   prcConNumOrName:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePrcConNumByNameOrNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param prcConName
      @param ds
   */  
export interface ChangePrcConNumByName_input{
      /**  Vendor's contact name  */  
   prcConName:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePrcConNumByName_output{
parameters : {
      /**  output parameters  */  
   prcConNum:number,
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param PrcConNum
      @param ds
   */  
export interface ChangePrcConNum_input{
      /**  Proposed PrcConNum to be validated  */  
   PrcConNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePrcConNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param PurPoint
      @param ds
   */  
export interface ChangePurPoint_input{
      /**  New Purchase Point  */  
   PurPoint:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangePurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipQtyOption
      @param ds
   */  
export interface ChangeQtyOption_input{
      /**  New QtyOption  */  
   ipQtyOption:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeQtyOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewAsmSeq
      @param ds
   */  
export interface ChangeRelAssemblySeq_input{
      /**  New Assembly to be tested  */  
   NewAsmSeq:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ProposedGlbCompany
      @param ds
   */  
export interface ChangeRelGlbCompany_input{
      /**  Proposed GlbCompany value  */  
   ProposedGlbCompany:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelGlbCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ProposedGlbPlant
      @param ds
   */  
export interface ChangeRelGlbPlant_input{
      /**  Proposed GlbPlant value  */  
   ProposedGlbPlant:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelGlbPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ProposedGlbWarehouse
      @param ds
   */  
export interface ChangeRelGlbWarehouse_input{
      /**  Proposed GlbCompany value  */  
   ProposedGlbWarehouse:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelGlbWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewIUM
      @param ds
   */  
export interface ChangeRelIUM_input{
      /**  New IUM  */  
   NewIUM:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelIUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewJobNum
      @param ds
   */  
export interface ChangeRelJobNum_input{
      /**  New Job Number  */  
   NewJobNum:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipTranType
      @param ipJobNum
      @param ipAssemblySeq
      @param ipNewJobSeq
      @param ipPODtlPartNum
      @param ipPODtlRevNum
   */  
export interface ChangeRelJobSeqWarning_input{
      /**  Transaction Type  */  
   ipTranType:string,
      /**  Job Number  */  
   ipJobNum:string,
      /**  Assembly Sequence  */  
   ipAssemblySeq:number,
      /**  Job Sequence  */  
   ipNewJobSeq:number,
      /**  Part Number  */  
   ipPODtlPartNum:string,
      /**  Part Revision  */  
   ipPODtlRevNum:string,
}

export interface ChangeRelJobSeqWarning_output{
parameters : {
      /**  output parameters  */  
   opWrnMsg:string,
}
}

   /** Required : 
      @param NewJobSeqNum
      @param ds
   */  
export interface ChangeRelJobSeq_input{
      /**  New job/mtl seq to be tested  */  
   NewJobSeqNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewMangCust
      @param ds
   */  
export interface ChangeRelMangCust_input{
      /**  New MangCustID  */  
   NewMangCust:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelMangCust_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipOrderLine
      @param ds
   */  
export interface ChangeRelOrderLine_input{
      /**  New OrderLine  */  
   ipOrderLine:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipOrderNum
      @param ds
   */  
export interface ChangeRelOrderNum_input{
      /**  New OrderNum  */  
   ipOrderNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipOrderRelNum
      @param ds
   */  
export interface ChangeRelOrderRelNum_input{
      /**  New OrderRelNum  */  
   ipOrderRelNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelOrderRelNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
   opWrnMsg:string,
}
}

   /** Required : 
      @param NewOurQty
      @param ds
   */  
export interface ChangeRelOurQty_input{
      /**  New quantity to be tested  */  
   NewOurQty:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelOurQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
   opWarningMsg:string,
}
}

   /** Required : 
      @param NewPUM
      @param ds
   */  
export interface ChangeRelPUM_input{
      /**  New PUM  */  
   NewPUM:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelPUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newPlant
      @param ds
   */  
export interface ChangeRelPlant_input{
      /**  New Plant  */  
   newPlant:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newTaxExempt
      @param ds
   */  
export interface ChangeRelTaxExempt_input{
      /**  New Tax Exempt  */  
   newTaxExempt:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelTaxExempt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param NewVendQty
      @param ds
   */  
export interface ChangeRelVendQty_input{
      /**  New quantity to be tested  */  
   NewVendQty:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeRelVendQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
   opWarningMsg:string,
}
}

   /** Required : 
      @param tableName
      @param proposedTaxDeductable
      @param ds
   */  
export interface ChangeTaxDeductable_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed tax deductible  */  
   proposedTaxDeductable:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxDeductable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param proposedFixedAmt
      @param ds
   */  
export interface ChangeTaxFixedAmount_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed reportable amount  */  
   proposedFixedAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxFixedAmount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param proposedTaxPercent
      @param ds
   */  
export interface ChangeTaxPercent_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed tax percent  */  
   proposedTaxPercent:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param proposedRateCode
      @param ds
   */  
export interface ChangeTaxRateCode_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed rate code  */  
   proposedRateCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxRateCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param proposedReportableAmt
      @param ds
   */  
export interface ChangeTaxReportableAmt_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed reportable amount  */  
   proposedReportableAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxReportableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param proposedTaxAmt
      @param ds
   */  
export interface ChangeTaxTaxAmt_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed tax amount  */  
   proposedTaxAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxTaxAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param proposedTaxCode
      @param ds
   */  
export interface ChangeTaxTaxCode_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed tax code  */  
   proposedTaxCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxTaxCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param proposedTaxableAmt
      @param ds
   */  
export interface ChangeTaxTaxableAmt_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
      /**  The proposed taxable amount  */  
   proposedTaxableAmt:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTaxTaxableAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param newTranType
      @param ds
   */  
export interface ChangeTranType_input{
      /**  New transaction type  */  
   newTranType:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeTranType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param poNum
      @param poLine
   */  
export interface ChangeUOMConfirm_input{
   poNum:number,
   poLine:number,
}

export interface ChangeUOMConfirm_output{
parameters : {
      /**  output parameters  */  
   msg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUnitPriceConfirmOverride_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeUnitPriceConfirmOverride_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
   sConfirmMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUnitPrice_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeUnitPrice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param VendID
      @param ds
   */  
export interface ChangeVendor_input{
      /**  Proposed vendor ID to be validated  */  
   VendID:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangeVendor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param poNum
      @param ds
   */  
export interface ChangedApproveSwitch_input{
      /**  The Purchase Order Number  */  
   poNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangedApproveSwitch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
   violationMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangedHeaderTaxManual_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangedHeaderTaxManual_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param tableName
      @param ds
   */  
export interface ChangedTaxManual_input{
      /**  Table Name POHeaderMiscTax, PODetailMiscTax or PORelTax  */  
   tableName:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangedTaxManual_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ChangingDetailRevisionNum_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface ChangingDetailRevisionNum_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param viewName
      @param ds
   */  
export interface CheckBeforeUpdate_input{
      /**  ViewName  */  
   viewName:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface CheckBeforeUpdate_output{
parameters : {
      /**  output parameters  */  
   cOrderChangedMsgText:string,
   taxableChangedMsgText:string,
   vendorChangedMsgText:string,
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param poNum
   */  
export interface CheckComplianceFail_input{
      /**  Current PO Number.  */  
   poNum:number,
}

export interface CheckComplianceFail_output{
parameters : {
      /**  output parameters  */  
   compliant:boolean,
}
}

   /** Required : 
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface CheckForMRPAttributes_input{
      /**  PO Number  */  
   poNum:number,
      /**  PO Line  */  
   poLine:number,
      /**  PO rel num  */  
   poRelNum:number,
}

export interface CheckForMRPAttributes_output{
parameters : {
      /**  output parameters  */  
   mrpAttributeMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckLOCWithMessages_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface CheckLOCWithMessages_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
   opMessageLimit:string,
   opMessageShipComplete:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckLOC_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface CheckLOC_output{
parameters : {
      /**  output parameters  */  
   opMsg:any[],
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CheckPODetailCNBonded_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface CheckPODetailCNBonded_output{
parameters : {
      /**  output parameters  */  
   sMessage:string,
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ProposedPONum
   */  
export interface CheckPONum_input{
      /**  The proposed PO Number  */  
   ProposedPONum:number,
}

export interface CheckPONum_output{
parameters : {
      /**  output parameters  */  
   opFoundPO:boolean,
   opMessage:string,
}
}

   /** Required : 
      @param ipProjectID
      @param ds
   */  
export interface CheckProjectID_input{
      /**  The Project ID value  */  
   ipProjectID:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface CheckProjectID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipRateGrpCode
      @param ds
   */  
export interface CheckRateGrpCode_input{
      /**  Currency Rate Group Code  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface CheckRateGrpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param PoNum
      @param PoLine
   */  
export interface CloseOrderLine_input{
      /**  The purchase order number  */  
   PoNum:number,
      /**  The purchase order line  */  
   PoLine:number,
}

export interface CloseOrderLine_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param PoNum
   */  
export interface CloseOrder_input{
      /**  The purchase order number  */  
   PoNum:number,
}

export interface CloseOrder_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param PoNum
      @param PoLine
      @param PoRelease
   */  
export interface CloseRelease_input{
      /**  The purchase order number  */  
   PoNum:number,
      /**  The purchase order line  */  
   PoLine:number,
      /**  The purchase order release number  */  
   PoRelease:number,
}

export interface CloseRelease_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param poNum
   */  
export interface DeleteByID_input{
   poNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param poNum
      @param copyUnitCosts
      @param copyJobInfo
      @param getLatestSupplierPrice
      @param getLatestRevision
      @param newDueDate
      @param newPromiseDate
      @param newBuyerID
   */  
export interface DuplicatePO_input{
      /**  The purchase order number  */  
   poNum:number,
      /**  Unit Costs  */  
   copyUnitCosts:boolean,
      /**  Job Info  */  
   copyJobInfo:boolean,
      /**  Supplier Price List  */  
   getLatestSupplierPrice:boolean,
      /**  Latest Revision  */  
   getLatestRevision:boolean,
      /**  new Due Date  */  
   newDueDate:string,
      /**  new Promise Date  */  
   newPromiseDate:string,
      /**  new BuyerID  */  
   newBuyerID:string,
}

export interface DuplicatePO_output{
   returnObj:Erp_Tablesets_POTableset[],
parameters : {
      /**  output parameters  */  
   cJobMTLIssuedComplete:string,
}
}

export interface Erp_Tablesets_PODetailAttchRow{
   Company:string,
   PONUM:number,
   POLine:number,
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

export interface Erp_Tablesets_PODetailInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase order number that the detail line item is linked to.  */  
   PONUM:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   POLine:number,
      /**  A sequence number that uniquely identifies the PartMtlInsp record within the Part material  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PODetailMiscTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Purchase order that this release record is related to.  */  
   PONUM:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ** NOT USED TO BE DROPPED 10.2 **  */  
   MiscCode:string,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  User ID of the user who created the record  */  
   CreatedBy:string,
      /**  The date/ time that the record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date/ time that the record was last changed  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Indicates if this row was created as part of the migration process.  */  
   Migrated:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Desc. Collection Type  */  
   DescCollectionType:string,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   DocScrFixedAmount:number,
   Rpt1ScrFixedAmount:number,
   Rpt2ScrFixedAmount:number,
   Rpt3ScrFixedAmount:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PODetailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this line item is Open/Closed. This is not directly maintainable by the user. Normally it gets set to "Closed" as a result of the receiving process. When there are no longer any open PORel records then the PODetail record is closed. This can also be closed when the user Voids the Order or PODetail record.  */  
   OpenLine:boolean,
      /**   Indicates if the Line was voided. Voided line items are not maintainable, can't "unvoid".  This field is not directly maintainable.  Instead the void function will be performed via a "Void Line" button.  Which then presents a verification dialog box.
When an PODetail record is 'voided',  all current open  PORel records are also closed and voided.  If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoHeader is voided.  */  
   VoidLine:boolean,
      /**  Purchase order number that the detail line item is linked to.  */  
   PONUM:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   POLine:number,
      /**  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  */  
   LineDesc:string,
      /**  (Our) Unit Of Measure.  */  
   IUM:string,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   UnitCost:number,
      /**  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  */  
   DocUnitCost:number,
      /**  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This insures that Order quantity and scheduled  quantities are always in sync.  */  
   OrderQty:number,
      /**  Total Order Quantity for the line item.  This is stored in Our Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table.  Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable.  As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted.  This ensures that Order quantity and scheduled quantities are always in sync.  */  
   XOrderQty:number,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Purchasing UOM  */  
   PUM:string,
      /**   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCode:string,
      /**  OUR internal Part number for this item.  */  
   PartNum:string,
      /**  Supplier Part Number  */  
   VenPartNum:string,
      /**  Contains comments about the detail order line item. These will be printed on the purchase order.  Defaults from the related JobOper, JobMtl or Part file.  */  
   CommentText:string,
      /**  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.ClassID. The PartClass is used in determining a default G/L expense account.  */  
   ClassID:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Indicates if  Inspection is required when this PO line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in POHeader and is maintained  in the write triggers of POHeader and PODetail.  */  
   VendorNum:number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   AdvancePayBal:number,
      /**  Tracks the "Balance" of Advance Payments which are to be used to reduce the invoice when actual order is received. This value is increased via the "Advance Pay" invoice type. It is reduced when the receipt invoice is created by entering amount in the APInvDtl.  */  
   DocAdvancePayBal:number,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   Confirmed:boolean,
      /**  Indicates this line has a pending date change  */  
   DateChgReq:boolean,
      /**  Indicates this line has a pending qty change  */  
   QtyChgReq:boolean,
      /**  Requested pending partnumber change  */  
   PartNumChgReq:string,
      /**  Requested pending revision change  */  
   RevisionNumChgReq:string,
      /**  Date Supplier Confirmed the PO  */  
   ConfirmDate:string,
      /**  Can be "web" or "client"  */  
   ConfirmVia:string,
      /**  Requested Price change.  SRM  */  
   PrcChgReq:number,
      /**  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  */  
   PurchCode:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Linked to sales order line.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Is this line active on the Contract Purchase Order?  */  
   ContractActive:boolean,
      /**  Quantity for this Contract Purchase Order Line.  */  
   ContractQty:number,
      /**  Unit Price for this Contract Purchase Order Line.  */  
   ContractUnitCost:number,
      /**  Document Unit Price for this Contract Purchase Order Line.  */  
   ContractDocUnitCost:number,
      /**  Advanced Payments Balance in Rpt1 currency.  */  
   Rpt1AdvancePayBal:number,
      /**  Advanced Payments Balance in Rpt2 currency.  */  
   Rpt2AdvancePayBal:number,
      /**  Advanced Payments Balance in Rpt3 currency.  */  
   Rpt3AdvancePayBal:number,
      /**  Unit price in the vendors unit of measure and Rpt1 currency.  */  
   Rpt1UnitCost:number,
      /**  Unit price in the vendors unit of measure and Rpt2 currency.  */  
   Rpt2UnitCost:number,
      /**  Unit price in the vendors unit of measure and Rpt3 currency.  */  
   Rpt3UnitCost:number,
      /**  Unit Of Measure of the ContractQty.  */  
   ContractQtyUOM:string,
      /**  Unit Price for this Contract Purchase Order Line in Rpt1 currency.  */  
   Rpt1ContractUnitCost:number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt2 currency.  */  
   Rpt2ContractUnitCost:number,
      /**  Unit Price for this Contract Purchase Order Line in Rpt3 currency.  */  
   Rpt3ContractUnitCost:number,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PODeltail.XOrderQty to the PODetail.BaseUOM .  */  
   BaseQty:number,
      /**   Unit of Measure of the PODetail.BaseXOrderQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   BaseUOM:string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderNum:number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderLine:number,
      /**   Vendor Part Print Options. Determines what is printed.
M = Main Part Reference (Default)
S = Secondary Part Reference
O = Only Part Reference
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   VendorPartOpts:string,
      /**   Mfg Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
A = All Supplier Parts Referenced
N = No Supplier Parts Referenced  */  
   MfgPartOpts:string,
      /**   Substitute Part Print Options. Determines what is printed.
O = Only Part Reference (Default)
M = Main Part Reference
S = Secondary Part Reference  */  
   SubPartOpts:string,
      /**  Manufacturer Unique ID  */  
   MfgNum:number,
      /**  Manufacturer's Part Number.  */  
   MfgPartNum:string,
      /**  Substitute Part Number  */  
   SubPartNum:string,
      /**   Substitute Part Type
O = Original
S = Substitute  */  
   SubPartType:string,
      /**   Same as Unit cost except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitCost:number,
      /**  This is the base cost for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitCost:number,
      /**  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  */  
   ConvOverRide:boolean,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  Direction  */  
   Direction:string,
      /**  Per  */  
   Per:string,
      /**  MaintainPricingUnits  */  
   MaintainPricingUnits:boolean,
      /**  OverrideConversion  */  
   OverrideConversion:boolean,
      /**  RowsManualFactor  */  
   RowsManualFactor:boolean,
      /**  KeepRowsManualFactorTmp  */  
   KeepRowsManualFactorTmp:boolean,
      /**  ShipToSupplierDate  */  
   ShipToSupplierDate:string,
      /**  Factor  */  
   Factor:number,
      /**  PricingQty  */  
   PricingQty:number,
      /**  PricingUnitPrice  */  
   PricingUnitPrice:number,
      /**  UOM  */  
   UOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  DocPricingUnitPrice  */  
   DocPricingUnitPrice:number,
      /**  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  */  
   OverridePriceList:boolean,
      /**  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  */  
   QtyOption:string,
      /**  Contains old comments about the detail order line item. This field saves old comments about the detail line that are going to be replaced by new comments.  */  
   OrigComment:string,
      /**  SmartString  */  
   SmartString:string,
      /**  SmartStringProcessed  */  
   SmartStringProcessed:boolean,
      /**  Specifies the date by which you need to receive the part. If you set the Due Date before create releases, it will act as default value when adding new releases. If you're adding lines from:  - BTO or Drop Shipments, PODetail.DueDate will take the value from OrderRel.NeedByDate. - Job Material , PODetail.DueDate  will take the value from JobMtl.ReqDate. - Subcontract Operations, PODetail.DueDate  wil take the value from JobOper.DueDate  */  
   DueDate:string,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  SelCurrPricingUnitPrice  */  
   SelCurrPricingUnitPrice:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date and time that the record was last changed  */  
   ChangeDate:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  Indicates the Tax Category for this PO line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  */  
   TaxCatID:string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   NoTaxRecalc:boolean,
      /**  Unit price in the vendors unit of measure inclusive of tax in base currency.  */  
   InUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in document currency.  */  
   DocInUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   Rpt1InUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   Rpt2InUnitCost:number,
      /**  Unit price in the vendors unit of measure inclusive of tax in Rpt1 currency.  */  
   Rpt3InUnitCost:number,
      /**  Advanced Payments Balance inclusive of tax in base currency.  */  
   InAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in document currency.  */  
   DocInAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in Rpt1 currency.  */  
   Rpt1InAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in Rpt2 currency.  */  
   Rpt2InAdvancePayBal:number,
      /**  Advanced Payments Balance inclusive of tax in Rpt3 currency.  */  
   Rpt3InAdvancePayBal:number,
      /**  Contract unit cost inclusive of tax in base currency.  */  
   InContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in document currency.  */  
   DocInContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in Rpt1 currency.  */  
   Rpt1InContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in Rpt2 currency.  */  
   Rpt2InContractUnitCost:number,
      /**  Contract unit cost inclusive of tax in Rpt3 currency.  */  
   Rpt3InContractUnitCost:number,
      /**  Extended cost of the PO Line in document currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.DocUnitCost.  */  
   DocExtCost:number,
      /**  Extended cost of the PO Line in base currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.UnitCost.  */  
   ExtCost:number,
      /**  Extended cost of the PO Line in Rpt1 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt1UnitCost.  */  
   Rpt1ExtCost:number,
      /**  Extended cost of the PO Line in Rpt2 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt2UnitCost.  */  
   Rpt2ExtCost:number,
      /**  Extended cost of the PO Line in Rpt3 currency. This is PODetail.OrderQty / PODetail.CostPerCode * PODetail.Rpt3UnitCost.  */  
   Rpt3ExtCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in document currency.  This is the sum of POMisc.DocMiscAmt for all line charges.  */  
   DocMiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in base currency.  This is the sum of POMisc.MiscAmt for all line charges.  */  
   MiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt for all line charges.  */  
   Rpt1MiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt for all line charges.  */  
   Rpt2MiscCost:number,
      /**  Total amount for all miscellaneous charges associated to this PO Line in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt for all line charges.  */  
   Rpt3MiscCost:number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   TotalTax:number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   DocTotalTax:number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   Rpt1TotalTax:number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   Rpt2TotalTax:number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   Rpt3TotalTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   TotalSATax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   DocTotalSATax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalSATax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalSATax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalSATax:number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   TotalDedTax:number,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   DocTotalDedTax:number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalDedTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalDedTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalDedTax:number,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  CNBonded  */  
   CNBonded:boolean,
      /**  Acknowledge code received from EDI  */  
   EDIAckCode:string,
      /**  Additional comments to send with Acknowledge  */  
   EDIAckComment:string,
      /**  The flag to indicate if the user is supposed to be asked to enter a Reference code before saving a new PoDetail record .  */  
   AskRefCode:boolean,
   CalcAssemblySeq:number,
   CalcDocTotalCost:number,
   CalcDueDate:string,
   CalcJobNum:string,
   CalcJobSeq:number,
   CalcJobSeqType:string,
   calcLeadTime:number,
   CalcMangCustID:string,
   CalcMangCustName:string,
   CalcMangCustNum:number,
   CalcMfg:string,
   CalcMfgPart:string,
   calcMinOrderQty:number,
   CalcOurQty:number,
   calcPartPUM:string,
      /**  purchasing factor  */  
   CalcPurchasingFactor:number,
   CalcPurchasingFactorDirection:string,
   CalcTotalCost:number,
   CalcTranType:string,
   CalcVendQty:number,
   Configured:string,
   ConsolidatedPO:boolean,
   ContractOrder:boolean,
      /**  Indicates the costing per quantity (When Contract PO). It can be "E" = per each, "C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit cost for the line item.  The logic is to divide the PODetail.OrderQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default.  If Part record does not exist then default as "E".  */  
   CostPerCodeContract:string,
   CPFactor:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DelPoSug:boolean,
   DisablePartRevBtn:boolean,
      /**  Display Account Description.  */  
   DispAcctDescription:string,
      /**  A character string made up of Div, Dept, Chart and Segment values and their related separators concatenated into the full GL account number.  */  
   DispExpAccount:string,
   DisplaySymbol:string,
   DocDisplaySymbol:string,
   DocScrUnitCost:number,
      /**  False if vendor or class requires inspection, otherwise true.  */  
   EnableRcvInspectionReq:boolean,
      /**  The Chart ID component of the default G/L account.  */  
   ExpChart:string,
      /**  The Division Component of the default expence G/L account.  */  
   ExpDivision:string,
      /**  The Department component of the default G/L account.  */  
   ExpGLDept:string,
   FromPOSugChg:boolean,
   LinkedSOConfig:boolean,
   MultiRel:boolean,
   NonMasterPart:boolean,
   OpCode:string,
   PartQtyBearing:boolean,
   POHeaderApprove:boolean,
      /**  True if there is only one release and it's open.  */  
   PORelOneOpenRelease:boolean,
   PriceBrkBTNSensitive:boolean,
      /**  Reference Code Description  */  
   RefCodeDesc:string,
      /**  Reference Code Status  */  
   RefCodeStatus:string,
      /**  Link to the related code in GlRefCod.RefCode  */  
   ReferenceCode:string,
   Rpt1CalcTotalCost:number,
   Rpt1ScrUnitCost:number,
   Rpt2CalcTotalCost:number,
   Rpt2ScrUnitCost:number,
   Rpt3CalcTotalCost:number,
   Rpt3ScrUnitCost:number,
      /**   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  */  
   ScrUnitCost:number,
   SetCheveron:boolean,
   SubAvail:boolean,
   UpdateRelRecords:boolean,
      /**  Update PO Release Taxable Flag on Change of PO Detail Taxable Flag  */  
   UpdateRelTaxable:boolean,
      /**  Purchase Point used in the Supplier Tracker.  */  
   VendPurPoint:string,
   AllowPORecon:boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   EnableDynAttrButton:boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   AttributeQtyMismatch:boolean,
   CalcJobMtlSeq:number,
   CalcJobOprSeq:number,
      /**  Flag to indicate the current PO Line has at least one Buy To Order Release  */  
   HasBuyToOrderRelease:boolean,
      /**  The flag to indicate if PO  doc/base/rpt line amounts are recalculated  whne entered and no need to recalculate on save.  */  
   LineAmtCalcd:boolean,
   BitFlag:number,
   ClassInactive:boolean,
   ClassDescription:string,
   CommodityCodeDescription:string,
   GlPurchPurchDesc:string,
   MfgNumMfgID:string,
   MfgNumName:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumAttrClassID:string,
   PONUMCurrencyCode:string,
   PONUMOrderDate:string,
   PONUMInPrice:boolean,
   PONUMShipName:string,
   PONUMShipToConName:string,
   TaxCatIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   DeliveryInstructions_c:string,
}

export interface Erp_Tablesets_PODetailTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Purchase order number.  */  
   PONum:number,
      /**  The line # of PODetail record  */  
   POLine:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  Reportable Amount  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  User ID of the user who created the record  */  
   CreatedBy:string,
      /**  The date / time that the record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date/ time that the record was last changed  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  ResolutionNum  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   DocScrFixedAmount:number,
   Rpt1ScrFixedAmount:number,
   Rpt2ScrFixedAmount:number,
   Rpt3ScrFixedAmount:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POHeadMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   PONum:number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  */  
   POLine:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   MiscAmt:number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   DocMiscAmt:number,
      /**  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  */  
   Taxable:boolean,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   InvoicedAmt:number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   DocInvoicedAmt:number,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  */  
   OrderSeqNum:number,
      /**  Linked to sales order misc charge.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Reporting currency value of this field  */  
   Rpt1InvoicedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoicedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoicedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   InMiscAmt:number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   DocInMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InMiscAmt:number,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   InInvoiceAmt:number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   DocInInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InInvoiceAmt:number,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   NoTaxRecalc:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrencySymbol:string,
   DocCurrencySymbol:string,
   POHeaderApprove:boolean,
   Rpt1ScrMiscAmt:number,
   Rpt2ScrMiscAmt:number,
   Rpt3ScrMiscAmt:number,
   ScrDocMiscAmt:number,
   ScrMiscAmt:number,
      /**  Description of Tax ID  */  
   TaxIDDescription:string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   DocTotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   DocTotalSATax:number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   DocTotalTax:number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   Rpt1TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   Rpt2TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   Rpt3TotalTax:number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   TotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   TotalSATax:number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   TotalTax:number,
   BitFlag:number,
   MiscCodeTaxCatID:string,
   MiscCodeLCAmount:number,
   MiscCodeLCCurrencyCode:string,
   MiscCodeLCDisburseMethod:string,
   MiscCodeDescription:string,
   PONumInPrice:boolean,
   PONumShipToConName:string,
   PONumShipName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POHeaderAttchRow{
   Company:string,
   PONum:number,
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

export interface Erp_Tablesets_POHeaderListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  */  
   OpenOrder:boolean,
      /**  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  */  
   VoidOrder:boolean,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Entry Person  */  
   EntryPerson:string,
      /**  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  */  
   OrderDate:string,
      /**  Incoterms  */  
   FOB:string,
      /**  Ship Via Code  */  
   ShipViaCode:string,
      /**  Terms  */  
   TermsCode:string,
      /**  defaults from the company file.  */  
   ShipName:string,
      /**  First adress line  */  
   ShipAddress1:string,
      /**  Second address line  */  
   ShipAddress2:string,
      /**  Third address line  */  
   ShipAddress3:string,
      /**  City portion of the address  */  
   ShipCity:string,
      /**  Statee portion of the address  */  
   ShipState:string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   ShipCountry:string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   OrderHeld:boolean,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   ShipToConName:string,
      /**  Indicates if the PO can be printed. Print functions are not available if this is = No.  */  
   ReadyToPrint:boolean,
   VendorVendorID:string,
   VendorName:string,
   BuyerIDName:string,
   FOBDescription:string,
      /**  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  */  
   ApprovedDate:string,
      /**  The BuyerID  that approved the PO. (See ApprovedDate for related info)  */  
   ApprovedBy:string,
   ShipViaCodeDescription:string,
   TermsCodeDescription:string,
      /**   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  */  
   Approve:boolean,
      /**   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  */  
   ApprovalStatus:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  */  
   POType:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POHeaderListTableset{
   POHeaderList:Erp_Tablesets_POHeaderListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_POHeaderMiscTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ** NOT USED TO BE DROPPED 10.2 ** The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   MiscCode:string,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  User ID o fthe user who created the record  */  
   CreatedBy:string,
      /**  The date / time that the record was created  */  
   CreatedOn:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date/ time that the record was last changed  */  
   ChangedOn:string,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Indicates if this row was created as part of the migration process.  */  
   Migrated:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
   CurrencySwitch:boolean,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   DocScrFixedAmount:number,
   Rpt1ScrFixedAmount:number,
   Rpt2ScrFixedAmount:number,
   Rpt3ScrFixedAmount:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POHeaderRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the order is open or closed. This is set automatically when all the PODetail records have been closed or can be set if the user Voids the Order. This field is not directly maintainable.  */  
   OpenOrder:boolean,
      /**  Indicates if the entire remaining Purchase Order is Voided. When an order is voided the POHeader.OpenOrder is set to No and all remaining PODetail and PORel records for the related order are closed and voided.  */  
   VoidOrder:boolean,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Entry Person  */  
   EntryPerson:string,
      /**  Order Date for this purchase order. Initially defaults as "today", then defaults as last date entered in this session.  */  
   OrderDate:string,
      /**  Incoterms  */  
   FOB:string,
      /**  Ship Via Code  */  
   ShipViaCode:string,
      /**  Terms  */  
   TermsCode:string,
      /**  defaults from the company file.  */  
   ShipName:string,
      /**  First adress line  */  
   ShipAddress1:string,
      /**  Second address line  */  
   ShipAddress2:string,
      /**  Third address line  */  
   ShipAddress3:string,
      /**  City portion of the address  */  
   ShipCity:string,
      /**  Statee portion of the address  */  
   ShipState:string,
      /**  Postal code or Zip code portion of the address  */  
   ShipZIP:string,
      /**  Country is used as part of the Ship to  address. It can be left blank.  */  
   ShipCountry:string,
      /**  The ID that links to the Purchasing Agent master file.  */  
   BuyerID:string,
      /**  The freight charge is to be paid by the vendor.  */  
   FreightPP:boolean,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  */  
   PrcConNum:number,
      /**  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  */  
   VendorNum:number,
      /**  Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
      /**  Contains comments about over all  purchase order. These will be printed on the purchase order.  */  
   CommentText:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   OrderHeld:boolean,
      /**  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  */  
   ShipToConName:string,
      /**  Indicates if the PO can be printed. Print functions are not available if this is = No.  */  
   ReadyToPrint:boolean,
      /**  N = New, C = Change Order  */  
   PrintAs:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  */  
   ShipCountryNum:number,
      /**  This field indicates if the system should generate purchase order booking records. Booking tables are used to track changes to POheader.  */  
   LogChanges:boolean,
      /**  System date that the PO was approved.  This only pertains to PO which exceeded the buyers limit and have been approved.  */  
   ApprovedDate:string,
      /**  The BuyerID  that approved the PO. (See ApprovedDate for related info)  */  
   ApprovedBy:string,
      /**   Inidicates if the PO is "ready" to be approved.  This is checked  when all the information is complete and is ready to be processed. When checked the system will test if PO has exceeded the buyers or system purchasing limit.  (See ApprovalStatus for related info)
When Approve = yes the PO cannot be maintained.  */  
   Approve:boolean,
      /**   Indicates the approval status of the PO.
Valid values are; U - Unsubmitted for Approval,  P - Pending Approval, A - Approved, R - Rejected.  Before a PO can be printed it must be approved.  A PO is consider  approved if it doesn't exceed the buyers limit or it has been approved by the approver.  */  
   ApprovalStatus:string,
      /**   An internally used field that represents the total amount of the PO (in base currency) captured the last time the po was approved/rejected.  Note: this only pertains to PO that required approval in the first place otherwise it's zero.  The limit checking process will compare PO amounts to the greater of the buyers limit or this amount. Basically, if the PO was already approved once for a specific amount then it should not require subsequent approval until that amount is exceeded.
Note: This also contains the PO amount if it was rejected. In this case, the PO remains as rejected until they reduce the PO amount.  */  
   ApprovedAmount:number,
      /**  Indicates the Supplier will respond via Suppliers workbench  */  
   PostToWeb:boolean,
      /**  Date Buyer posted the PO  */  
   PostDate:string,
      /**  Vendor reference number.  */  
   VendorRefNum:string,
      /**  Indicated this PO requires a confirmation.  This would default yes for any Web Vendor  */  
   ConfirmReq:boolean,
      /**  Indicated Supplier Confirmed the PO  */  
   Confirmed:boolean,
      /**   Indicates if the Supplier has confirmed that they intend to fill the Order, and that it will be done through Supplier Connect("web"), 
phoned in a confirmation and clicked on the Confirmed checkbox in Epicor ("client"), or they clicked on the "Reject" checkbox in Supplier Connect("rejected").  */  
   ConfirmVia:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Linked to sales order.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Cross reference PO number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefPONum:string,
      /**  Consolidated PO flag.  Used in Consolidated Purchasing.  */  
   ConsolidatedPO:boolean,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Is this Purchase Order a Contract Purchase Order?  */  
   ContractOrder:boolean,
      /**  The date the Contract Purchase Order is active.  */  
   ContractStartDate:string,
      /**  The date the Contract Purchase Order expires.  */  
   ContractEndDate:string,
      /**  Print Header Address flag  */  
   PrintHeaderAddress:boolean,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  PO Type Identifier ('STD' - standard PO, 'CMI' - Customer managed inventory PO, or 'SMI' - Supplier managed inventory PO)  */  
   POType:string,
      /**  Letter of Credit ID.  */  
   APLOCID:string,
      /**  Transaction Document for the record.  */  
   TranDocTypeID:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  ICPOLocked  */  
   ICPOLocked:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Specifies the date by which you need to receive the whole Purchase Order. If you set the Due Date before create lines and releases, it will act as a default value when adding new lines/releases.  */  
   DueDate:string,
      /**  Specifies the date on which the supplier has promised to ship the whole Purchase Order. If you set the Promise Date before create lines and releases, it will act as a default value when adding releases.  */  
   PromiseDate:string,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date and time that the record was last changed.  */  
   ChangeDate:string,
      /**  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  */  
   POTaxReadyToProcess:boolean,
      /**  The Tax Liability for this Purchase Order  */  
   TaxRegionCode:string,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Total Tax amount for this PO in base currency, Totals the TaxAmt from the POTax records of this purchase order  */  
   TotalTax:number,
      /**  Total Tax amount for this PO in document currency, Totals the DocTaxAmt from the POTax records of this purchase order  */  
   DocTotalTax:number,
      /**  Total Tax amount for this PO in Rpt1 currency, Totals the Rpt1TaxAmt from the POTax records of this purchase order  */  
   Rpt1TotalTax:number,
      /**  Total Tax amount for this PO in Rpt2 currency, Totals the Rpt2TaxAmt from the POTax records of this purchase order  */  
   Rpt2TotalTax:number,
      /**  Total Tax amount for this PO in Rpt3 currency, Totals the Rpt3TaxAmt from the POTax records of this purchase order  */  
   Rpt3TotalTax:number,
      /**  Total Order Withholding Taxes in base currency  */  
   TotalWhTax:number,
      /**  Total Order Withholding Taxes in document currency  */  
   DocTotalWhTax:number,
      /**  Total Order Withholding Taxes in Rpt1 currency  */  
   Rpt1TotalWhTax:number,
      /**  Total Order Withholding Taxes in Rpt2 currency  */  
   Rpt2TotalWhTax:number,
      /**  Total Order Withholding Taxes in Rpt3 currency  */  
   Rpt3TotalWhTax:number,
      /**  Total Order Self Assessed Taxes in base currency.  */  
   TotalSATax:number,
      /**  Total Order Self Assessed Taxes in document currency.  */  
   DocTotalSATax:number,
      /**  Total Order Self Assessed Taxes in Rpt1 currency.  */  
   Rpt1TotalSATax:number,
      /**  Total Order Self Assessed Taxes in Rpt2 currency.  */  
   Rpt2TotalSATax:number,
      /**  Total Order Self Assessed Taxes in Rpt3 currency.  */  
   Rpt3TotalSATax:number,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   HdrTaxNoUpdt:boolean,
      /**  Tax Rate Group Code - FUTUREUSE  */  
   TaxRateGrpCode:string,
      /**  Total deductable tax amount in base currency.  */  
   TotalDedTax:number,
      /**  Total deductable tax amount in document currency.  */  
   DocTotalDedTax:number,
      /**  Total deductable tax amount in Rpt1 currency.  */  
   Rpt1TotalDedTax:number,
      /**  Total deductable tax amount in Rpt2 currency.  */  
   Rpt2TotalDedTax:number,
      /**  Total deductable tax amount in Rpt3 currency.  */  
   Rpt3TotalDedTax:number,
      /**  Total charge amount for the PO in base currency,  This is the sum of PODetail.ExtCost for non voided lines.  */  
   TotalCharges:number,
      /**  Total amount for all miscellaneous charges associated to this PO in base currency.  This is the sum of POMisc.MiscAmt.  */  
   TotalMiscCharges:number,
      /**  Total amount for the PO in base currency.  This is the sum of POMisc.MiscAmt + PODetail.ExtCost + POHeader.TotalTax.  */  
   TotalOrder:number,
      /**  Total charge amount for the PO in document currency,  This is the sum of PODetail.DocExtCost for non voided lines.  */  
   DocTotalCharges:number,
      /**  Total amount for all miscellaneous charges associated to this PO in document currency.  This is the sum of POMisc.DocMiscAmt.  */  
   DocTotalMisc:number,
      /**  Total amount for the PO in document currency.  This is the sum of POMisc.DocMiscAmt + PODetail.DocExtCost + POHeader.DocTotalTax.  */  
   DocTotalOrder:number,
      /**  Total charge amount for the PO in Rpt1 currency,  This is the sum of PODetail.Rpt1ExtCost for non voided lines.  */  
   Rpt1TotalCharges:number,
      /**  Total charge amount for the PO in Rpt2 currency,  This is the sum of PODetail.Rpt2ExtCost for non voided lines.  */  
   Rpt2TotalCharges:number,
      /**  Total charge amount for the PO in Rpt3 currency,  This is the sum of PODetail.Rpt3ExtCost for non voided lines.  */  
   Rpt3TotalCharges:number,
      /**  Total amount for all miscellaneous charges associated to this PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt.  */  
   Rpt1TotalMiscCharges:number,
      /**  Total amount for all miscellaneous charges associated to this PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt.  */  
   Rpt2TotalMiscCharges:number,
      /**  Total amount for all miscellaneous charges associated to this PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt.  */  
   Rpt3TotalMiscCharges:number,
      /**  Total amount for the PO in Rpt1 currency.  This is the sum of POMisc.Rpt1MiscAmt + PODetail.Rpt1ExtCost + POHeader.Rpt1TotalTax.  */  
   Rpt1TotalOrder:number,
      /**  Total amount for the PO in Rpt2 currency.  This is the sum of POMisc.Rpt2MiscAmt + PODetail.Rpt2ExtCost + POHeader.Rpt2TotalTax.  */  
   Rpt2TotalOrder:number,
      /**  Total amount for the PO in Rpt3 currency.  This is the sum of POMisc.Rpt3MiscAmt + PODetail.Rpt3ExtCost + POHeader.Rpt3TotalTax.  */  
   Rpt3TotalOrder:number,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  CNBonded  */  
   CNBonded:boolean,
      /**  EDI Revision number that marks changes in the purchase order since the last time the purchase order was sent.  */  
   EDIRevNum:number,
      /**  Flag used to mark the Purchase Order as posted to EDI  */  
   EDIPosted:boolean,
      /**  Date when the PO was last acknowledge from EDI Portal  */  
   EDIPostedDate:string,
      /**  Date when the PO was last acknowledge from EDI Portal  */  
   EDIAckDate:string,
      /**  Temporarily stores the return message from the PO approval process  */  
   ApproveMessage:string,
      /**  Used when switching the Vendor and need to prompt if the user wants to recalculate unit costs.  */  
   RecalcUnitCosts:boolean,
   RuleCode:number,
   UpdateDtlAndRelRecords:boolean,
   VendCntFaxNum:string,
   VendCntPhoneNumber:string,
   ApproveChkBxSensitive:boolean,
   BaseCurrencyID:string,
   ConfirmChkBxSensitive:boolean,
      /**  Flag for UI to know when to Enable/Disable the SupplierID field in POEntry  */  
   EnableSupplierID:boolean,
      /**  True is there are lines for this PO  */  
   HasLines:boolean,
   HoldChkBxSensitive:boolean,
   MassPrntChkBxSensitive:boolean,
   RefCodeCurrSymbol:string,
      /**  The formatted vendor address  */  
   VendAddrFormat:string,
   EDIEnable:boolean,
   BitFlag:number,
   APLOCDescription:string,
   BuyerIDName:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrencyID:string,
   FOBDescription:string,
   RateGrpDescription:string,
   ShipCountryNumDescription:string,
   ShipViaCodeInactive:boolean,
   ShipViaCodeDescription:string,
   ShipViaCodeWebDesc:string,
   TaxRegionCodeDescription:string,
   TermsCodeDescription:string,
   VendorVendorID:string,
   VendorZIP:string,
   VendorDefaultFOB:string,
   VendorCity:string,
   VendorName:string,
   VendorCountry:string,
   VendorAddress3:string,
   VendorTermsCode:string,
   VendorAddress1:string,
   VendorAddress2:string,
   VendorCurrencyCode:string,
   VendorState:string,
   VendorEDISupplier:boolean,
   VendorCntName:string,
   VendorCntEmailAddress:string,
   VendorCntPhoneNum:string,
   VendorCntFaxNum:string,
   VendorPPAddress3:string,
   VendorPPCountry:string,
   VendorPPZip:string,
   VendorPPState:string,
   VendorPPAddress1:string,
   VendorPPName:string,
   VendorPPPrimPCon:number,
   VendorPPAddress2:string,
   VendorPPCity:string,
   XbSystAllowLinkedPOChg:boolean,
   XbSystPOUserInt2Label:string,
   XbSystPOUserDate3Label:string,
   XbSystPOUserChar3Label:string,
   XbSystPOUserChar4Label:string,
   XbSystPOUserChar2Label:string,
   XbSystPOUserDate2Label:string,
   XbSystPOUserInt1Label:string,
   XbSystPOUserDec1Label:string,
   XbSystPOUserDec2Label:string,
   XbSystPOUserDate4Label:string,
   XbSystPOUserDate1Label:string,
   XbSystPOUserChar1Label:string,
   XbSystDisableOverridePriceListOption:boolean,
   XbSystPOTaxCalculate:boolean,
   XbSystAPTaxLnLevel:boolean,
      /**  RowMod  */  
   RowMod:string,
   UD_SysRevID:string,
   PrePaymentFlag_c:boolean,
   PrePaymentTerms_c:string,
   ProductFamily_c:string,
   VendorConfirmationNo_c:string,
   POTerms_c:string,
}

export interface Erp_Tablesets_POHeaderTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Purchase order number that uniquely identifies the purchase order.  */  
   PONum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  The reportable sales amount to the tax jurisdiction. Set the value as follows; first determine if the item needs to be reported to the tax jurisdiction.  This is done by using the  APInvDtl.TaxCode and APInvDtl/APInvMisc.TaxCat to find a record in the SalesTxC. If a record is not found or SalesTxC.Reportable = Yes then add in the line item extended amount or if this is for a InvcMisc record InvcMisc.Amount. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcReportableAmt.  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last changed (seconds since midnight)  */  
   ChangeTime:number,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Collection Type  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution Date  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  TextCode  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  flag to indicate if this record is used only to total detail records,  */  
   SummaryOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   EnableSuperGRate:boolean,
   Rpt1ScrDedTaxAmt:number,
      /**  Display field for Rpt1ScrFixedAmount  */  
   Rpt1ScrFixedAmount:number,
   ScrDedTaxAmt:number,
   ScrDocDedTaxAmt:number,
      /**  Doc Fixed Amount  */  
   ScrDocFixedAmount:number,
   ScrDocReportableAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
      /**  Display field for Rpt2FixedAmount  */  
   Rpt2ScrFixedAmount:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
      /**  Display field for Rpt3rFixedAmount  */  
   Rpt3ScrFixedAmount:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDocTaxableAmt:number,
   ScrDocTaxAmt:number,
   ScrDocTaxAmtVar:number,
      /**  FixedAmount  */  
   ScrFixedAmount:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POMiscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Purchase order number that this miscellaneous record is related to.  */  
   PONum:number,
      /**  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when they requested miscellaneous maintenance.  */  
   POLine:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the PO. The default is provided by PurMisc.Description, but it is overridable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   MiscAmt:number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   DocMiscAmt:number,
      /**  Sets the miscellaneous line as being taxable. This is used to pass along to invoice processing.  */  
   Taxable:boolean,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   InvoicedAmt:number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   DocInvoicedAmt:number,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Order Misc Seq Num created for this PO Misc Seq Num for the Inter-Company Trading.  */  
   OrderSeqNum:number,
      /**  Linked to sales order misc charge.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Reporting currency value of this field  */  
   Rpt1InvoicedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoicedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoicedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   InMiscAmt:number,
      /**  The Customer Currency amount of the Miscellaneous Charge/Credit. Can't be zero.  */  
   DocInMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InMiscAmt:number,
      /**  Amount invoiced against this POMisc record. This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   InInvoiceAmt:number,
      /**  Amount invoiced against this POMisc record(Customer Currency). This is provided so that during the A/P invoicing process the entry person can see the POMisc records with their planned and invoiced amounts. This is updated via A/P invoice entry.  */  
   DocInInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InInvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InInvoiceAmt:number,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True the tax engine will not calculate any miscellaneous charge tax information  */  
   NoTaxRecalc:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrencySymbol:string,
   DocCurrencySymbol:string,
   POHeaderApprove:boolean,
   Rpt1ScrMiscAmt:number,
   Rpt2ScrMiscAmt:number,
   Rpt3ScrMiscAmt:number,
   ScrDocMiscAmt:number,
   ScrMiscAmt:number,
      /**  Description of Tax ID  */  
   TaxIDDescription:string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   DocTotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   DocTotalSATax:number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   DocTotalTax:number,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   Rpt1TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   Rpt2TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   Rpt3TotalTax:number,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   TotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   TotalSATax:number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   TotalTax:number,
   BitFlag:number,
   MiscCodeLCCurrencyCode:string,
   MiscCodeLCAmount:number,
   MiscCodeDescription:string,
   MiscCodeLCDisburseMethod:string,
   MiscCodeTaxCatID:string,
   PONumInPrice:boolean,
   PONumShipName:string,
   PONumShipToConName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POReceiptsRow{
   Company:string,
   ContainerID:number,
   ContainerLCAmt:number,
   CurrencyCode:string,
   DropShip:boolean,
   DueDate:string,
   IUM:string,
   LCFlag:boolean,
   Ontime:string,
   OpenRelease:boolean,
   OurRemQty:number,
   PackLine:number,
   PackSlip:string,
   PartNum:string,
   PONum:number,
   POLine:number,
   PORelNum:number,
   PUM:string,
   PurPoint:string,
   ReceiptDate:string,
   RemainingSMIQty:number,
   VendorNum:number,
   VendorNumName:string,
   VenRemQty:number,
   RevisionNum:string,
   PartDescription:string,
   OurQty:number,
   Invoiced:boolean,
   Volume:number,
   InvoiceNum:string,
   InvoiceLine:number,
   VenPartNum:string,
   VendorQty:number,
   OurUnitCost:number,
   LCSpecLineDutyAmt:number,
   AppliedRcptLCAmt:number,
   LCUpliftIndCost:number,
   LCAmt:number,
   AppliedLCVariance:number,
   LCMtlBurUnitCost:number,
   ArrivedDate:string,
   DocVendorUnitCost:number,
   ThisTranQty:number,
   ThisTranUOM:string,
   EnableInventoryAttributes:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   TrackInventoryAttributes:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POReceiptsTableset{
   POReceipts:Erp_Tablesets_POReceiptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PORelAttchRow{
   Company:string,
   PONum:number,
   POLine:number,
   PORelNum:number,
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

export interface Erp_Tablesets_PORelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  */  
   VoidRelease:boolean,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   DueDate:string,
      /**  Order quantity for this release in our unit of measure.  */  
   XRelQty:number,
      /**   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  */  
   PurchasingFactor:number,
      /**  Order quantity for this release in vendors unit of measure.  */  
   RelQty:number,
      /**  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  */  
   JobNum:string,
      /**  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  */  
   AssemblySeq:number,
      /**   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Warehouse that the item on this release is being purchased for.  */  
   WarehouseCode:string,
      /**  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  */  
   ReceivedQty:number,
      /**  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  */  
   ExpOverride:boolean,
      /**  Requisition which generated this PORel record.  */  
   ReqNum:number,
      /**  Requisition line which generated this PORel record.  */  
   ReqLine:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  */  
   PromiseDt:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  */  
   Confirmed:boolean,
      /**  Can be "web", "client", or "rejected"  */  
   ConfirmVia:string,
      /**   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  */  
   ReqChgDate:string,
      /**   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  */  
   ReqChgQty:number,
      /**  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  */  
   LockRel:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  */  
   RefDisplayAccount:string,
      /**  Link to the related GLRefTyp.RefType. Not displayed.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   RefCodeDesc:string,
      /**  Order number created for this PO for the Inter-Company Trading.  */  
   OrderNum:number,
      /**  Order Line created for this PO Line for the Inter-Company Trading.  */  
   OrderLine:number,
      /**  Order Release Line created for this PO Release for the Inter-Company Trading.  */  
   OrderRelNum:number,
      /**  Linked to sales order release.  */  
   Linked:boolean,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  */  
   ShippedQty:number,
      /**   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  */  
   TranType:string,
      /**  Global Company identifier.  Used in Consolidated Purchasing.  */  
   GlbCompany:string,
      /**  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  */  
   GlbPlant:string,
      /**  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  */  
   GlbWarehouse:string,
      /**  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  */  
   GlbCreateJobMtl:boolean,
      /**  Shipped Date  */  
   ShippedDate:string,
      /**  ID field to the ContainerHeader table.  */  
   ContainerID:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   PurchasingFactorDirection:string,
      /**  This field holds the previous value of Due Date.  */  
   PreviousDueDate:string,
      /**  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  */  
   BaseQty:number,
      /**   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  */  
   BaseUOM:string,
      /**  Order Num related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderNum:number,
      /**  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderLine:number,
      /**  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  */  
   BTOOrderRelNum:number,
      /**  The value of this field comes from the sales order release. Used only for Buy To Order POs.  */  
   DropShip:boolean,
      /**  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  */  
   ShipToNum:string,
      /**  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  */  
   SoldToNum:number,
      /**  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  */  
   SMIRcvdQty:number,
      /**  Contains the key value for the shipping contact.  */  
   ShpConNum:number,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  */  
   MangCustNum:number,
      /**  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  */  
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
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipping Country Number  */  
   OTSCountryNum:number,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Open Purchase Release flag  */  
   PORelOpen:boolean,
      /**  Mapping  */  
   Mapping:boolean,
      /**  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  */  
   PhaseID:string,
      /**  Project Phase ID  */  
   WBSPhaseID:string,
      /**  IsMultiRel  */  
   IsMultiRel:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Field to track the SMIRcvdQty that has not yet been moved to stock  */  
   SMIRemQty:number,
      /**  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  */  
   LockQty:boolean,
      /**  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  */  
   LockDate:boolean,
      /**  Indicates Due Date has been changed.  */  
   DueDateChanged:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  */  
   Status:string,
      /**  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  */  
   ArrivedQty:number,
      /**  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  */  
   InvoicedQty:number,
      /**  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  */  
   NeedByDate:string,
      /**  Set to 'true' if 'NeedByDate' was derived from a valid demand.  */  
   LockNeedByDate:boolean,
      /**  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  */  
   InspectionQty:number,
      /**  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  */  
   FailedQty:number,
      /**  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  */  
   PassedQty:number,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   ProjProcessed:boolean,
      /**  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  */  
   DeliverTo:string,
      /**  Taxable  */  
   Taxable:boolean,
      /**  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  */  
   TaxExempt:string,
      /**  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  */  
   NoTaxRecalc:boolean,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  When the Promise Date is changed, this is the previous PromiseDt  */  
   ReqChgPromiseDate:string,
      /**  One Time ShipTo email address.  */  
   OTSEMailAddress:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Indicates if this release is  "FIRM".  */  
   FirmRelease:boolean,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  Name of the ship reference that is going to be stored.  */  
   EDIShipReferenceType:string,
      /**  Data that is going to be stored as ship reference.  */  
   EDIShipReferenceData:string,
      /**  Estimated time when the shipment will arrive.  */  
   EDIEstimatedDockDate:string,
      /**  Quantity sent by the supplier.  */  
   EDIShipQty:number,
      /**  Unit of Measure of the EDIShipQty.  */  
   EDIShipQtyUOM:string,
   ConsolidatedPO:boolean,
      /**  Is this Release related to a Contract Purchase Order?  */  
   ContractOrder:boolean,
   DelPoSug:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
      /**  Total deductable tax amount for this PO Line in document currency.  */  
   DocTotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in document currency.  */  
   DocTotalSATax:number,
      /**  Total Tax amount for this PO Line in document currency.  */  
   DocTotalTax:number,
      /**  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  */  
   EnableBTOOrderNum:boolean,
      /**  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  */  
   EnableGLAcct:boolean,
   EstUnitCost:number,
   ExpDesc:string,
   FromPOSugChg:boolean,
   GlbPlantName:string,
   GlbWhseName:string,
   Inspection:boolean,
   IUM:string,
      /**  This field will be used in the UI to Lock and unLock a release.  */  
   Lock:boolean,
      /**  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  */  
   MangCustID:string,
      /**  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  */  
   MangCustName:string,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
      /**  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  */  
   OrderHeld:boolean,
   POHeaderApprove:boolean,
      /**  Identifies the type of PO  */  
   POType:string,
      /**  Replicate PUM on detail  */  
   PUM:string,
      /**  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  */  
   PurPoint:string,
   RefCodeStatus:string,
      /**  Total deductable tax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  */  
   Rpt1TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt1 currency,  */  
   Rpt1TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  */  
   Rpt2TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt2 currency,  */  
   Rpt2TotalTax:number,
      /**  Total Deductable tax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalDedTax:number,
      /**  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  */  
   Rpt3TotalSATax:number,
      /**  Total Tax amount for this PO Line in Rpt3 currency,  */  
   Rpt3TotalTax:number,
   ShipToAddressList:string,
      /**  Description text of the Status field  */  
   StatusDescription:string,
      /**  Total deductable tax amount for this PO Line in base currency.  */  
   TotalDedTax:number,
      /**  Total Order Self Assessed Taxes for this PO Line in base currency.  */  
   TotalSATax:number,
      /**  Total Tax amount for this PO Line in base currency,  */  
   TotalTax:number,
      /**   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  */  
   TranTypeDesc:string,
      /**  Indicates if Glb fields should be used in place of the non-global equivalent  */  
   UseGlbFields:boolean,
      /**  Related Supplier ID  */  
   VendorID:string,
      /**  Related Vendor Name  */  
   VendorName:string,
      /**  Logical indicating if the container has been shipped.  */  
   ContainerShipped:boolean,
      /**  The formatted ship to address  */  
   ShipToAddrFormatted:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  */  
   TrackInventoryAttributes:boolean,
      /**  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  */  
   EnableDynAttrButton:boolean,
      /**  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  */  
   AttributeQtyMismatch:boolean,
   JobMtlSeq:number,
   JobOprSeq:number,
   TrackInventoryByRevision:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   ContainerHeaderPromiseDate:string,
   ContainerHeaderDueDate:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   PlantName:string,
   POLineRevisionNum:string,
   POLineLineDesc:string,
   POLineVenPartNum:string,
   POLinePartNum:string,
   PONumShipName:string,
   PONumShipToConName:string,
   ProjectIDDescription:string,
   ReqLineLineDesc:string,
   ReqNumShipName:string,
   ReqNumShipToConName:string,
   ShipToCustNumInactive:boolean,
   ShipToCustNumBTName:string,
   ShipToCustNumCustID:string,
   ShipToCustNumName:string,
   ShipToNumInactive:boolean,
   SoldToNumCustID:string,
   SoldToNumBTName:string,
   SoldToNumName:string,
   SoldToNumInactive:boolean,
   WarehouseCodeDescription:string,
   WBSPhaseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PORelTGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  */  
   TGLCTranNum:number,
      /**  String identifier of the account context.  */  
   GLAcctContext:string,
      /**  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  */  
   BookID:string,
      /**  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  */  
   COACode:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   GLAccount:string,
      /**  Indicates if the user can update or delete this record.  */  
   UserCanModify:boolean,
      /**  Segement Value 1 of the account for this context.  */  
   SegValue1:string,
      /**  Segement Value 2 of the account for this context.  */  
   SegValue2:string,
      /**  Segement Value 3 of the account for this context.  */  
   SegValue3:string,
      /**  Segement Value 4 of the account for this context.  */  
   SegValue4:string,
      /**  Segement Value 5 of the account for this context.  */  
   SegValue5:string,
      /**  Segement Value 6 of the account for this context.  */  
   SegValue6:string,
      /**  Segement Value 7 of the account for this context.  */  
   SegValue7:string,
      /**  Segement Value 8 of the account for this context.  */  
   SegValue8:string,
      /**  Segement Value 9 of the account for this context.  */  
   SegValue9:string,
      /**  Segement Value 10 of the account for this context.  */  
   SegValue10:string,
      /**  Segement Value 11 of the account for this context.  */  
   SegValue11:string,
      /**  Segement Value 12 of the account for this context.  */  
   SegValue12:string,
      /**  Segement Value 13 of the account for this context.  */  
   SegValue13:string,
      /**  Segement Value 14 of the account for this context.  */  
   SegValue14:string,
      /**  Segement Value 15 of the account for this context.  */  
   SegValue15:string,
      /**  Segement Value 16 of the account for this context.  */  
   SegValue16:string,
      /**  Segement Value 17 of the account for this context.  */  
   SegValue17:string,
      /**  Segement Value 18 of the account for this context.  */  
   SegValue18:string,
      /**  Segement Value 19 of the account for this context.  */  
   SegValue19:string,
      /**  Segement Value 20 of the account for this context.  */  
   SegValue20:string,
      /**  Unique Identifier of the system GL Control Type.  */  
   SysGLControlType:string,
      /**  System generated GL Control Identifier.  */  
   SysGLControlCode:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Fiscal year of the related GLJrnDtl.  */  
   FiscalYear:number,
      /**  JournalCode of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Journal number of the related GLJrnDtl.  */  
   JournalNum:number,
      /**  JournalLine of the related GLJrnDtl.  */  
   JournalLine:number,
      /**  Transaction date of the transaction.  This is used in order to display the transactions in date order.  */  
   TranDate:string,
      /**   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  */  
   TranSource:string,
      /**  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  */  
   LaborDtlSeq:number,
      /**  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysDate:string,
      /**  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   SysTime:number,
      /**  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  */  
   TranNum:number,
      /**  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  */  
   ARInvoiceNum:number,
      /**  Transaction amount that this transaction posted to the related GlJrnDtl.  */  
   TransAmt:number,
      /**  Invoice Line Number associated with this GL Journal  */  
   InvoiceLine:number,
      /**  The sequence number associated with this GL journal  */  
   SeqNum:number,
      /**  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  */  
   VendorNum:number,
      /**  Vendor's invoice number.  */  
   APInvoiceNum:string,
      /**  Date record was created  */  
   CreateDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  BookCreditAmount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  A unique code that identifies the document currency.  */  
   CurrencyCode:string,
      /**   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  */  
   RecordType:string,
      /**  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  */  
   CorrAccUID:number,
      /**  this field equals ABTUID which was created during posting  */  
   ABTUID:string,
      /**  Technical identifier.  */  
   RuleUID:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  IsModifiedByUser  */  
   IsModifiedByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MovementNum  */  
   MovementNum:number,
      /**  MovementType  */  
   MovementType:string,
      /**  Plant  */  
   Plant:string,
      /**  POLine of PORel  */  
   POLine:number,
      /**  PONum of PORel  */  
   PONum:number,
      /**  PORelNum of PORel  */  
   PORelNum:number,
   ReqRef:boolean,
      /**  Indicates if the user selected a different account from the default.  */  
   AcctOverride:boolean,
      /**  Column used to know if the book assigned is the Main Book.  */  
   IsMainBook:boolean,
   BitFlag:number,
   COADescription:string,
   GLAccountAccountDesc:string,
   GLAccountGLAcctDisp:string,
   GLAccountGLShortAcct:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PORelTaxRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  */  
   TaxCode:string,
      /**  Tax Rate Code.  */  
   RateCode:string,
      /**  Used to allow a second tax record using the same tax code on an invoice.  When the sales tax field EcAquisition is checked then 2 invoice tax records are created.  */  
   ECAcquisitionSeq:number,
      /**  ReportableAmt  */  
   ReportableAmt:number,
      /**  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency. Manually entered if APInvTax.Manual = Yes else set equal to SysCalcDocTaxableAmt.  */  
   DocReportableAmt:number,
      /**  Taxable amount for this invoice.  Manually entered if APInvTax.Manual = Yes else set equal to SysCalcTaxableAmt.  */  
   TaxableAmt:number,
      /**  Taxable amount for this invoice in foreign currency. Manually entered if APInvTax.Manual = Yes else it is set equal to SysCalcDocTaxableAmt.  */  
   DocTaxableAmt:number,
      /**  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  */  
   Percent:number,
      /**  Sales Tax amount for the corresponding taxable sales amount.  */  
   TaxAmt:number,
      /**  Sales Tax amount for the corresponding taxable sales amount in foreign currency.  */  
   DocTaxAmt:number,
      /**  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  */  
   Manual:boolean,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last changed (seconds since midnight)  */  
   ChangeTime:number,
      /**  Indicates if this tax line is for a Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ReportableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  CollectionType  */  
   CollectionType:number,
      /**  Timing of when to report taxes  */  
   Timing:number,
      /**  Exemption Type  */  
   ExemptType:number,
      /**  Exemption Percent  */  
   ExemptPercent:number,
      /**  Resolution Number  */  
   ResolutionNum:string,
      /**  Resolution date.  */  
   ResolutionDate:string,
      /**  Date to determine the tax rate.  */  
   TaxRateDate:string,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DefTaxableAmt:number,
      /**  Balance of the Taxable amount that has been deferred until payment  */  
   DocDefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxableAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxableAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DefTaxAmt:number,
      /**  Balance of the Tax amount that has been deferred until payment  */  
   DocDefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DefTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DefTaxAmt:number,
      /**  This record was manually added (not in Liability) but will use the standard calculations  */  
   ManAdd:boolean,
      /**  Deducatable Tax Amount  */  
   DedTaxAmt:number,
      /**  Deducatable Tax Amount  */  
   DocDedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2DedTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3DedTaxAmt:number,
      /**  Fixed Tax Amount  */  
   FixedAmount:number,
      /**  Document Fixed Tax Amount  */  
   DocFixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2FixedAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3FixedAmount:number,
      /**  Unique Identifier for Legal Text  */  
   TextCode:string,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   TaxAmtVar:number,
      /**  Difference between tax calculated in document rate less tax calculated in tax rate  */  
   DocTaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmtVar:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmtVar:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencySwitch:boolean,
   CurrencyCode:string,
   DocScrDedTaxAmt:number,
   DocScrReportableAmt:number,
   DocScrTaxableAmt:number,
   DocScrTaxAmt:number,
   DocScrTaxAmtVar:number,
   Rpt1ScrDedTaxAmt:number,
   Rpt1ScrReportableAmt:number,
   Rpt1ScrTaxableAmt:number,
   Rpt1ScrTaxAmt:number,
   Rpt1ScrTaxAmtVar:number,
   Rpt2ScrDedTaxAmt:number,
   Rpt2ScrReportableAmt:number,
   Rpt2ScrTaxableAmt:number,
   Rpt2ScrTaxAmt:number,
   Rpt2ScrTaxAmtVar:number,
   Rpt3ScrDedTaxAmt:number,
   Rpt3ScrReportableAmt:number,
   Rpt3ScrTaxableAmt:number,
   Rpt3ScrTaxAmt:number,
   Rpt3ScrTaxAmtVar:number,
   ScrDedTaxAmt:number,
   ScrReportableAmt:number,
   ScrTaxableAmt:number,
   ScrTaxAmt:number,
   ScrTaxAmtVar:number,
   DocScrFixedAmount:number,
   Rpt1ScrFixedAmount:number,
   Rpt2ScrFixedAmount:number,
   Rpt3ScrFixedAmount:number,
      /**  Display Fixed Amount in base currency.  */  
   ScrFixedAmount:number,
      /**  Collection Type Description  */  
   DescCollectionType:string,
   BitFlag:number,
   RateCodeDescription:string,
   TaxCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POTableset{
   POHeader:Erp_Tablesets_POHeaderRow[],
   POHeaderAttch:Erp_Tablesets_POHeaderAttchRow[],
   PODetail:Erp_Tablesets_PODetailRow[],
   PODetailAttch:Erp_Tablesets_PODetailAttchRow[],
   PORel:Erp_Tablesets_PORelRow[],
   PORelAttch:Erp_Tablesets_PORelAttchRow[],
   PORelTax:Erp_Tablesets_PORelTaxRow[],
   PORelTGLC:Erp_Tablesets_PORelTGLCRow[],
   PODetailInsp:Erp_Tablesets_PODetailInspRow[],
   PODetailTax:Erp_Tablesets_PODetailTaxRow[],
   POMisc:Erp_Tablesets_POMiscRow[],
   PODetailMiscTax:Erp_Tablesets_PODetailMiscTaxRow[],
   POHeadMisc:Erp_Tablesets_POHeadMiscRow[],
   POHeaderMiscTax:Erp_Tablesets_POHeaderMiscTaxRow[],
   POHeaderTax:Erp_Tablesets_POHeaderTaxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartSubsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Part number that this substitute Part is for.  */  
   PartNum:string,
      /**  Substitute Part  */  
   SubPart:string,
      /**  Indicates the record type. "S" = Substitute, "C" = Compliment  */  
   RecType:string,
      /**  Pertains only to Substitute Parts (RecType = "S"). Values are "C" - Comparable, "D" - Downgrade, "U" - Upgrade  */  
   SubType:string,
      /**   The quantity of the alternate part per 1 of the parent part in the parents base inventory uom. Cannot be zero.
To convert an existing OrderDtl.SellingQty to a PartSubs. It is converted to the Parents Part Base Inventory UOM  then multiply PartSubs.QtyPer, then converted to  PartSub.SalesUM.  */  
   QtyPer:number,
      /**  Selling Unit of measure used when this part is used as a substitute/compliment with the parent part (partsubs.partnum).  Defaults as Part.SUM of the PartSub.SubPart.  */  
   SalesUM:string,
      /**  Optional Comment  */  
   Comment:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DefaultSub:boolean,
      /**  Price for the Suggested Quantity  */  
   Price:number,
      /**  Suggested Quantity  */  
   SuggestedQty:number,
      /**  Selected Row  */  
   Selected:boolean,
      /**  Suggested Quantity for Order Qty in Quote Detail  */  
   SugOrderQty:number,
   BitFlag:number,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   SubPartSellingFactor:number,
   SubPartTrackSerialNum:boolean,
   SubPartTrackDimension:boolean,
   SubPartPartDescription:string,
   SubPartIUM:string,
   SubPartSalesUM:string,
   SubPartTrackLots:boolean,
   SubPartPricePerCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartSubsTableset{
   PartSubs:Erp_Tablesets_PartSubsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPOTableset{
   POHeader:Erp_Tablesets_POHeaderRow[],
   POHeaderAttch:Erp_Tablesets_POHeaderAttchRow[],
   PODetail:Erp_Tablesets_PODetailRow[],
   PODetailAttch:Erp_Tablesets_PODetailAttchRow[],
   PORel:Erp_Tablesets_PORelRow[],
   PORelAttch:Erp_Tablesets_PORelAttchRow[],
   PORelTax:Erp_Tablesets_PORelTaxRow[],
   PORelTGLC:Erp_Tablesets_PORelTGLCRow[],
   PODetailInsp:Erp_Tablesets_PODetailInspRow[],
   PODetailTax:Erp_Tablesets_PODetailTaxRow[],
   POMisc:Erp_Tablesets_POMiscRow[],
   PODetailMiscTax:Erp_Tablesets_PODetailMiscTaxRow[],
   POHeadMisc:Erp_Tablesets_POHeadMiscRow[],
   POHeaderMiscTax:Erp_Tablesets_POHeaderMiscTaxRow[],
   POHeaderTax:Erp_Tablesets_POHeaderTaxRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param poAPLOCID
      @param ds
   */  
export interface GetAPLOCDescription_input{
      /**  Proposed newPOType to be validated  */  
   poAPLOCID:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface GetAPLOCDescription_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param sourceSysRowID
   */  
export interface GetBasePartAndConfigType_input{
      /**  PODetail sysrowid  */  
   sourceSysRowID:string,
}

export interface GetBasePartAndConfigType_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
   configType:string,
   configURL:string,
   configID:string,
}
}

   /** Required : 
      @param sourceSysRowID
   */  
export interface GetBasePartForConfig_input{
      /**  Order Number of the target Assembly  */  
   sourceSysRowID:string,
}

export interface GetBasePartForConfig_output{
parameters : {
      /**  output parameters  */  
   cfgPartNum:string,
   cfgRevisionNum:string,
}
}

   /** Required : 
      @param poNum
   */  
export interface GetByID_input{
   poNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The TableName  */  
   tableName:string,
      /**  The Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
      /**  description List  */  
   returnObj:string,
}

export interface GetCurrencyBase_output{
parameters : {
      /**  output parameters  */  
   opCurrencyBase:string,
}
}

export interface GetDefaultBuyer_output{
      /**  Returns true if default buyer was found  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   buyerID:string,
   buyerIDName:string,
}
}

   /** Required : 
      @param pPONum
      @param ds
   */  
export interface GetDefaultGLAccountAllPOReleases_input{
   pPONum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface GetDefaultGLAccountAllPOReleases_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param pPONum
      @param pPOLine
      @param pPORelNum
      @param ds
   */  
export interface GetDefaultGLAccount_input{
   pPONum:number,
   pPOLine:number,
   pPORelNum:number,
   ds:Erp_Tablesets_POTableset[],
}

export interface GetDefaultGLAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetDropShipPOHeaderList_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetDropShipPOHeaderList_output{
   returnObj:Erp_Tablesets_POHeaderListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetGlbCompanyList_output{
parameters : {
      /**  output parameters  */  
   GlbCompanyList:string,
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
   returnObj:Erp_Tablesets_POHeaderListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewConsolidatedPO_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface GetNewConsolidatedPO_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewContractPO_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface GetNewContractPO_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNUM
      @param poLine
   */  
export interface GetNewPODetailAttch_input{
   ds:Erp_Tablesets_POTableset[],
   poNUM:number,
   poLine:number,
}

export interface GetNewPODetailAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNUM
      @param poLine
   */  
export interface GetNewPODetailInsp_input{
   ds:Erp_Tablesets_POTableset[],
   poNUM:number,
   poLine:number,
}

export interface GetNewPODetailInsp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNUM
      @param poLine
      @param seqNum
      @param taxCode
      @param rateCode
   */  
export interface GetNewPODetailMiscTax_input{
   ds:Erp_Tablesets_POTableset[],
   poNUM:number,
   poLine:number,
   seqNum:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewPODetailMiscTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
      @param taxCode
      @param rateCode
   */  
export interface GetNewPODetailTax_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   poLine:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewPODetailTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNUM
   */  
export interface GetNewPODetail_input{
   ds:Erp_Tablesets_POTableset[],
   poNUM:number,
}

export interface GetNewPODetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
   */  
export interface GetNewPOHeadMisc_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   poLine:number,
}

export interface GetNewPOHeadMisc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
   */  
export interface GetNewPOHeaderAttch_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
}

export interface GetNewPOHeaderAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param seqNum
      @param taxCode
      @param rateCode
   */  
export interface GetNewPOHeaderMiscTax_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   seqNum:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewPOHeaderMiscTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param taxCode
      @param rateCode
   */  
export interface GetNewPOHeaderTax_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewPOHeaderTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPOHeader_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface GetNewPOHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
   */  
export interface GetNewPOMisc_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   poLine:number,
}

export interface GetNewPOMisc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface GetNewPORelAttch_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface GetNewPORelAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
      @param poRelNum
   */  
export interface GetNewPORelTGLC_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   poLine:number,
   poRelNum:number,
}

export interface GetNewPORelTGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
      @param poRelNum
      @param taxCode
      @param rateCode
   */  
export interface GetNewPORelTax_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   poLine:number,
   poRelNum:number,
   taxCode:string,
   rateCode:string,
}

export interface GetNewPORelTax_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param poNum
      @param poLine
   */  
export interface GetNewPORel_input{
   ds:Erp_Tablesets_POTableset[],
   poNum:number,
   poLine:number,
}

export interface GetNewPORel_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ipPONum
   */  
export interface GetPOReceipts_input{
      /**  PONum.  */  
   ipPONum:number,
}

export interface GetPOReceipts_output{
   returnObj:Erp_Tablesets_POReceiptsTableset[],
}

   /** Required : 
      @param poNum
      @param maxNumOfCards
   */  
export interface GetPORelationshipMap_input{
   poNum:number,
   maxNumOfCards:number,
}

export interface GetPORelationshipMap_output{
   returnObj:string,
}

   /** Required : 
      @param PartNum
      @param pageSize
      @param absolutePage
   */  
export interface GetPartSubList_input{
      /**  The part number  */  
   PartNum:string,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface GetPartSubList_output{
   returnObj:Erp_Tablesets_PartSubsTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPartNum
   */  
export interface GetPlantsForPart_input{
      /**  Part Number  */  
   ipPartNum:string,
}

export interface GetPlantsForPart_output{
parameters : {
      /**  output parameters  */  
   opPlantList:string,
}
}

   /** Required : 
      @param whereClausePOHeader
      @param whereClausePOHeaderAttch
      @param whereClausePODetail
      @param whereClausePODetailAttch
      @param whereClausePORel
      @param whereClausePORelAttch
      @param whereClausePORelTax
      @param whereClausePORelTGLC
      @param whereClausePODetailInsp
      @param whereClausePODetailTax
      @param whereClausePOMisc
      @param whereClausePODetailMiscTax
      @param whereClausePOHeadMisc
      @param whereClausePOHeaderMiscTax
      @param whereClausePOHeaderTax
      @param invoiceNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForAPInvoice_input{
   whereClausePOHeader:string,
   whereClausePOHeaderAttch:string,
   whereClausePODetail:string,
   whereClausePODetailAttch:string,
   whereClausePORel:string,
   whereClausePORelAttch:string,
   whereClausePORelTax:string,
   whereClausePORelTGLC:string,
   whereClausePODetailInsp:string,
   whereClausePODetailTax:string,
   whereClausePOMisc:string,
   whereClausePODetailMiscTax:string,
   whereClausePOHeadMisc:string,
   whereClausePOHeaderMiscTax:string,
   whereClausePOHeaderTax:string,
   invoiceNum:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForAPInvoice_output{
   returnObj:Erp_Tablesets_POTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePOHeader
      @param whereClausePOHeaderAttch
      @param whereClausePODetail
      @param whereClausePODetailAttch
      @param whereClausePORel
      @param whereClausePORelAttch
      @param whereClausePORelTax
      @param whereClausePORelTGLC
      @param whereClausePODetailInsp
      @param whereClausePODetailTax
      @param whereClausePOMisc
      @param whereClausePODetailMiscTax
      @param whereClausePOHeadMisc
      @param whereClausePOHeaderMiscTax
      @param whereClausePOHeaderTax
      @param headNum
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForPayment_input{
   whereClausePOHeader:string,
   whereClausePOHeaderAttch:string,
   whereClausePODetail:string,
   whereClausePODetailAttch:string,
   whereClausePORel:string,
   whereClausePORelAttch:string,
   whereClausePORelTax:string,
   whereClausePORelTGLC:string,
   whereClausePODetailInsp:string,
   whereClausePODetailTax:string,
   whereClausePOMisc:string,
   whereClausePODetailMiscTax:string,
   whereClausePOHeadMisc:string,
   whereClausePOHeaderMiscTax:string,
   whereClausePOHeaderTax:string,
   headNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForPayment_output{
   returnObj:Erp_Tablesets_POTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePOHeader
      @param whereClausePOHeaderAttch
      @param whereClausePODetail
      @param whereClausePODetailAttch
      @param whereClausePORel
      @param whereClausePORelAttch
      @param whereClausePORelTax
      @param whereClausePORelTGLC
      @param whereClausePODetailInsp
      @param whereClausePODetailTax
      @param whereClausePOMisc
      @param whereClausePODetailMiscTax
      @param whereClausePOHeadMisc
      @param whereClausePOHeaderMiscTax
      @param whereClausePOHeaderTax
      @param vendorNum
      @param purPoint
      @param packSlip
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsForReceipt_input{
   whereClausePOHeader:string,
   whereClausePOHeaderAttch:string,
   whereClausePODetail:string,
   whereClausePODetailAttch:string,
   whereClausePORel:string,
   whereClausePORelAttch:string,
   whereClausePORelTax:string,
   whereClausePORelTGLC:string,
   whereClausePODetailInsp:string,
   whereClausePODetailTax:string,
   whereClausePOMisc:string,
   whereClausePODetailMiscTax:string,
   whereClausePOHeadMisc:string,
   whereClausePOHeaderMiscTax:string,
   whereClausePOHeaderTax:string,
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsForReceipt_output{
   returnObj:Erp_Tablesets_POTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePOHeader
      @param whereClausePOHeaderAttch
      @param whereClausePODetail
      @param whereClausePODetailAttch
      @param whereClausePORel
      @param whereClausePORelAttch
      @param whereClausePORelTax
      @param whereClausePORelTGLC
      @param whereClausePODetailInsp
      @param whereClausePODetailTax
      @param whereClausePOMisc
      @param whereClausePODetailMiscTax
      @param whereClausePOHeadMisc
      @param whereClausePOHeaderMiscTax
      @param whereClausePOHeaderTax
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePOHeader:string,
   whereClausePOHeaderAttch:string,
   whereClausePODetail:string,
   whereClausePODetailAttch:string,
   whereClausePORel:string,
   whereClausePORelAttch:string,
   whereClausePORelTax:string,
   whereClausePORelTGLC:string,
   whereClausePODetailInsp:string,
   whereClausePODetailTax:string,
   whereClausePOMisc:string,
   whereClausePODetailMiscTax:string,
   whereClausePOHeadMisc:string,
   whereClausePOHeaderMiscTax:string,
   whereClausePOHeaderTax:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_POTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetShipToAddressForCompany_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface GetShipToAddressForCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param custNum
      @param shipToNum
      @param ds
   */  
export interface GetShipToAddressForCustomer_input{
   custNum:number,
   shipToNum:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface GetShipToAddressForCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param plant
      @param ds
   */  
export interface GetShipToAddressForSite_input{
   plant:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface GetShipToAddressForSite_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param vendorNum
      @param purPoint
      @param ds
   */  
export interface GetShipToAddressForSupplier_input{
   vendorNum:number,
   purPoint:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface GetShipToAddressForSupplier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param partNum
   */  
export interface GetValidManufacturers_input{
   partNum:string,
}

export interface GetValidManufacturers_output{
parameters : {
      /**  output parameters  */  
   whereClause:string,
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
      @param valpartnum
   */  
export interface PartStatusValidationMessages_input{
      /**  The new PartNum if a substitute part is found, partNum will be the substitute part  */  
   valpartnum:string,
}

export interface PartStatusValidationMessages_output{
parameters : {
      /**  output parameters  */  
   valpartnum:string,
   QuestionString:string,
   SubstitutePartAvail:boolean,
   MsgType:string,
}
}

   /** Required : 
      @param ipoNum
   */  
export interface PreDuplicatePO_input{
   ipoNum:number,
}

export interface PreDuplicatePO_output{
parameters : {
      /**  output parameters  */  
   cMessage:string,
}
}

   /** Required : 
      @param PoNum
      @param PoLine
      @param PoRelease
   */  
export interface ReOpenRelease_input{
      /**  The Purchase ordre number  */  
   PoNum:number,
      /**  The Purchase order line  */  
   PoLine:number,
      /**  The Purchase ordre release  */  
   PoRelease:number,
}

export interface ReOpenRelease_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param PoNum
      @param PoLine
   */  
export interface ReopenOrderLine_input{
      /**  The Purchase ordre number  */  
   PoNum:number,
      /**  The Purchase ordre line  */  
   PoLine:number,
}

export interface ReopenOrderLine_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param PoNum
   */  
export interface ReopenOrder_input{
      /**  The Purchase ordre number  */  
   PoNum:number,
}

export interface ReopenOrder_output{
   returnObj:Erp_Tablesets_POTableset[],
}

   /** Required : 
      @param poNum
      @param calledFromUI
      @param ds
   */  
export interface SetReadyToCalc_input{
   poNum:number,
   calledFromUI:boolean,
   ds:Erp_Tablesets_POTableset[],
}

export interface SetReadyToCalc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPOTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPOTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_POTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param bLinkToContract
      @param partNum
      @param tableName
   */  
export interface ValidataPartToLinkToContract_input{
   bLinkToContract:boolean,
   partNum:string,
   tableName:string,
}

export interface ValidataPartToLinkToContract_output{
}

   /** Required : 
      @param ipPONum
   */  
export interface ValidateAcctForGLControl_input{
      /**  PONum  */  
   ipPONum:number,
}

export interface ValidateAcctForGLControl_output{
parameters : {
      /**  output parameters  */  
   outMessage:string,
}
}

   /** Required : 
      @param ipProposedInspPlan
      @param ipProposedSpecId
      @param ds
   */  
export interface ValidateInspection_input{
      /**  The new proposed InspPlanPartNum value  */  
   ipProposedInspPlan:string,
      /**  The new proposed SpecID value  */  
   ipProposedSpecId:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface ValidateInspection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
}
}

   /** Required : 
      @param PONum
   */  
export interface ValidatePOLinesTaxCategoryTypes_input{
      /**  The order number to validate  */  
   PONum:number,
}

export interface ValidatePOLinesTaxCategoryTypes_output{
}

   /** Required : 
      @param ds
      @param iPoNum
      @param iPoLine
      @param iPoRelease
      @param cPartNum
   */  
export interface VerifyReopenRelease_input{
   ds:Erp_Tablesets_POTableset[],
      /**  The Order Number of the Order Release to reopen  */  
   iPoNum:number,
      /**  The Order Line Number of the Release to close  */  
   iPoLine:number,
      /**  The Release Number of the Release to close  */  
   iPoRelease:number,
      /**  PartNum associated with this release  */  
   cPartNum:string,
}

export interface VerifyReopenRelease_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_POTableset[],
   cPromptMessage:string,
}
}

   /** Required : 
      @param viewName
      @param ds
   */  
export interface chkPODatesChanges_input{
      /**  Name of the view that is being modified.  */  
   viewName:string,
   ds:Erp_Tablesets_POTableset[],
}

export interface chkPODatesChanges_output{
parameters : {
      /**  output parameters  */  
   cOrderChangedMsgText:string,
}
}

