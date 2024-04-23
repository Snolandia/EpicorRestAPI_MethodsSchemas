import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxValidationSvc
# Description: Tax Id Validation Status Header
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxValidations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxValidations
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations",headers=creds) as resp:
           return await resp.json()

async def post_TaxValidations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations_Company_LocalName_Key1_Key2(Company, LocalName, Key1, Key2, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxValidation item
   Description: Calls GetByID to retrieve the TaxValidation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxValidation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxValidations_Company_LocalName_Key1_Key2(Company, LocalName, Key1, Key2, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxValidation for the service
   Description: Calls UpdateExt to update TaxValidation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxValidation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxValidations_Company_LocalName_Key1_Key2(Company, LocalName, Key1, Key2, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxValidation item
   Description: Call UpdateExt to delete TaxValidation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxValidation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations_Company_LocalName_Key1_Key2_TaxValidationCustomers(Company, LocalName, Key1, Key2, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxValidationCustomers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxValidationCustomers1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")/TaxValidationCustomers",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations_Company_LocalName_Key1_Key2_TaxValidationCustomers_Company_TaxValidationID_CustNum(Company, LocalName, Key1, Key2, TaxValidationID, CustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxValidationCustomer item
   Description: Calls GetByID to retrieve the TaxValidationCustomer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxValidationCustomer1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxValidationCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")/TaxValidationCustomers(" + Company + "," + TaxValidationID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations_Company_LocalName_Key1_Key2_TaxValidationVendors(Company, LocalName, Key1, Key2, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxValidationVendors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxValidationVendors1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")/TaxValidationVendors",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations_Company_LocalName_Key1_Key2_TaxValidationVendors_Company_TaxValidationID_VendorNum(Company, LocalName, Key1, Key2, TaxValidationID, VendorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxValidationVendor item
   Description: Calls GetByID to retrieve the TaxValidationVendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxValidationVendor1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")/TaxValidationVendors(" + Company + "," + TaxValidationID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations_Company_LocalName_Key1_Key2_TaxValidationHeadAttches(Company, LocalName, Key1, Key2, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxValidationHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxValidationHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")/TaxValidationHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidations_Company_LocalName_Key1_Key2_TaxValidationHeadAttches_Company_LocalName_Key1_Key2_DrawingSeq(Company, LocalName, Key1, Key2, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxValidationHeadAttch item
   Description: Calls GetByID to retrieve the TaxValidationHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxValidationHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidations(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + ")/TaxValidationHeadAttches(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidationCustomers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxValidationCustomers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxValidationCustomers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationCustomers",headers=creds) as resp:
           return await resp.json()

async def post_TaxValidationCustomers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxValidationCustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxValidationCustomerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxValidationCustomerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationCustomers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxValidationCustomers_Company_TaxValidationID_CustNum(Company, TaxValidationID, CustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxValidationCustomer item
   Description: Calls GetByID to retrieve the TaxValidationCustomer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxValidationCustomer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxValidationCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationCustomers(" + Company + "," + TaxValidationID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxValidationCustomers_Company_TaxValidationID_CustNum(Company, TaxValidationID, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxValidationCustomer for the service
   Description: Calls UpdateExt to update TaxValidationCustomer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxValidationCustomer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxValidationCustomerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationCustomers(" + Company + "," + TaxValidationID + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxValidationCustomers_Company_TaxValidationID_CustNum(Company, TaxValidationID, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxValidationCustomer item
   Description: Call UpdateExt to delete TaxValidationCustomer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxValidationCustomer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationCustomers(" + Company + "," + TaxValidationID + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidationVendors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxValidationVendors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxValidationVendors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationVendors",headers=creds) as resp:
           return await resp.json()

async def post_TaxValidationVendors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxValidationVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxValidationVendorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxValidationVendorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationVendors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxValidationVendors_Company_TaxValidationID_VendorNum(Company, TaxValidationID, VendorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxValidationVendor item
   Description: Calls GetByID to retrieve the TaxValidationVendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxValidationVendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationVendors(" + Company + "," + TaxValidationID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxValidationVendors_Company_TaxValidationID_VendorNum(Company, TaxValidationID, VendorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxValidationVendor for the service
   Description: Calls UpdateExt to update TaxValidationVendor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxValidationVendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxValidationVendorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationVendors(" + Company + "," + TaxValidationID + "," + VendorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxValidationVendors_Company_TaxValidationID_VendorNum(Company, TaxValidationID, VendorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxValidationVendor item
   Description: Call UpdateExt to delete TaxValidationVendor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxValidationVendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxValidationID: Desc: TaxValidationID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationVendors(" + Company + "," + TaxValidationID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxValidationHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxValidationHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxValidationHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_TaxValidationHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxValidationHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxValidationHeadAttches_Company_LocalName_Key1_Key2_DrawingSeq(Company, LocalName, Key1, Key2, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxValidationHeadAttch item
   Description: Calls GetByID to retrieve the TaxValidationHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxValidationHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationHeadAttches(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxValidationHeadAttches_Company_LocalName_Key1_Key2_DrawingSeq(Company, LocalName, Key1, Key2, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxValidationHeadAttch for the service
   Description: Calls UpdateExt to update TaxValidationHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxValidationHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxValidationHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationHeadAttches(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxValidationHeadAttches_Company_LocalName_Key1_Key2_DrawingSeq(Company, LocalName, Key1, Key2, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxValidationHeadAttch item
   Description: Call UpdateExt to delete TaxValidationHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxValidationHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/TaxValidationHeadAttches(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxValidationHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxValidationHead, whereClauseTaxValidationHeadAttch, whereClauseTaxValidationCustomer, whereClauseTaxValidationVendor, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxValidationHead=" + whereClauseTaxValidationHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxValidationHeadAttch=" + whereClauseTaxValidationHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxValidationCustomer=" + whereClauseTaxValidationCustomer
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxValidationVendor=" + whereClauseTaxValidationVendor
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(localName, key1, key2, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "localName=" + localName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_LookupVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LookupVendor
   Description: Lookup Vendor
   OperationID: LookupVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookupVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookupVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LookupCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LookupCustomer
   Description: Lookup Customer
   OperationID: LookupCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookupCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookupCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LookupVendors(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LookupVendors
   Description: Lookup Vendors
   OperationID: LookupVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookupVendors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookupVendors_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LookupCustomers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LookupCustomers
   Description: Lookup Customers
   OperationID: LookupCustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LookupCustomers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LookupCustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartValidate
   Description: Start Tax ID Validation
   OperationID: StartValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartValidateWithFilters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartValidateWithFilters
   Description: Start Tax ID Validation
   OperationID: StartValidateWithFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartValidateWithFilters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartValidateWithFilters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxValidationHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxValidationHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxValidationHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxValidationHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxValidationHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxValidationHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxValidationHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxValidationHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxValidationHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxValidationHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxValidationCustomerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxValidationCustomerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxValidationHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxValidationHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxValidationHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxValidationHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxValidationHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxValidationHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxValidationVendorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxValidationVendorRow] = obj["value"]
      pass

class Erp_Tablesets_TaxValidationCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Country:str = obj["Country"]
      self.Name:str = obj["Name"]
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ResaleID:str = obj["ResaleID"]
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      self.TaxValidationID:str = obj["TaxValidationID"]
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      self.TaxValidationStatusDisplay:str = obj["TaxValidationStatusDisplay"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.TaxValidationID:str = obj["TaxValidationID"]
      """  Tax Id validation Code.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.TaxValidationID:str = obj["TaxValidationID"]
      """  Tax Id validation Code.  """  
      self.DisplayCustomers:bool = obj["DisplayCustomers"]
      """  Include Customers  """  
      self.DisplayVendors:bool = obj["DisplayVendors"]
      """  Include Suppliers  """  
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.StatusNotValidated:bool = obj["StatusNotValidated"]
      """  Not Validated Status selection  """  
      self.StatusValid:bool = obj["StatusValid"]
      """  Valid Status selection  """  
      self.StatusInvalid:bool = obj["StatusInvalid"]
      """  Invalid Status selection  """  
      self.ValidatedBy:str = obj["ValidatedBy"]
      """  User Id run the validation.  """  
      self.ValidatedOn:str = obj["ValidatedOn"]
      """  The date when the user run the validation  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface of type Tax Id Validation  """  
      self.CompletionStatus:int = obj["CompletionStatus"]
      """  Not started/ Completed (0/1)  """  
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ValidationMethod:str = obj["ValidationMethod"]
      self.HMRCFraudPrevHeader:str = obj["HMRCFraudPrevHeader"]
      self.VendorNumList:str = obj["VendorNumList"]
      self.CustomerNumList:str = obj["CustomerNumList"]
      self.VendorIDList:str = obj["VendorIDList"]
      self.CustomerIDList:str = obj["CustomerIDList"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationVendorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Country:str = obj["Country"]
      self.Name:str = obj["Name"]
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      self.VendorID:str = obj["VendorID"]
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.TaxValidationID:str = obj["TaxValidationID"]
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      self.TaxValidationStatusDisplay:str = obj["TaxValidationStatusDisplay"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   localName
   key1
   key2
   """  
   def __init__(self, obj):
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxValidationCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Country:str = obj["Country"]
      self.Name:str = obj["Name"]
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ResaleID:str = obj["ResaleID"]
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      self.TaxValidationID:str = obj["TaxValidationID"]
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      self.TaxValidationStatusDisplay:str = obj["TaxValidationStatusDisplay"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.TaxValidationID:str = obj["TaxValidationID"]
      """  Tax Id validation Code.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationHeadListTableset:
   def __init__(self, obj):
      self.TaxValidationHeadList:list[Erp_Tablesets_TaxValidationHeadListRow] = obj["TaxValidationHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxValidationHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.TaxValidationID:str = obj["TaxValidationID"]
      """  Tax Id validation Code.  """  
      self.DisplayCustomers:bool = obj["DisplayCustomers"]
      """  Include Customers  """  
      self.DisplayVendors:bool = obj["DisplayVendors"]
      """  Include Suppliers  """  
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.StatusNotValidated:bool = obj["StatusNotValidated"]
      """  Not Validated Status selection  """  
      self.StatusValid:bool = obj["StatusValid"]
      """  Valid Status selection  """  
      self.StatusInvalid:bool = obj["StatusInvalid"]
      """  Invalid Status selection  """  
      self.ValidatedBy:str = obj["ValidatedBy"]
      """  User Id run the validation.  """  
      self.ValidatedOn:str = obj["ValidatedOn"]
      """  The date when the user run the validation  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface of type Tax Id Validation  """  
      self.CompletionStatus:int = obj["CompletionStatus"]
      """  Not started/ Completed (0/1)  """  
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ValidationMethod:str = obj["ValidationMethod"]
      self.HMRCFraudPrevHeader:str = obj["HMRCFraudPrevHeader"]
      self.VendorNumList:str = obj["VendorNumList"]
      self.CustomerNumList:str = obj["CustomerNumList"]
      self.VendorIDList:str = obj["VendorIDList"]
      self.CustomerIDList:str = obj["CustomerIDList"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxValidationTableset:
   def __init__(self, obj):
      self.TaxValidationHead:list[Erp_Tablesets_TaxValidationHeadRow] = obj["TaxValidationHead"]
      self.TaxValidationHeadAttch:list[Erp_Tablesets_TaxValidationHeadAttchRow] = obj["TaxValidationHeadAttch"]
      self.TaxValidationCustomer:list[Erp_Tablesets_TaxValidationCustomerRow] = obj["TaxValidationCustomer"]
      self.TaxValidationVendor:list[Erp_Tablesets_TaxValidationVendorRow] = obj["TaxValidationVendor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxValidationVendorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Country:str = obj["Country"]
      self.Name:str = obj["Name"]
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      self.VendorID:str = obj["VendorID"]
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.TaxValidationID:str = obj["TaxValidationID"]
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      self.TaxValidationStatusDisplay:str = obj["TaxValidationStatusDisplay"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtTaxValidationTableset:
   def __init__(self, obj):
      self.TaxValidationHead:list[Erp_Tablesets_TaxValidationHeadRow] = obj["TaxValidationHead"]
      self.TaxValidationHeadAttch:list[Erp_Tablesets_TaxValidationHeadAttchRow] = obj["TaxValidationHeadAttch"]
      self.TaxValidationCustomer:list[Erp_Tablesets_TaxValidationCustomerRow] = obj["TaxValidationCustomer"]
      self.TaxValidationVendor:list[Erp_Tablesets_TaxValidationVendorRow] = obj["TaxValidationVendor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   localName
   key1
   key2
   """  
   def __init__(self, obj):
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxValidationTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxValidationTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxValidationTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxValidationHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxValidationHeadAttch_input:
   """ Required : 
   ds
   localName
   key1
   key2
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      pass

class GetNewTaxValidationHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxValidationHead_input:
   """ Required : 
   ds
   localName
   key1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      pass

class GetNewTaxValidationHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxValidationHead
   whereClauseTaxValidationHeadAttch
   whereClauseTaxValidationCustomer
   whereClauseTaxValidationVendor
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxValidationHead:str = obj["whereClauseTaxValidationHead"]
      self.whereClauseTaxValidationHeadAttch:str = obj["whereClauseTaxValidationHeadAttch"]
      self.whereClauseTaxValidationCustomer:str = obj["whereClauseTaxValidationCustomer"]
      self.whereClauseTaxValidationVendor:str = obj["whereClauseTaxValidationVendor"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxValidationTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class LookupCustomer_input:
   """ Required : 
   CustID
   ds
   """  
   def __init__(self, obj):
      self.CustID:str = obj["CustID"]
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

class LookupCustomer_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LookupCustomers_input:
   """ Required : 
   taxValidationID
   custNumList
   ds
   """  
   def __init__(self, obj):
      self.taxValidationID:str = obj["taxValidationID"]
      self.custNumList:str = obj["custNumList"]
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

class LookupCustomers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LookupVendor_input:
   """ Required : 
   vendorID
   ds
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

class LookupVendor_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LookupVendors_input:
   """ Required : 
   taxValidationID
   vendorNumList
   ds
   """  
   def __init__(self, obj):
      self.taxValidationID:str = obj["taxValidationID"]
      self.vendorNumList:str = obj["vendorNumList"]
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

class LookupVendors_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartValidateWithFilters_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

class StartValidateWithFilters_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartValidate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

class StartValidate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxValidationTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxValidationTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

