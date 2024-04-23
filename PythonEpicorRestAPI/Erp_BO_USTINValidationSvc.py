import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.USTINValidationSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get USTINValidations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations",headers=creds) as resp:
           return await resp.json()

async def post_USTINValidations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_USTINValidations_Company_TINValidationID(Company, TINValidationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidation item
   Description: Calls GetByID to retrieve the USTINValidation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_USTINValidations_Company_TINValidationID(Company, TINValidationID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update USTINValidation for the service
   Description: Calls UpdateExt to update USTINValidation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_USTINValidations_Company_TINValidationID(Company, TINValidationID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete USTINValidation item
   Description: Call UpdateExt to delete USTINValidation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidations_Company_TINValidationID_USTINValidationVendors(Company, TINValidationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get USTINValidationVendors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_USTINValidationVendors1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationVendors",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidations_Company_TINValidationID_USTINValidationVendors_Company_TINValidationID_VendorNum(Company, TINValidationID, VendorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidationVendor item
   Description: Calls GetByID to retrieve the USTINValidationVendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationVendor1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidations_Company_TINValidationID_USTINValidationAttches(Company, TINValidationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get USTINValidationAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_USTINValidationAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationAttches",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidations_Company_TINValidationID_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company, TINValidationID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidationAttch item
   Description: Calls GetByID to retrieve the USTINValidationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidations(" + Company + "," + TINValidationID + ")/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationVendors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get USTINValidationVendors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidationVendors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors",headers=creds) as resp:
           return await resp.json()

async def post_USTINValidationVendors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidationVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationVendors_Company_TINValidationID_VendorNum(Company, TINValidationID, VendorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidationVendor item
   Description: Calls GetByID to retrieve the USTINValidationVendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationVendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_USTINValidationVendors_Company_TINValidationID_VendorNum(Company, TINValidationID, VendorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update USTINValidationVendor for the service
   Description: Calls UpdateExt to update USTINValidationVendor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidationVendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationVendorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_USTINValidationVendors_Company_TINValidationID_VendorNum(Company, TINValidationID, VendorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete USTINValidationVendor item
   Description: Call UpdateExt to delete USTINValidationVendor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidationVendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationVendors(" + Company + "," + TINValidationID + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get USTINValidationAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidationAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches",headers=creds) as resp:
           return await resp.json()

async def post_USTINValidationAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidationAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company, TINValidationID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidationAttch item
   Description: Calls GetByID to retrieve the USTINValidationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company, TINValidationID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update USTINValidationAttch for the service
   Description: Calls UpdateExt to update USTINValidationAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidationAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_USTINValidationAttches_Company_TINValidationID_DrawingSeq(Company, TINValidationID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete USTINValidationAttch item
   Description: Call UpdateExt to delete USTINValidationAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidationAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationID: Desc: TINValidationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/USTINValidationAttches(" + Company + "," + TINValidationID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseUSTINValidation, whereClauseUSTINValidationAttch, whereClauseUSTINValidationVendor, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUSTINValidation=" + whereClauseUSTINValidation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUSTINValidationAttch=" + whereClauseUSTINValidationAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUSTINValidationVendor=" + whereClauseUSTINValidationVendor
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tiNValidationID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "tiNValidationID=" + tiNValidationID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_RemoveUSTINValidationVendors(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveUSTINValidationVendors
   OperationID: RemoveUSTINValidationVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveUSTINValidationVendors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveUSTINValidationVendors_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDescriptionList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDescriptionList
   Description: Get Description list for field
   OperationID: GetDescriptionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDescriptionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDescriptionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenExportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenExportFile
   Description: Generate Export File for TIN Validation
   OperationID: GenExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelExport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelExport
   Description: Cancel Export
   OperationID: CancelExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateUSTINValidationVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateUSTINValidationVendor
   Description: Update USTINValidationVendor table. Standard update not worked for keyed field
   OperationID: UpdateUSTINValidationVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateUSTINValidationVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateUSTINValidationVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckVendor
   Description: CheckVendor
   OperationID: CheckVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MarkAsSubmitted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MarkAsSubmitted
   Description: Mark valiation as submitted
   OperationID: MarkAsSubmitted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MarkAsSubmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MarkAsSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUSTINValidationVendors(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddUSTINValidationVendors
   OperationID: AddUSTINValidationVendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUSTINValidationVendors_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUSTINValidationVendors_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUSTINValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUSTINValidation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUSTINValidationAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUSTINValidationAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidationAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidationAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidationAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUSTINValidationVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUSTINValidationVendor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidationVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidationVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidationVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_USTINValidationAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_USTINValidationListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_USTINValidationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationVendorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_USTINValidationVendorRow] = obj["value"]
      pass

class Erp_Tablesets_USTINValidationAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TINValidationID:str = obj["TINValidationID"]
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

class Erp_Tablesets_USTINValidationListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ExportFile:str = obj["ExportFile"]
      """  Export File  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.Exported:bool = obj["Exported"]
      """  Exported  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  Tracking Number  """  
      self.ResultReceived:bool = obj["ResultReceived"]
      """  Result Received  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_USTINValidationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.ExportFile:str = obj["ExportFile"]
      """  Export File  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.Exported:bool = obj["Exported"]
      """  Exported  """  
      self.IncludeValidStatusNew:bool = obj["IncludeValidStatusNew"]
      """  Include Valid Status New  """  
      self.IncludeValidStatusInvalid:bool = obj["IncludeValidStatusInvalid"]
      """  Include Valid Status Invalid  """  
      self.IncludeValidStatusPending:bool = obj["IncludeValidStatusPending"]
      """  Include Valid Status Pending  """  
      self.IncludeValidStatusMatched:bool = obj["IncludeValidStatusMatched"]
      """  Include Valid Status Matched  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  Tracking Number  """  
      self.ResultReceived:bool = obj["ResultReceived"]
      """  Result Received  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ValidationResultsDescription:str = obj["ValidationResultsDescription"]
      self.ValidationResultsID:str = obj["ValidationResultsID"]
      self.ExportFileNameDisplay:str = obj["ExportFileNameDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_USTINValidationVendorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TINValidationID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.Country:str = obj["Country"]
      self.Inactive:bool = obj["Inactive"]
      self.Name:str = obj["Name"]
      self.PayHold:bool = obj["PayHold"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.State:str = obj["State"]
      self.TaxPayerID:str = obj["TaxPayerID"]
      self.TIN:str = obj["TIN"]
      self.TINType:str = obj["TINType"]
      self.VendorID:str = obj["VendorID"]
      self.ZIP:str = obj["ZIP"]
      self.TINValidationStatus:int = obj["TINValidationStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddUSTINValidationVendors_input:
   """ Required : 
   tinValidationID
   vendorNumList
   vendorIDList
   """  
   def __init__(self, obj):
      self.tinValidationID:str = obj["tinValidationID"]
      self.vendorNumList:str = obj["vendorNumList"]
      self.vendorIDList:str = obj["vendorIDList"]
      pass

class AddUSTINValidationVendors_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_USTINValidationTableset] = obj["returnObj"]
      pass

class CancelExport_input:
   """ Required : 
   tinValidationID
   """  
   def __init__(self, obj):
      self.tinValidationID:str = obj["tinValidationID"]
      pass

class CancelExport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckVendor_input:
   """ Required : 
   tinValidationID
   vendorID
   """  
   def __init__(self, obj):
      self.tinValidationID:str = obj["tinValidationID"]
      self.vendorID:str = obj["vendorID"]
      pass

class CheckVendor_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   tiNValidationID
   """  
   def __init__(self, obj):
      self.tiNValidationID:str = obj["tiNValidationID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_USTINValidationAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TINValidationID:str = obj["TINValidationID"]
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

class Erp_Tablesets_USTINValidationListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ExportFile:str = obj["ExportFile"]
      """  Export File  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.Exported:bool = obj["Exported"]
      """  Exported  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  Tracking Number  """  
      self.ResultReceived:bool = obj["ResultReceived"]
      """  Result Received  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_USTINValidationListTableset:
   def __init__(self, obj):
      self.USTINValidationList:list[Erp_Tablesets_USTINValidationListRow] = obj["USTINValidationList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_USTINValidationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.ExportFile:str = obj["ExportFile"]
      """  Export File  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.Exported:bool = obj["Exported"]
      """  Exported  """  
      self.IncludeValidStatusNew:bool = obj["IncludeValidStatusNew"]
      """  Include Valid Status New  """  
      self.IncludeValidStatusInvalid:bool = obj["IncludeValidStatusInvalid"]
      """  Include Valid Status Invalid  """  
      self.IncludeValidStatusPending:bool = obj["IncludeValidStatusPending"]
      """  Include Valid Status Pending  """  
      self.IncludeValidStatusMatched:bool = obj["IncludeValidStatusMatched"]
      """  Include Valid Status Matched  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  Tracking Number  """  
      self.ResultReceived:bool = obj["ResultReceived"]
      """  Result Received  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ValidationResultsDescription:str = obj["ValidationResultsDescription"]
      self.ValidationResultsID:str = obj["ValidationResultsID"]
      self.ExportFileNameDisplay:str = obj["ExportFileNameDisplay"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_USTINValidationTableset:
   def __init__(self, obj):
      self.USTINValidation:list[Erp_Tablesets_USTINValidationRow] = obj["USTINValidation"]
      self.USTINValidationAttch:list[Erp_Tablesets_USTINValidationAttchRow] = obj["USTINValidationAttch"]
      self.USTINValidationVendor:list[Erp_Tablesets_USTINValidationVendorRow] = obj["USTINValidationVendor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_USTINValidationVendorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TINValidationID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.Country:str = obj["Country"]
      self.Inactive:bool = obj["Inactive"]
      self.Name:str = obj["Name"]
      self.PayHold:bool = obj["PayHold"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.State:str = obj["State"]
      self.TaxPayerID:str = obj["TaxPayerID"]
      self.TIN:str = obj["TIN"]
      self.TINType:str = obj["TINType"]
      self.VendorID:str = obj["VendorID"]
      self.ZIP:str = obj["ZIP"]
      self.TINValidationStatus:int = obj["TINValidationStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtUSTINValidationTableset:
   def __init__(self, obj):
      self.USTINValidation:list[Erp_Tablesets_USTINValidationRow] = obj["USTINValidation"]
      self.USTINValidationAttch:list[Erp_Tablesets_USTINValidationAttchRow] = obj["USTINValidationAttch"]
      self.USTINValidationVendor:list[Erp_Tablesets_USTINValidationVendorRow] = obj["USTINValidationVendor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenExportFile_input:
   """ Required : 
   tinValidationID
   eftHeadUID
   exportFileName
   """  
   def __init__(self, obj):
      self.tinValidationID:str = obj["tinValidationID"]
      """  Report ID  """  
      self.eftHeadUID:int = obj["eftHeadUID"]
      """  Electronic Interface ID  """  
      self.exportFileName:str = obj["exportFileName"]
      """  Export File Name  """  
      pass

class GenExportFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Generated File Name  """  
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.CountRecordsExported:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   tiNValidationID
   """  
   def __init__(self, obj):
      self.tiNValidationID:str = obj["tiNValidationID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_USTINValidationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_USTINValidationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_USTINValidationTableset] = obj["returnObj"]
      pass

class GetDescriptionList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetDescriptionList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_USTINValidationListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUSTINValidationAttch_input:
   """ Required : 
   ds
   tiNValidationID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      self.tiNValidationID:str = obj["tiNValidationID"]
      pass

class GetNewUSTINValidationAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUSTINValidationVendor_input:
   """ Required : 
   ds
   tiNValidationID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      self.tiNValidationID:str = obj["tiNValidationID"]
      pass

class GetNewUSTINValidationVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUSTINValidation_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

class GetNewUSTINValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseUSTINValidation
   whereClauseUSTINValidationAttch
   whereClauseUSTINValidationVendor
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseUSTINValidation:str = obj["whereClauseUSTINValidation"]
      self.whereClauseUSTINValidationAttch:str = obj["whereClauseUSTINValidationAttch"]
      self.whereClauseUSTINValidationVendor:str = obj["whereClauseUSTINValidationVendor"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_USTINValidationTableset] = obj["returnObj"]
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

class LookupVendor_input:
   """ Required : 
   tinValidationID
   vendorID
   ds
   """  
   def __init__(self, obj):
      self.tinValidationID:str = obj["tinValidationID"]
      self.vendorID:str = obj["vendorID"]
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

class LookupVendor_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MarkAsSubmitted_input:
   """ Required : 
   tinValidationID
   """  
   def __init__(self, obj):
      self.tinValidationID:str = obj["tinValidationID"]
      pass

class MarkAsSubmitted_output:
   def __init__(self, obj):
      pass

class RemoveUSTINValidationVendors_input:
   """ Required : 
   tinValidationID
   """  
   def __init__(self, obj):
      self.tinValidationID:str = obj["tinValidationID"]
      pass

class RemoveUSTINValidationVendors_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUSTINValidationTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUSTINValidationTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateUSTINValidationVendor_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

class UpdateUSTINValidationVendor_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationTableset] = obj["ds"]
      pass

      """  output parameters  """  

