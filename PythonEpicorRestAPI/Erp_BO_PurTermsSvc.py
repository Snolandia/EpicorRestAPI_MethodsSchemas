import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PurTermsSvc
# Description: Purchasing PurTerms master. Used by Purchase Order management and Accounts Payable modules.
DELETE: Not allowed if referenced in the Vendor, POHeader or APInvHed file.
Since the delete of a PurTerms code should be a very rare occurence, these files will not
be indexed by the code. This is done so not to put undue overhead on the system for
maintaining indexes. A Message will be displayed "Please Wait...Validating delete Request".
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PurTerms(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurTerms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTerms
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms",headers=creds) as resp:
           return await resp.json()

async def post_PurTerms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTerms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurTermsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurTerms_Company_TermsCode(Company, TermsCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurTerm item
   Description: Calls GetByID to retrieve the PurTerm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTerm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurTermsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurTerms_Company_TermsCode(Company, TermsCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurTerm for the service
   Description: Calls UpdateExt to update PurTerm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTerm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurTerms_Company_TermsCode(Company, TermsCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurTerm item
   Description: Call UpdateExt to delete PurTerm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTerm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurTerms_Company_TermsCode_PurTermsDtls(Company, TermsCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PurTermsDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurTermsDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsDtls",headers=creds) as resp:
           return await resp.json()

async def get_PurTerms_Company_TermsCode_PurTermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurTermsDtl item
   Description: Calls GetByID to retrieve the PurTermsDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurTermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurTerms_Company_TermsCode_PurTermsScheds(Company, TermsCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PurTermsScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurTermsScheds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsScheds",headers=creds) as resp:
           return await resp.json()

async def get_PurTerms_Company_TermsCode_PurTermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurTermsSched item
   Description: Calls GetByID to retrieve the PurTermsSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsSched1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurTermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurTerms_Company_TermsCode_PurTermsAttches(Company, TermsCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PurTermsAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurTermsAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsAttches",headers=creds) as resp:
           return await resp.json()

async def get_PurTerms_Company_TermsCode_PurTermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurTermsAttch item
   Description: Calls GetByID to retrieve the PurTermsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurTermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTerms(" + Company + "," + TermsCode + ")/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurTermsDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurTermsDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTermsDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls",headers=creds) as resp:
           return await resp.json()

async def post_PurTermsDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTermsDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurTermsDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurTermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurTermsDtl item
   Description: Calls GetByID to retrieve the PurTermsDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurTermsDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurTermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurTermsDtl for the service
   Description: Calls UpdateExt to update PurTermsDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTermsDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurTermsDtls_Company_TermsCode_TermsSeq(Company, TermsCode, TermsSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurTermsDtl item
   Description: Call UpdateExt to delete PurTermsDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTermsDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param TermsSeq: Desc: TermsSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsDtls(" + Company + "," + TermsCode + "," + TermsSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurTermsScheds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurTermsScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTermsScheds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds",headers=creds) as resp:
           return await resp.json()

async def post_PurTermsScheds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTermsScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurTermsSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurTermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurTermsSched item
   Description: Calls GetByID to retrieve the PurTermsSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurTermsSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurTermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurTermsSched for the service
   Description: Calls UpdateExt to update PurTermsSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTermsSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurTermsScheds_Company_TermsCode_PaySeq(Company, TermsCode, PaySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurTermsSched item
   Description: Call UpdateExt to delete PurTermsSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTermsSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param PaySeq: Desc: PaySeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsScheds(" + Company + "," + TermsCode + "," + PaySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurTermsAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurTermsAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurTermsAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches",headers=creds) as resp:
           return await resp.json()

async def post_PurTermsAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurTermsAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurTermsAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurTermsAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurTermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurTermsAttch item
   Description: Calls GetByID to retrieve the PurTermsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurTermsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurTermsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurTermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurTermsAttch for the service
   Description: Calls UpdateExt to update PurTermsAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurTermsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurTermsAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurTermsAttches_Company_TermsCode_DrawingSeq(Company, TermsCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurTermsAttch item
   Description: Call UpdateExt to delete PurTermsAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurTermsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TermsCode: Desc: TermsCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/PurTermsAttches(" + Company + "," + TermsCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurTermsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePurTerms, whereClausePurTermsAttch, whereClausePurTermsDtl, whereClausePurTermsSched, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePurTerms=" + whereClausePurTerms
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePurTermsAttch=" + whereClausePurTermsAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePurTermsDtl=" + whereClausePurTermsDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePurTermsSched=" + whereClausePurTermsSched
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(termsCode, epicorHeaders = None):
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
   params += "termsCode=" + termsCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDisDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDisDays
   Description: Purpose:
Parameters:  none
Notes:
<param name="vDueOnDay">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingDisDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDisDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDisDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDisPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDisPercent
   Description: Purpose:
Parameters:  none
Notes:
<param name="vDiscountPercent">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingDisPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDisPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDisPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumOfDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumOfDays
   Description: Purpose:
Parameters:  none
Notes:
<param name="vNumOfDay">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingNumOfDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumOfDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumOfDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumOfMonths(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumOfMonths
   Description: Purpose:
Parameters:  none
Notes:
<param name="vNumOfMonths">Propose Discount Days</param><param name="ds">Temporary tables for PurTerms details</param>
   OperationID: OnChangingNumOfMonths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumOfMonths_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumOfMonths_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTermDueOnDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTermDueOnDay
   Description: Purpose:
Parameters:  none
Notes:
<param name="pDueOnDay">Propose Discount Days</param>
   OperationID: OnChangingTermDueOnDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTermDueOnDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTermDueOnDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPurTermsSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPurTermsSched
   OperationID: GetPurTermsSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPurTermsSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurTermsSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTermsTypeCodeDescList(epicorHeaders = None):
   """  
   Summary: Invoke method GetTermsTypeCodeDescList
   Description: Purpose: Gets list of codes/descriptions for TermsType combo-box
Parameters: none
   OperationID: GetTermsTypeCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTermsTypeCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnPurTermsSchedPercentageUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPurTermsSchedPercentageUpdate
   Description: Called on PurTermsSched.PayPercentage update
   OperationID: OnPurTermsSchedPercentageUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPurTermsSchedPercentageUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPurTermsSchedPercentageUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDiscountPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDiscountPercent
   Description: This method will check if current discount percent is less or greater than previous or next discounts and send a warning message.
   OperationID: ValidateDiscountPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDiscountPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDiscountPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnPurTermsSchedPercentageUpdate2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPurTermsSchedPercentageUpdate2
   OperationID: OnPurTermsSchedPercentageUpdate2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPurTermsSchedPercentageUpdate2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPurTermsSchedPercentageUpdate2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurTerms(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurTerms
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTerms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurTerms_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTerms_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurTermsAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurTermsAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTermsAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurTermsAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTermsAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurTermsDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurTermsDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTermsDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurTermsDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTermsDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurTermsSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurTermsSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurTermsSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurTermsSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurTermsSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurTermsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurTermsAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurTermsDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurTermsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurTermsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurTermsSchedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurTermsSchedRow] = obj["value"]
      pass

class Erp_Tablesets_PurTermsAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TermsCode:str = obj["TermsCode"]
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

class Erp_Tablesets_PurTermsDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.TermsSeq:int = obj["TermsSeq"]
      """  Sequence Counter to allow multiple Discounts  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Discount Type (Day of Months)  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   The discount percentage given for prompt payment of an invoice.
Invoice printing uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Month Y Days)  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Disc Type (Days of Month)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurTermsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field define the type of the term.  """  
      self.Description:str = obj["Description"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.DueDays:int = obj["DueDays"]
      """  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  """  
      self.DiscountDays:int = obj["DiscountDays"]
      """  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.Monthly:bool = obj["Monthly"]
      """  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Day of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Tems Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalPurTerms:bool = obj["GlobalPurTerms"]
      """  Marks this PurTerms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MonthsInFuture:int = obj["MonthsInFuture"]
      """  Months In Future  """  
      self.DueDayOfMonth:int = obj["DueDayOfMonth"]
      """  DueDayOfMonth  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the Purchase Term is default  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurTermsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field define the type of the term.  """  
      self.Description:str = obj["Description"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.DueDays:int = obj["DueDays"]
      """  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  """  
      self.DiscountDays:int = obj["DiscountDays"]
      """  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.Monthly:bool = obj["Monthly"]
      """  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Day of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Tems Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalPurTerms:bool = obj["GlobalPurTerms"]
      """  Marks this PurTerms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  COIFRSCalculation  """  
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  COIFRSNumberOfPeriods  """  
      self.MonthsInFuture:int = obj["MonthsInFuture"]
      """  Months In Future  """  
      self.DueDayOfMonth:int = obj["DueDayOfMonth"]
      """  DueDayOfMonth  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the Purchase Term is default  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurTermsSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.PaySeq:int = obj["PaySeq"]
      """  Specifies the number of payment of the Payment Schedule. This is an auto-generated sequence number.  """  
      self.Days:int = obj["Days"]
      """  Specifies the number of days for the payment to be paid. This is used to calculate Due Date in Invoice Payment Schedule.  """  
      self.PayPercent:int = obj["PayPercent"]
      """  Specifies the percent of the payment to be paid. This is used to calculate amount to be paid per payment in Purchase Order and Invoice Payment Sechedule.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of user who created this record.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date that the record was created.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   termsCode
   """  
   def __init__(self, obj):
      self.termsCode:str = obj["termsCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PurTermsAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TermsCode:str = obj["TermsCode"]
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

class Erp_Tablesets_PurTermsDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.TermsSeq:int = obj["TermsSeq"]
      """  Sequence Counter to allow multiple Discounts  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Discount Type (Day of Months)  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   The discount percentage given for prompt payment of an invoice.
Invoice printing uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Month Y Days)  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Disc Type (Days of Month)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurTermsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field define the type of the term.  """  
      self.Description:str = obj["Description"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.DueDays:int = obj["DueDays"]
      """  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  """  
      self.DiscountDays:int = obj["DiscountDays"]
      """  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.Monthly:bool = obj["Monthly"]
      """  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Day of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Tems Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalPurTerms:bool = obj["GlobalPurTerms"]
      """  Marks this PurTerms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MonthsInFuture:int = obj["MonthsInFuture"]
      """  Months In Future  """  
      self.DueDayOfMonth:int = obj["DueDayOfMonth"]
      """  DueDayOfMonth  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the Purchase Term is default  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurTermsListTableset:
   def __init__(self, obj):
      self.PurTermsList:list[Erp_Tablesets_PurTermsListRow] = obj["PurTermsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PurTermsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchase Terms code master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysDefault:bool = obj["SysDefault"]
      """  System Default Term  """  
      self.TermsType:str = obj["TermsType"]
      """  This field define the type of the term.  """  
      self.Description:str = obj["Description"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.DueDays:int = obj["DueDays"]
      """  This field is used in invoice entry to calculate the due date of the invoice.  For "Monthly" terms this is the number of days from the end of the invoice's month that the invoice is due.  """  
      self.DiscountDays:int = obj["DiscountDays"]
      """  Number of days in which payment discount can be earned.  Invoice entry uses this value to calculate a discount due date.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   OBSOLETE FIELD The discount percentage given for prompt payment of invoice.
Invoice entry uses this value to calculate a prompt payment discount amount.  """  
      self.NumberOfPayments:int = obj["NumberOfPayments"]
      """  An optional entry which if used defines the # of installment payments that will be made for invoices using the specific terms. Invoicing will generate due dates and disburse the invoice total into equal corresponding amounts based on this value.  """  
      self.Monthly:bool = obj["Monthly"]
      """  Indicates that the due date is calculated on a monthly basis instead of a strict number of days from the invoice date.  """  
      self.NumberOfDays:int = obj["NumberOfDays"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.MinimumDays:int = obj["MinimumDays"]
      """  Used for Terms Type (Day of Month)  """  
      self.DueOnDay:int = obj["DueOnDay"]
      """  Used for Tems Type (Day of Months)  """  
      self.NumberOfMonths:int = obj["NumberOfMonths"]
      """  Used for Terms Type (X Months + Y Days)  """  
      self.DiscountType:str = obj["DiscountType"]
      """  This field defines the type of the Discount  """  
      self.PartPayment:bool = obj["PartPayment"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.ReqLOC:bool = obj["ReqLOC"]
      """  Require Letter of Credit.  """  
      self.GlobalPurTerms:bool = obj["GlobalPurTerms"]
      """  Marks this PurTerms as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  COIFRSCalculation  """  
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  COIFRSNumberOfPeriods  """  
      self.MonthsInFuture:int = obj["MonthsInFuture"]
      """  Months In Future  """  
      self.DueDayOfMonth:int = obj["DueDayOfMonth"]
      """  DueDayOfMonth  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Indicate if the Purchase Term is default  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurTermsSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Unique identifier of the terms assigned by the user.  """  
      self.PaySeq:int = obj["PaySeq"]
      """  Specifies the number of payment of the Payment Schedule. This is an auto-generated sequence number.  """  
      self.Days:int = obj["Days"]
      """  Specifies the number of days for the payment to be paid. This is used to calculate Due Date in Invoice Payment Schedule.  """  
      self.PayPercent:int = obj["PayPercent"]
      """  Specifies the percent of the payment to be paid. This is used to calculate amount to be paid per payment in Purchase Order and Invoice Payment Sechedule.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of user who created this record.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date that the record was created.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurTermsTableset:
   def __init__(self, obj):
      self.PurTerms:list[Erp_Tablesets_PurTermsRow] = obj["PurTerms"]
      self.PurTermsAttch:list[Erp_Tablesets_PurTermsAttchRow] = obj["PurTermsAttch"]
      self.PurTermsDtl:list[Erp_Tablesets_PurTermsDtlRow] = obj["PurTermsDtl"]
      self.PurTermsSched:list[Erp_Tablesets_PurTermsSchedRow] = obj["PurTermsSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPurTermsTableset:
   def __init__(self, obj):
      self.PurTerms:list[Erp_Tablesets_PurTermsRow] = obj["PurTerms"]
      self.PurTermsAttch:list[Erp_Tablesets_PurTermsAttchRow] = obj["PurTermsAttch"]
      self.PurTermsDtl:list[Erp_Tablesets_PurTermsDtlRow] = obj["PurTermsDtl"]
      self.PurTermsSched:list[Erp_Tablesets_PurTermsSchedRow] = obj["PurTermsSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   termsCode
   """  
   def __init__(self, obj):
      self.termsCode:str = obj["termsCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurTermsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurTermsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurTermsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurTermsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPurTermsAttch_input:
   """ Required : 
   ds
   termsCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      self.termsCode:str = obj["termsCode"]
      pass

class GetNewPurTermsAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurTermsDtl_input:
   """ Required : 
   ds
   termsCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      self.termsCode:str = obj["termsCode"]
      pass

class GetNewPurTermsDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurTermsSched_input:
   """ Required : 
   ds
   termsCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      self.termsCode:str = obj["termsCode"]
      pass

class GetNewPurTermsSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurTerms_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class GetNewPurTerms_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPurTermsSched_input:
   """ Required : 
   termsCode
   purTermsSchedTable
   """  
   def __init__(self, obj):
      self.termsCode:str = obj["termsCode"]
      self.purTermsSchedTable:object
      pass

class GetPurTermsSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.purTermsSchedTable:list = obj[any]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePurTerms
   whereClausePurTermsAttch
   whereClausePurTermsDtl
   whereClausePurTermsSched
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePurTerms:str = obj["whereClausePurTerms"]
      self.whereClausePurTermsAttch:str = obj["whereClausePurTermsAttch"]
      self.whereClausePurTermsDtl:str = obj["whereClausePurTermsDtl"]
      self.whereClausePurTermsSched:str = obj["whereClausePurTermsSched"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurTermsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTermsTypeCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of Terms Type codes/descriptions  """  
      pass

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

class OnChangingDisDays_input:
   """ Required : 
   vDueOnDay
   ds
   """  
   def __init__(self, obj):
      self.vDueOnDay:int = obj["vDueOnDay"]
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class OnChangingDisDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingDisPercent_input:
   """ Required : 
   vDiscountPercent
   ds
   """  
   def __init__(self, obj):
      self.vDiscountPercent:int = obj["vDiscountPercent"]
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class OnChangingDisPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumOfDays_input:
   """ Required : 
   vNumOfDay
   ds
   """  
   def __init__(self, obj):
      self.vNumOfDay:int = obj["vNumOfDay"]
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class OnChangingNumOfDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumOfMonths_input:
   """ Required : 
   vNumOfMonths
   ds
   """  
   def __init__(self, obj):
      self.vNumOfMonths:int = obj["vNumOfMonths"]
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class OnChangingNumOfMonths_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingTermDueOnDay_input:
   """ Required : 
   pDueOnDay
   """  
   def __init__(self, obj):
      self.pDueOnDay:int = obj["pDueOnDay"]
      pass

class OnChangingTermDueOnDay_output:
   def __init__(self, obj):
      pass

class OnPurTermsSchedPercentageUpdate2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class OnPurTermsSchedPercentageUpdate2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnPurTermsSchedPercentageUpdate_input:
   """ Required : 
   ts
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_PurTermsTableset] = obj["ts"]
      pass

class OnPurTermsSchedPercentageUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ts:list[Erp_Tablesets_PurTermsTableset] = obj["ts"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPurTermsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPurTermsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateDiscountPercent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      pass

class ValidateDiscountPercent_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurTermsTableset] = obj["ds"]
      self.warningMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

