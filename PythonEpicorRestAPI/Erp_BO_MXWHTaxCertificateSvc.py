import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MXWHTaxCertificateSvc
# Description: CSF Mexico WHT Certificate BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MXWHTaxCertificates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertificates
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates",headers=creds) as resp:
           return await resp.json()

async def post_MXWHTaxCertificates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertificates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates_Company_CertificateNum(Company, CertificateNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXWHTaxCertificate item
   Description: Calls GetByID to retrieve the MXWHTaxCertificate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertificate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MXWHTaxCertificates_Company_CertificateNum(Company, CertificateNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MXWHTaxCertificate for the service
   Description: Calls UpdateExt to update MXWHTaxCertificate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertificate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MXWHTaxCertificates_Company_CertificateNum(Company, CertificateNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MXWHTaxCertificate item
   Description: Call UpdateExt to delete MXWHTaxCertificate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertificate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertDtls(Company, CertificateNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MXWHTaxCertDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXWHTaxCertDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertDtls",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company, CertificateNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXWHTaxCertDtl item
   Description: Calls GetByID to retrieve the MXWHTaxCertDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertErrors(Company, CertificateNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MXWHTaxCertErrors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXWHTaxCertErrors1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertErrors",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company, CertificateNum, ErrorSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXWHTaxCertError item
   Description: Calls GetByID to retrieve the MXWHTaxCertError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertError1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param ErrorSeq: Desc: ErrorSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertHeadAttches(Company, CertificateNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MXWHTaxCertHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MXWHTaxCertHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertificates_Company_CertificateNum_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company, CertificateNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item
   Description: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertificates(" + Company + "," + CertificateNum + ")/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MXWHTaxCertDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls",headers=creds) as resp:
           return await resp.json()

async def post_MXWHTaxCertDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company, CertificateNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXWHTaxCertDtl item
   Description: Calls GetByID to retrieve the MXWHTaxCertDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company, CertificateNum, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MXWHTaxCertDtl for the service
   Description: Calls UpdateExt to update MXWHTaxCertDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MXWHTaxCertDtls_Company_CertificateNum_LineNum(Company, CertificateNum, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MXWHTaxCertDtl item
   Description: Call UpdateExt to delete MXWHTaxCertDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertDtls(" + Company + "," + CertificateNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertErrors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MXWHTaxCertErrors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertErrors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors",headers=creds) as resp:
           return await resp.json()

async def post_MXWHTaxCertErrors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company, CertificateNum, ErrorSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXWHTaxCertError item
   Description: Calls GetByID to retrieve the MXWHTaxCertError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertError
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param ErrorSeq: Desc: ErrorSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company, CertificateNum, ErrorSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MXWHTaxCertError for the service
   Description: Calls UpdateExt to update MXWHTaxCertError. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertError
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param ErrorSeq: Desc: ErrorSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertErrorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MXWHTaxCertErrors_Company_CertificateNum_ErrorSeq(Company, CertificateNum, ErrorSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MXWHTaxCertError item
   Description: Call UpdateExt to delete MXWHTaxCertError item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertError
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param ErrorSeq: Desc: ErrorSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertErrors(" + Company + "," + CertificateNum + "," + ErrorSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MXWHTaxCertHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXWHTaxCertHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_MXWHTaxCertHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXWHTaxCertHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company, CertificateNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item
   Description: Calls GetByID to retrieve the MXWHTaxCertHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXWHTaxCertHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company, CertificateNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MXWHTaxCertHeadAttch for the service
   Description: Calls UpdateExt to update MXWHTaxCertHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXWHTaxCertHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXWHTaxCertHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MXWHTaxCertHeadAttches_Company_CertificateNum_DrawingSeq(Company, CertificateNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MXWHTaxCertHeadAttch item
   Description: Call UpdateExt to delete MXWHTaxCertHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXWHTaxCertHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CertificateNum: Desc: CertificateNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/MXWHTaxCertHeadAttches(" + Company + "," + CertificateNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXWHTaxCertHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMXWHTaxCertHead, whereClauseMXWHTaxCertHeadAttch, whereClauseMXWHTaxCertDtl, whereClauseMXWHTaxCertError, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMXWHTaxCertHead=" + whereClauseMXWHTaxCertHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMXWHTaxCertHeadAttch=" + whereClauseMXWHTaxCertHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMXWHTaxCertDtl=" + whereClauseMXWHTaxCertDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMXWHTaxCertError=" + whereClauseMXWHTaxCertError
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(certificateNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "certificateNum=" + certificateNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GenerateNewCerts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateNewCerts
   Description: Generate New CSF Mexico WHT Certificate Header and Details in DB
   OperationID: GenerateNewCerts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateNewCerts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewCerts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateNewCertsForSuppliers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateNewCertsForSuppliers
   Description: Generate New CSF Mexico WHT Certificate Header and Details in DB
   OperationID: GenerateNewCertsForSuppliers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateNewCertsForSuppliers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewCertsForSuppliers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MXWHTaxCertGetNewFilterSearch(epicorHeaders = None):
   """  
   Summary: Invoke method MXWHTaxCertGetNewFilterSearch
   Description: Return Get New Certificates Search Screen Values
   OperationID: MXWHTaxCertGetNewFilterSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MXWHTaxCertGetNewFilterSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GenerateMXWHTaxCertificate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateMXWHTaxCertificate
   Description: Creates MXWHTaxCertificate, stores it to the URL retrieved from docType.BaseURL, add it as attachment.
   OperationID: GenerateMXWHTaxCertificate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateMXWHTaxCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateMXWHTaxCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMXWHTaxCertificate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMXWHTaxCertificate
   Description: Validate MXWHTaxCertificate before generating XML. If some errors found then return error message
   OperationID: ValidateMXWHTaxCertificate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMXWHTaxCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMXWHTaxCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMXWHTaxCertificatesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMXWHTaxCertificatesList
   Description: Validate MXWHTaxCertificates List before generating XML. If some errors found then return error message
   OperationID: ValidateMXWHTaxCertificatesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMXWHTaxCertificatesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMXWHTaxCertificatesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMXWHTaxCertificates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMXWHTaxCertificates
   Description: Validate MXWHTaxCertificates List before generating XML. If some errors found then return error message
   OperationID: ValidateMXWHTaxCertificates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMXWHTaxCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMXWHTaxCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateMXWHTaxCertificates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateMXWHTaxCertificates
   Description: Creates MXWHTaxCertificate, stores it to the URL retrieved from docType.BaseURL, add it as attachment for all certificates numbers in the list.
   OperationID: GenerateMXWHTaxCertificates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateMXWHTaxCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateMXWHTaxCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Void Legal Number
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistWHTaxCert(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistWHTaxCert
   Description: Validate is WHTaxCertificate already existed
   OperationID: ExistWHTaxCert
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistWHTaxCert_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistWHTaxCert_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistWHTaxCert2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistWHTaxCert2
   Description: Validate is WHTaxCertificate already existed
   OperationID: ExistWHTaxCert2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistWHTaxCert2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistWHTaxCert2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRelatedCertificateNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRelatedCertificateNum
   Description: RelatedCertificateNum is changing
   OperationID: OnChangingRelatedCertificateNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRelatedCertificateNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRelatedCertificateNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockSuspendedCertificate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockSuspendedCertificate
   Description: Revert PACProcessing certificate to XMLGenerated
   OperationID: UnlockSuspendedCertificate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockSuspendedCertificate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockSuspendedCertificate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCertificatesByCertNumList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCertificatesByCertNumList
   Description: Returns list of Certificates according to given delimited list of cert numbers
   OperationID: GetCertificatesByCertNumList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCertificatesByCertNumList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCertificatesByCertNumList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMXWHTaxCertHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMXWHTaxCertHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMXWHTaxCertHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMXWHTaxCertHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMXWHTaxCertDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMXWHTaxCertDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMXWHTaxCertError(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMXWHTaxCertError
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMXWHTaxCertError
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMXWHTaxCertError_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMXWHTaxCertError_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXWHTaxCertificateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXWHTaxCertDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertErrorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXWHTaxCertErrorRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXWHTaxCertHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXWHTaxCertHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXWHTaxCertHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXWHTaxCertHeadRow] = obj["value"]
      pass

class Erp_Tablesets_MXWHTaxCertDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateNum:int = obj["CertificateNum"]
      """  CSF Mexico Withholding Certificate Number  """  
      self.LineNum:int = obj["LineNum"]
      """  CSF Mexico Line Number  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.PayType:str = obj["PayType"]
      """  CSF Mexico Payment Type  """  
      self.TaxType:str = obj["TaxType"]
      """  TaxType  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  TaxableAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ExemptAmt:int = obj["ExemptAmt"]
      """  CSF Mexico Exempt Amountt  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  CSF Mexico Total Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTranAPInvoiceNum:str = obj["TaxTranAPInvoiceNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertErrorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateNum:int = obj["CertificateNum"]
      """  CertificateNum  """  
      self.ErrorSeq:int = obj["ErrorSeq"]
      """  ErrorSeq  """  
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  ErrorMessage  """  
      self.StackTrace:str = obj["StackTrace"]
      """  StackTrace  """  
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CertificateNum:int = obj["CertificateNum"]
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

class Erp_Tablesets_MXWHTaxCertHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriodStart:int = obj["FiscalPeriodStart"]
      """  FiscalPeriodStart  """  
      self.FiscalPeriodEnd:int = obj["FiscalPeriodEnd"]
      """  FiscalPeriodEnd  """  
      self.SupplierNum:int = obj["SupplierNum"]
      """  Supplier Number  """  
      self.RetentionCode:str = obj["RetentionCode"]
      """  CSF Mexico Retention Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateNum:int = obj["CertificateNum"]
      """  CSF Mexico Withholding Certificate Number  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriodStart:int = obj["FiscalPeriodStart"]
      """  FiscalPeriodStart  """  
      self.FiscalPeriodEnd:int = obj["FiscalPeriodEnd"]
      """  FiscalPeriodEnd  """  
      self.SupplierNum:int = obj["SupplierNum"]
      """  Supplier Number  """  
      self.RetentionCode:str = obj["RetentionCode"]
      """  CSF Mexico Retention Code  """  
      self.IsForeignSupplement:bool = obj["IsForeignSupplement"]
      """  CSF Mexico. If the checkbox is checked, then foreign vendor supplement would be printed; If the checkbox is not checked, then foreign vendor supplement would not be printed.  """  
      self.IsSeparateLegalRep:bool = obj["IsSeparateLegalRep"]
      """   CSF Mexico. This field defines the value of EsBenefEfectDelCobro node and additionally if the NoBeneficiario element or the Beneficiario element is the one that prints.

If checkbox is checked (EsBenefEfectDelCobro equals SI), then the legal representative information would be included in the xml (Beneficiario nodes)

If checkbox is not checked (EsBenefEfectDelCobro equals NO), then the NoBeneficiario nodes would be the ones to be included.  """  
      self.SupplierTaxID:str = obj["SupplierTaxID"]
      """  SupplierTaxID  """  
      self.SupplierLegalName:str = obj["SupplierLegalName"]
      """  Supplier Legal Name  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.IssueDate:str = obj["IssueDate"]
      """  CSF Mexico Issue Date  """  
      self.Status:str = obj["Status"]
      """  CSF Mexico Status  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  TaxableAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ExemptAmt:int = obj["ExemptAmt"]
      """  CSF Mexico Exempt Amount  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  CSF Mexico Total Amountt  """  
      self.RetentionDescr:str = obj["RetentionDescr"]
      """  CSF Mexico Retention Description  """  
      self.Serie:str = obj["Serie"]
      """  CSF Mexico Serie  """  
      self.Folio:str = obj["Folio"]
      """  CSF Mexico Folio  """  
      self.CertifiedTimestamp:str = obj["CertifiedTimestamp"]
      """  CSF Mexico Certified Timestamp  """  
      self.CertificateSN:str = obj["CertificateSN"]
      """  CSF Mexico Digital Certificate Serial Number  """  
      self.Certificate:str = obj["Certificate"]
      """  CSF Mexico Digital Certificate  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  CSF Mexico Fiscal Folio  """  
      self.SATCertificateSN:str = obj["SATCertificateSN"]
      """  CSF Mexico SAT Certificate Serial Number  """  
      self.DigitalSeal:str = obj["DigitalSeal"]
      """  CSF Mexico Digital Seal  """  
      self.SATSeal:str = obj["SATSeal"]
      """  CSF Mexico SAT Digital Seal  """  
      self.OriginalString:str = obj["OriginalString"]
      """  CSF Mexico Original String  """  
      self.OriginalStringTFD:str = obj["OriginalStringTFD"]
      """  CSF Mexico Original String TFD  """  
      self.CancellationID:str = obj["CancellationID"]
      """  CSF Mexico Cancellation ID  """  
      self.CancellationStatus:int = obj["CancellationStatus"]
      """  CSF Mexico Cancellation Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RelatedCertificateNum:int = obj["RelatedCertificateNum"]
      """  RelatedCertificateNum  """  
      self.RelationType:str = obj["RelationType"]
      """  RelationType  """  
      self.SupplierID:str = obj["SupplierID"]
      """  Supplier ID  """  
      self.Errors:str = obj["Errors"]
      """  Text of all error messages related to current certificate from MXWHTaxCertError table  """  
      self.StatusDescription:str = obj["StatusDescription"]
      """  CSF Mexico Status Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RetentionCodeLongDesc:str = obj["RetentionCodeLongDesc"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCity:str = obj["VendorCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   certificateNum
   """  
   def __init__(self, obj):
      self.certificateNum:int = obj["certificateNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MXWHTaxCertDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateNum:int = obj["CertificateNum"]
      """  CSF Mexico Withholding Certificate Number  """  
      self.LineNum:int = obj["LineNum"]
      """  CSF Mexico Line Number  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.PayType:str = obj["PayType"]
      """  CSF Mexico Payment Type  """  
      self.TaxType:str = obj["TaxType"]
      """  TaxType  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  TaxableAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ExemptAmt:int = obj["ExemptAmt"]
      """  CSF Mexico Exempt Amountt  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  CSF Mexico Total Amount  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTranAPInvoiceNum:str = obj["TaxTranAPInvoiceNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertErrorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateNum:int = obj["CertificateNum"]
      """  CertificateNum  """  
      self.ErrorSeq:int = obj["ErrorSeq"]
      """  ErrorSeq  """  
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  ErrorMessage  """  
      self.StackTrace:str = obj["StackTrace"]
      """  StackTrace  """  
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertGetNewFilterRow:
   def __init__(self, obj):
      self.EndingFiscalPeriod:int = obj["EndingFiscalPeriod"]
      """  EndingFiscalPeriod  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.StartingFiscalPeriod:int = obj["StartingFiscalPeriod"]
      """  StartingFiscalPeriod  """  
      self.SupplierLabel:str = obj["SupplierLabel"]
      """  SupplierLabel  """  
      self.Suppliers:str = obj["Suppliers"]
      """  Suppliers  """  
      self.SuppliersSelected:str = obj["SuppliersSelected"]
      """  SuppliersSelected  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertGetNewTableset:
   def __init__(self, obj):
      self.MXWHTaxCertGetNewFilter:list[Erp_Tablesets_MXWHTaxCertGetNewFilterRow] = obj["MXWHTaxCertGetNewFilter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MXWHTaxCertHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CertificateNum:int = obj["CertificateNum"]
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

class Erp_Tablesets_MXWHTaxCertHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriodStart:int = obj["FiscalPeriodStart"]
      """  FiscalPeriodStart  """  
      self.FiscalPeriodEnd:int = obj["FiscalPeriodEnd"]
      """  FiscalPeriodEnd  """  
      self.SupplierNum:int = obj["SupplierNum"]
      """  Supplier Number  """  
      self.RetentionCode:str = obj["RetentionCode"]
      """  CSF Mexico Retention Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertHeadListTableset:
   def __init__(self, obj):
      self.MXWHTaxCertHeadList:list[Erp_Tablesets_MXWHTaxCertHeadListRow] = obj["MXWHTaxCertHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MXWHTaxCertHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CertificateNum:int = obj["CertificateNum"]
      """  CSF Mexico Withholding Certificate Number  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriodStart:int = obj["FiscalPeriodStart"]
      """  FiscalPeriodStart  """  
      self.FiscalPeriodEnd:int = obj["FiscalPeriodEnd"]
      """  FiscalPeriodEnd  """  
      self.SupplierNum:int = obj["SupplierNum"]
      """  Supplier Number  """  
      self.RetentionCode:str = obj["RetentionCode"]
      """  CSF Mexico Retention Code  """  
      self.IsForeignSupplement:bool = obj["IsForeignSupplement"]
      """  CSF Mexico. If the checkbox is checked, then foreign vendor supplement would be printed; If the checkbox is not checked, then foreign vendor supplement would not be printed.  """  
      self.IsSeparateLegalRep:bool = obj["IsSeparateLegalRep"]
      """   CSF Mexico. This field defines the value of EsBenefEfectDelCobro node and additionally if the NoBeneficiario element or the Beneficiario element is the one that prints.

If checkbox is checked (EsBenefEfectDelCobro equals SI), then the legal representative information would be included in the xml (Beneficiario nodes)

If checkbox is not checked (EsBenefEfectDelCobro equals NO), then the NoBeneficiario nodes would be the ones to be included.  """  
      self.SupplierTaxID:str = obj["SupplierTaxID"]
      """  SupplierTaxID  """  
      self.SupplierLegalName:str = obj["SupplierLegalName"]
      """  Supplier Legal Name  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.IssueDate:str = obj["IssueDate"]
      """  CSF Mexico Issue Date  """  
      self.Status:str = obj["Status"]
      """  CSF Mexico Status  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  TaxableAmt  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  TaxAmt  """  
      self.ExemptAmt:int = obj["ExemptAmt"]
      """  CSF Mexico Exempt Amount  """  
      self.TotalAmt:int = obj["TotalAmt"]
      """  CSF Mexico Total Amountt  """  
      self.RetentionDescr:str = obj["RetentionDescr"]
      """  CSF Mexico Retention Description  """  
      self.Serie:str = obj["Serie"]
      """  CSF Mexico Serie  """  
      self.Folio:str = obj["Folio"]
      """  CSF Mexico Folio  """  
      self.CertifiedTimestamp:str = obj["CertifiedTimestamp"]
      """  CSF Mexico Certified Timestamp  """  
      self.CertificateSN:str = obj["CertificateSN"]
      """  CSF Mexico Digital Certificate Serial Number  """  
      self.Certificate:str = obj["Certificate"]
      """  CSF Mexico Digital Certificate  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  CSF Mexico Fiscal Folio  """  
      self.SATCertificateSN:str = obj["SATCertificateSN"]
      """  CSF Mexico SAT Certificate Serial Number  """  
      self.DigitalSeal:str = obj["DigitalSeal"]
      """  CSF Mexico Digital Seal  """  
      self.SATSeal:str = obj["SATSeal"]
      """  CSF Mexico SAT Digital Seal  """  
      self.OriginalString:str = obj["OriginalString"]
      """  CSF Mexico Original String  """  
      self.OriginalStringTFD:str = obj["OriginalStringTFD"]
      """  CSF Mexico Original String TFD  """  
      self.CancellationID:str = obj["CancellationID"]
      """  CSF Mexico Cancellation ID  """  
      self.CancellationStatus:int = obj["CancellationStatus"]
      """  CSF Mexico Cancellation Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RelatedCertificateNum:int = obj["RelatedCertificateNum"]
      """  RelatedCertificateNum  """  
      self.RelationType:str = obj["RelationType"]
      """  RelationType  """  
      self.SupplierID:str = obj["SupplierID"]
      """  Supplier ID  """  
      self.Errors:str = obj["Errors"]
      """  Text of all error messages related to current certificate from MXWHTaxCertError table  """  
      self.StatusDescription:str = obj["StatusDescription"]
      """  CSF Mexico Status Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RetentionCodeLongDesc:str = obj["RetentionCodeLongDesc"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorName:str = obj["VendorName"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCity:str = obj["VendorCity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXWHTaxCertificateTableset:
   def __init__(self, obj):
      self.MXWHTaxCertHead:list[Erp_Tablesets_MXWHTaxCertHeadRow] = obj["MXWHTaxCertHead"]
      self.MXWHTaxCertHeadAttch:list[Erp_Tablesets_MXWHTaxCertHeadAttchRow] = obj["MXWHTaxCertHeadAttch"]
      self.MXWHTaxCertDtl:list[Erp_Tablesets_MXWHTaxCertDtlRow] = obj["MXWHTaxCertDtl"]
      self.MXWHTaxCertError:list[Erp_Tablesets_MXWHTaxCertErrorRow] = obj["MXWHTaxCertError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMXWHTaxCertificateTableset:
   def __init__(self, obj):
      self.MXWHTaxCertHead:list[Erp_Tablesets_MXWHTaxCertHeadRow] = obj["MXWHTaxCertHead"]
      self.MXWHTaxCertHeadAttch:list[Erp_Tablesets_MXWHTaxCertHeadAttchRow] = obj["MXWHTaxCertHeadAttch"]
      self.MXWHTaxCertDtl:list[Erp_Tablesets_MXWHTaxCertDtlRow] = obj["MXWHTaxCertDtl"]
      self.MXWHTaxCertError:list[Erp_Tablesets_MXWHTaxCertErrorRow] = obj["MXWHTaxCertError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistWHTaxCert2_input:
   """ Required : 
   certificateNum
   isRelated
   """  
   def __init__(self, obj):
      self.certificateNum:int = obj["certificateNum"]
      """  certificateNum  """  
      self.isRelated:bool = obj["isRelated"]
      """  Is Certificate related or not  """  
      pass

class ExistWHTaxCert2_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ExistWHTaxCert_input:
   """ Required : 
   certificateNum
   """  
   def __init__(self, obj):
      self.certificateNum:int = obj["certificateNum"]
      """  certificateNum  """  
      pass

class ExistWHTaxCert_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GenerateMXWHTaxCertificate_input:
   """ Required : 
   certificateNum
   """  
   def __init__(self, obj):
      self.certificateNum:int = obj["certificateNum"]
      """  Certificate number  """  
      pass

class GenerateMXWHTaxCertificate_output:
   def __init__(self, obj):
      pass

class GenerateMXWHTaxCertificates_input:
   """ Required : 
   certificateNumsList
   """  
   def __init__(self, obj):
      self.certificateNumsList:str = obj["certificateNumsList"]
      """  List of the Certificates numbers  """  
      pass

class GenerateMXWHTaxCertificates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class GenerateNewCertsForSuppliers_input:
   """ Required : 
   fiscalYear
   fiscalYearSuffix
   startFiscalPeriod
   endFiscalPeriod
   suppliersList
   warningText
   """  
   def __init__(self, obj):
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.startFiscalPeriod:int = obj["startFiscalPeriod"]
      """  Starting Fiscal Period  """  
      self.endFiscalPeriod:int = obj["endFiscalPeriod"]
      """  Ending Fiscal Period  """  
      self.suppliersList:str = obj["suppliersList"]
      """  List of Suppliers  """  
      self.warningText:str = obj["warningText"]
      """  ref Warnings. Example: There are existing certificates for the same period, supplier, retencionCode  """  
      pass

class GenerateNewCertsForSuppliers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GenerateNewCerts_input:
   """ Required : 
   fiscalYear
   fiscalYearSuffix
   startFiscalPeriod
   endFiscalPeriod
   warningText
   """  
   def __init__(self, obj):
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.startFiscalPeriod:int = obj["startFiscalPeriod"]
      """  Starting Fiscal Period  """  
      self.endFiscalPeriod:int = obj["endFiscalPeriod"]
      """  Ending Fiscal Period  """  
      self.warningText:str = obj["warningText"]
      """  ref Warnings. Example: There are existing certificates for the same period, supplier, retencionCode  """  
      pass

class GenerateNewCerts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   certificateNum
   """  
   def __init__(self, obj):
      self.certificateNum:int = obj["certificateNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["returnObj"]
      pass

class GetCertificatesByCertNumList_input:
   """ Required : 
   certNumList
   """  
   def __init__(self, obj):
      self.certNumList:str = obj["certNumList"]
      """  Delimited list of certificates numbers  """  
      pass

class GetCertificatesByCertNumList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMXWHTaxCertDtl_input:
   """ Required : 
   ds
   certificateNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      self.certificateNum:int = obj["certificateNum"]
      pass

class GetNewMXWHTaxCertDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMXWHTaxCertError_input:
   """ Required : 
   ds
   certificateNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      self.certificateNum:int = obj["certificateNum"]
      pass

class GetNewMXWHTaxCertError_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMXWHTaxCertHeadAttch_input:
   """ Required : 
   ds
   certificateNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      self.certificateNum:int = obj["certificateNum"]
      pass

class GetNewMXWHTaxCertHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMXWHTaxCertHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      pass

class GetNewMXWHTaxCertHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMXWHTaxCertHead
   whereClauseMXWHTaxCertHeadAttch
   whereClauseMXWHTaxCertDtl
   whereClauseMXWHTaxCertError
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMXWHTaxCertHead:str = obj["whereClauseMXWHTaxCertHead"]
      self.whereClauseMXWHTaxCertHeadAttch:str = obj["whereClauseMXWHTaxCertHeadAttch"]
      self.whereClauseMXWHTaxCertDtl:str = obj["whereClauseMXWHTaxCertDtl"]
      self.whereClauseMXWHTaxCertError:str = obj["whereClauseMXWHTaxCertError"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["returnObj"]
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

class MXWHTaxCertGetNewFilterSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertGetNewTableset] = obj["returnObj"]
      pass

class OnChangingRelatedCertificateNum_input:
   """ Required : 
   strCertificateNum
   """  
   def __init__(self, obj):
      self.strCertificateNum:str = obj["strCertificateNum"]
      pass

class OnChangingRelatedCertificateNum_output:
   def __init__(self, obj):
      pass

class UnlockSuspendedCertificate_input:
   """ Required : 
   certNum
   """  
   def __init__(self, obj):
      self.certNum:int = obj["certNum"]
      """  Certificate Number  """  
      pass

class UnlockSuspendedCertificate_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMXWHTaxCertificateTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMXWHTaxCertificateTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateMXWHTaxCertificate_input:
   """ Required : 
   certificateNum
   """  
   def __init__(self, obj):
      self.certificateNum:int = obj["certificateNum"]
      """  Certificate Number  """  
      pass

class ValidateMXWHTaxCertificate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidateMXWHTaxCertificatesList_input:
   """ Required : 
   certificateNumsList
   """  
   def __init__(self, obj):
      self.certificateNumsList:str = obj["certificateNumsList"]
      """  Certificates Numbers List  """  
      pass

class ValidateMXWHTaxCertificatesList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidateMXWHTaxCertificates_input:
   """ Required : 
   certificateNumsList
   """  
   def __init__(self, obj):
      self.certificateNumsList:int = obj["certificateNumsList"]
      """  Certificates Numbers List  """  
      pass

class ValidateMXWHTaxCertificates_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class VoidLegalNumber_input:
   """ Required : 
   ipCertificateNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipCertificateNum:int = obj["ipCertificateNum"]
      """  certificateNum  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  reason  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXWHTaxCertificateTableset] = obj["returnObj"]
      pass

